# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:23:12 2020

@author: ramoj
"""

zenPython = '''

The Zen of Python, by Tim Peters


Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!

'''

#words=zenPython.split('\n')
words=zenPython.split(' ')
print(words)
print(len(words))

def strip(s):
   news=''
   ignore=set(',.-*! \n')
   #print(ignore)
   for letter in s:
      #print(letter)
      if letter not in ignore:
          news+=letter
          #print(news)
   return news

print(strip('Ramoji,.-*'))

s= 'ramoji-,@'
print(strip('@'))




words=[s.strip(',.-*! ')  for s in words]
print('using strip function',words)