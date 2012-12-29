#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robdd import Robdd
from operators import Bdd


def synthesize(expression_a, operator, expression_b):
    s = Synthesis()

    s.expression_a = expression_a
    s.expression_b = expression_b
    s.operator = operator

    s.synthesize()
    return s.result



# makes an operation over two expressions with an operator
class Synthesis:

    def __init__(self) :
        self.memo = { }

        self.operator = None
        self.expression_a = None
        self.expression_b = None

        self.result = None

        self.errors = []


    def synthesize(self):
        if self.expression_a == None or not isinstance(self.expression_a, Robdd):
            raise "Expression A is not a Robdd object."

        if self.expression_b == None or not isinstance(self.expression_b, Robdd):
            raise "Expression B is not a Robdd object."
        
        if self.operator not in [Bdd.AND, Bdd.OR, Bdd.IMPL, Bdd.BIIMPL] :
            raise "Invalid operator."

        self.result = Robdd()
        self.result.root = self._synth(self.expression_a.root, self.expression_b.root)

        return self.result

    def _synth(self, a_index, b_index) :

        if self.has_memo((a_index, b_index)) :
            return self.memo[(a_index, b_index)]

        # print "_synth {}, {}".format(a_index, b_index)
        # print "   A is leaf:", self._is_leaf(a_index)
        # print "   B is leaf:", self._is_leaf(b_index)

        i_a, t_a, f_a = self.expression_a.items[a_index]
        i_b, t_b, f_b = self.expression_b.items[b_index]

        if self._is_leaf(a_index) and self._is_leaf(b_index) :
            # print "   operating leaves"
            result = self._operate(a_index, b_index)

        elif i_a == i_b :
            # print "   operating nodes"
            result = self.result.insert(i_a, 
                                        self._synth(t_a, t_b), 
                                        self._synth(f_a, f_b))

        elif i_a < i_b:
            # print "   advancing A"
            result = self.result.insert(i_a,
                                        self._synth(t_a, b_index),
                                        self._synth(f_a, b_index))

        # elif i_a > i_b:
        else :
            # print "   advancing B"
            result = self.result.insert(i_b,
                                        self._synth(a_index, t_b),
                                        self._synth(a_index, f_b))

        self.memo[(a_index, b_index)] = result

        return result


    def _operate(self, a_index, b_index) :
        a = self._index_to_bool(a_index)
        b = self._index_to_bool(b_index)

        if self.operator == Bdd.AND :
            return a and b

        if self.operator == Bdd.OR :
            return a or b

        if self.operator == Bdd.IMPL :
            return False if (a and not b) else True

        if self.operator == Bdd.BIIMPL :
            return a == b

        raise "Unknown operator."

    def has_memo(self, tuple) :
        return tuple in self.memo

    def _is_leaf(self, index) :
        return index == 0 or index == 1

    def _index_to_bool(self, index):
        return index == 1
