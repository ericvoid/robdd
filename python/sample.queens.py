#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ite import Ite
from robdd import Robdd
from synthesis import synthesize
from operators import Bdd


synth = synthesize


def queens(n):

    solution = Robdd.true()

    # put one queen in each line
    for j in range(1, n + 1):
        line = Robdd.false()

        for i in range(1, n + 1):
            queen = Robdd.make_x(index_of(i, j))
            line = synth(line, Bdd.OR, queen)

        solution = synth(solution, Bdd.AND, line)

    # create one variable for each boad position
    board = {}
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            board[(i, j)] = Robdd.make_not_x(index_of(i, j))

    # create conditions for each position
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            queen = queen_conditions(board, i, j, n)
            solution = synth(solution, Bdd.AND, queen)
    
    # print "   vars:", len(solution.variables)
    # print "   len:", solution.solutions_len()
    # print "   sol:", len(solution.get_solutions())
    # print "nodes:"
    # print solution.list()
    # print "tree:"
    # print solution

    return solution


def queen_conditions(board, i, j, n) :
    queen = Robdd.make_x(index_of(i, j))
    
    a = Robdd.true()
    b = Robdd.true()
    c = Robdd.true()
    d = Robdd.true()

    expression = Robdd()

    # creates the rule "none in the same column"
    for y in range(1, n + 1) :
        if y == j : continue

        a_ = synth(queen, Bdd.IMPL, board[(i, y)])
        a = synth(a, Bdd.AND, a_)

    # creates the rule "none in the same line"
    for x in range(1, n + 1) :
        if x == i : continue

        b_ = synth(queen, Bdd.IMPL, board[(x, j)])
        b = synth(b, Bdd.AND, b_)

    # creates the rule "none in the diagonals"
    x = 1
    while True :
        if (i - x) < 1 or (j - x) < 1 : break

        c_ = synth(queen, Bdd.IMPL, board[(i - x, j - x)])
        c  = synth(c, Bdd.AND, c_)
        x += 1

    x = 1
    while True :
        if (i + x) > n or (j + x) > n : break

        c_ = synth(queen, Bdd.IMPL, board[(i + x, j + x)])
        c  = synth(c, Bdd.AND, c_)
        x += 1

    x = 1
    while True :
        if (i - x) < 1 or (j + x) > n : break

        d_ = synth(queen, Bdd.IMPL, board[(i - x, j + x)])
        d  = synth(d, Bdd.AND, d_)
        x += 1

    x = 1
    while True :
        if (i + x) > n or (j - x) < 1 : break

        d_ = synth(queen, Bdd.IMPL, board[(i + x, j - x)])
        d  = synth(d, Bdd.AND, d_)
        x += 1

    return synth(synth(a, Bdd.AND, b), Bdd.AND, synth(c, Bdd.AND, d))




def index_of(i, j) :
    return i + ((j - 1) * n)


if __name__ == "__main__":
    from time import time

    for n in range(1,15):
        start = time()

        result = queens(n)
        
        elapsed = time() - start

        print "N =", n
        print "   S =", result.solutions_len()
        print "   t = %.2fs" % elapsed
        print "   nodes (reduced) =", result.insert_distinct
        print "   nodes (attempts)=", result.insert_attempts