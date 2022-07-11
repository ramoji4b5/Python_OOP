# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:35:07 2020

@author: ramoj
"""

''' 
Define the generator function fib_gen, which is capable of yielding values of infinite fibonacci series.

For e.g : You should able to create a generator fs from fib_gen and if fs is accessed using next for four times, then it should yield values 0, 1, 1, 2. You may type python3.5 to use the latest version for the exercise
'''
def fib_gen():
  a,b=0,1
  while a<4:
    yield a
    print('---', a)
    a,b=b,a+b

fs=fib_gen()
print(next(fs))
print(next(fs))
print(next(fs))
print(next(fs))



def factorial_gen(x):
  if x == 1 or x == 0:
    return 1
  else:
    return x * factorial_gen(x-1)

fs=factorial_gen(3)
print(next(fs))
print(next(fs))
print(next(fs))



def factorial_gen(x):
    a,b=0,1
    while a<4:
        yield a
    a,b=b,a+b

fs=factorial_gen(3)
print(next(fs))
print(next(fs))
print(next(fs))


def factorial_series():

    fs = factorial_gen()

    print(next(fs))

    print(next(fs))

    print(next(fs))

    print(next(fs))

def factorial_gen():
    a,b = 0, 1
    while True:
        if a == 0:
            yield 1
        else:
            for num in range(a,0,-1):
                b = b*num
            yield b
    a += 1
    b = 1

factorial_series()
