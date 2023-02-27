"""
How For Loop in Python Works Internally?
To understand how for loops work internally, you must have a good understanding of iterators in Python. You must know the difference between the iterable and iterator. First, let’s see these terms.

Iterable: It is an object in Python in which iter() or getitem() methods are defined. On a higher level, if something is iterable, then it simply means that it can be looped over. If something is iterable or can be looped over, then it must have iter() method. For example, list, tuple, dictionary, set, or strings are all iterables.
Iterator: Iterator is a Python object with a state such that it remembers where it is during the iterations. Also, the iterator has the next() method defined which helps to fetch consecutive elements stored one after the other in the iterable.
In short, Iterable is a sequence or a series of elements that can be iterated over, and an iterator keeps track of the elements of iterable and lets us check if it has more elements and helps to move to the next element(if any) in the series.

For loops in python are used to iterate over any iterable objects (For example, list, tuple, dictionary, set, or string).

"""

# Python program
country = ['India', 'UAE', 'United Kingdom']
for x in country:
    print(x)
