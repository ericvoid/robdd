Intro
=====

Decision Diagram is a data structure for representing and manipulating boolean expressions. 
In its restrict form, called Reduced Ordered Binary Decision Diagram (ROBDD),
its application became comprehensive for its canonical aspect and for allowing efficient manipulations.

The package includes a sample - sample.queens.py. It is a solution for the N Queens Problem aka Eight Queens Puzzle:
http://en.wikipedia.org/wiki/Eight_queens_puzzle


Background
==========

This code was originally written for monography (back to 2006) in PHP language. I
was mentored by Silvio do Lago Pereira PhD - http://www.ime.usp.br/~slago/

I know that using PHP for AI is awful (for plenty of reasons), 
but I choose that language because I had experience with it and it wouldn't be a 
hindrance to the progress of the monography.

The current code is a translation of the PHP original code to Python. It has few ajustments; 
curly braces are gone, there are tuples and more powerful list and dictionary manipulation methods.

The greatest change during this translation is that I completely discaded a Memoizing class. 
It was possible to completely replace it using a dictionary with tuple-keys.

I actually do not have the source code in PHP anymore, just a print version of it O.o!


Future Dev
==========

There are still many improvements to be done on this code. Teletex me for suggestions.

And also I'm planning to implement it in Haskell. I'm currently studying that language and
eventualy I will figure out how to translate it from an imperative language to a purely functional one.

