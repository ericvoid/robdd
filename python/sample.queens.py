#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ite import Ite
from robdd import Robdd
from synthesis import synthesize
from operators import Bdd


synth = synthesize


def queens(n):

    solution = Robdd.true()

    # create the rule "there must be at least one queen at each line"
    for j in range(1, n + 1):
        line = Robdd.false()

        for i in range(1, n + 1):
            queen = Robdd.make_x(index_of(i, j))
            line = synth(line, Bdd.OR, queen)

        solution = synth(solution, Bdd.AND, line)

    # create a list of "NOT" expressions
    not_expressions = {}
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            not_expressions[(i, j)] = Robdd.make_not_x(index_of(i, j))

    # create conditions for each position
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            queen = queen_conditions(not_expressions, i, j, n)
            solution = synth(solution, Bdd.AND, queen)
    
    return solution


def queen_conditions(not_x, i, j, n) :
    queen = Robdd.make_x(index_of(i, j))

    # creates the rule "none in the same column"
    a = Robdd.true()
    for y in range(1, n + 1) :
        if y == j : continue

        a_ = synth(queen, Bdd.IMPL, not_x[(i, y)])
        a  = synth(a, Bdd.AND, a_)

    # creates the rule "none in the same line"
    b = Robdd.true()
    for x in range(1, n + 1) :
        if x == i : continue

        b_ = synth(queen, Bdd.IMPL, not_x[(x, j)])
        b  = synth(b, Bdd.AND, b_)

    # creates the rule "none in the diagonals"
    c = Robdd.true()
    x = 1
    while (i - x) > 0 and (j - x) > 0 :
        c_ = synth(queen, Bdd.IMPL, not_x[(i - x, j - x)])
        c  = synth(c, Bdd.AND, c_)
        x += 1

    x = 1
    while (i + x) <= n and (j + x) <= n :
        c_ = synth(queen, Bdd.IMPL, not_x[(i + x, j + x)])
        c  = synth(c, Bdd.AND, c_)
        x += 1

    d = Robdd.true()
    x = 1
    while (i - x) > 0 and (j + x) <= n : 
        d_ = synth(queen, Bdd.IMPL, not_x[(i - x, j + x)])
        d  = synth(d, Bdd.AND, d_)
        x += 1

    x = 1
    while (i + x) <= n and (j - x) > 0 :

        d_ = synth(queen, Bdd.IMPL, not_x[(i + x, j - x)])
        d  = synth(d, Bdd.AND, d_)
        x += 1

    return synth(synth(a, Bdd.AND, b), Bdd.AND, synth(c, Bdd.AND, d))




def index_of(i, j) :
    return i + ((j - 1) * n)
    


if __name__ == "__main__":
    from time import time

    for n in range(1,9):
        start = time()

        result = queens(n)
        
        elapsed = time() - start

        print "N =", n
        print "   solutions       =", result.solutions_len()
        print "   elapsed time    = %.2fs" % elapsed
        print "   variables       =", len(result.variables)
        print "   nodes (reduced) =", result.insert_distinct
        print "   nodes (attempts)=", result.insert_attempts
