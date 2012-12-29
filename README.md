Intro
=====

Decision Diagram is a data structure for representing and manipulating boolean expressions. 
In its restrict form, called Reduced Ordered Binary Decision Diagram (ROBDD),
ts application became comprehensive for its canonical aspect and for allowing efficient manipulations.

The package includes a sample - sample.queens.py. It is a solution for the N Queens Problem aka Eight Queens Puzzle:
http://en.wikipedia.org/wiki/Eight_queens_puzzle


Background
==========

This code was originally written for monography (back to 2006) in PHP language. 
I know that's awful (for plenty of reasons). 
But I spent a few hours in the last two days to translate it into Python.

The current code is a translation from the PHP code. It has few ajustments; 
curly braces are gone, there are tuples and more powerful list manipulation methods.

The greatest change during this translation is that I completely discaded a Memoizing class. 
It was possible to completely replace it combining the dictionary with tuples.

I actually do not have the PHP code files anymore, just a print version of it O.o!


Future Dev
==========

There are still many improvements to be done on this code. Teletex me for suggestions.

And also I'm planning to implement it in Haskell. I'm currently studying that language and
eventualy I will figure out how to translate it from an imperative language to a purely functional one.

