# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:58:30 2020

@author: ramoj
"""

'''def factrorial_gen():
    return x

fs=factrorial_gen()
print(next(fs))
print(next(fs))
print(next(fs))'''


'''def factrorial_gen(n):
    start = 1
    fact = 1
    while start <= n :
       yield fact
       start = start + 1
       fact = fact * start
 
fs = factrorial_gen(5)
print(next(fs))
print(next(fs))
print(next(fs))'''
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        start = 1
        fact = 1
        while start <= n :
            yield fact
            start = start + 1
            fact = fact * start
 
func = factorial(1)
print(next(func))'''

'''
def factrorial_gen(n):
    start = 1
    fact = 1
    while start <= n :
       yield fact
       start = start + 1
       fact = fact * start
 
fs = factrorial_gen(5)
print(next(fs))
print(next(fs))
print(next(fs))'''


'''
def factorial(n):
    count = 1
    fact = 1
    while count <= n:
        yield fact
        count = count + 1
        fact = fact * count

print('Factorial program using generators.')
fs = factorial(0)
print(next(fs))
print(next(fs))
print(next(fs)) '''


def factrorial_gen(x):
    a = 1
    b = 1
    if x == 0:
        a = 1
    if x < 0:
        print('enter valid whole number!')
    if x > 0:
        while b < x:
            a = a * b
            b += 1
    return a
#main
z = 3
fs = (factrorial_gen(n) for n in range(0,z))
print(next(fs))
print(next(fs))
print(next(fs))



def fact(x):
    a = 1
    b = 1
    if x == 0:
        a = 1
    if x < 0:
        print('enter valid whole number!')
    if x > 0:
        while b < x:
            a = a * b
            b += 1
            yield a
            
#main
z = 3
g = (fact(n) for n in range (0,int(z)))
print(next(g))
print(next(g))
print(next(g))