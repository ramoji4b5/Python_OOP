"""String Method exercise 2"""

""" istitle()
Returns true if string is a titled cased string
Syntax:str.istitle()"""

S = 'Hello World'
print(S.istitle())
S = '!!! Hello World $$$'
print(S.istitle())
S = 'H@l0 T#ere'
print(S.istitle())

"""
isupper()
Returns true if all characters in a string are uppercase, else returns false.
Syntax:str.isupper()
"""

S = 'HELLO WORLD'
x = S.isupper()
print(x)
S = 'H@!!O W@RLD'
x = S.isupper()
print(x)
S = 'ABCDe'
x = S.isupper()
print(x)

"""
join()
Returns a string by joining all the elements of an iterable collection.
These iterable collections include: List, Tuple, Set & Dictionary.

Syntax:str.join(collection)

Parameters:
Collection: These iterable collections include: List, Tuple, Set & Dictionary.
Note:
Join(), joins keys of the dictionary and NOT the values. When joining sets, the resulting string may be any random join of elements of the set, as set is an unordered collection
"""
L = ['yesterday', 'today', 'tomorrow']
x = ' then '.join(L)
print(x)
L = ['yesterday', 'today', 'tomorrow']
S = {'ramoji','lakshmoji','swami'}
x = '\n'.join(L)
y = '\t'.join(L)
print(x)
print(y)
z = '\t'.join(S)
print(z)

