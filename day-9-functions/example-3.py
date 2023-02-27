"""Categorizing Functions in Python based on Parameters and Return Value"""
"""Without parameters, without return statement"""
def hello():
    print("Hello World!")
hello()
"""With Parameters, without return statement"""
def hello(fname):
    print("Hello " + fname)
hello("Tina")
"""Without parameters, with the return statement"""


def isEven(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Not Even"


even10 = isEven(10)
print(even10)

"""With parameters, with return statement"""
def sum(a, b):
   return a + b
total=sum(10,20)
print(total)

"""Recursive Functions in Python"""
"""Recursion is the process in which a function calls itself. Recursive functions are used mostly for sequence generation and are used to make the code look clean and elegant."""
def rec_sum(n):
    if n<=1:
        return n
    else:
        return n + rec_sum(n-1)
y = rec_sum(5)
print(y)

"""Anonymous Functions in Python"""
"""An anonymous in python is a function that is defined without a name. 
Unlike functions defined using the def keyword, these are defined using the lambda keyword and are hence called lambda functions. 
They can have 0 or more arguments but only one return value"""

"""
Syntax: lambda arguments: expression
"""
square = lambda x: x * x
print(square(2))

def square(x):
  return x * 2
print(square(2))

"""Pass Statement
Empty functions are used as a means of time delay. 
Since functions cannot be empty, the pass statement can be used to avoid errors caused by a lack of statements."""
def function1():
    pass

"""Python neither uses pass by value nor pass by reference mechanism, but it uses pass by object reference sort of mechanism."""



