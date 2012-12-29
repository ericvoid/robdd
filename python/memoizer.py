#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Memoizer:

    def __init__(self):
        self.items = []

    # adds an item to the memoizer
    def add(self, entry, result):
        self.items.append(MemoItem(entry, result))

    def find(self, entry):
        raise "not implemented"


# for local usage
class MemoItem:
    def __init(self, entry, result):
        self.entry = entry
        self.result = result