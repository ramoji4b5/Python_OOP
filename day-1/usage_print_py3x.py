import sys

print('Python version is', sys.version[:3])

print('Hello, World!')  # if you remove parentheses here it will throw a syntax error

print("content ", end="");
print('more content')

print("The answer is", 2 * 2)

print(10, end=" ")  # end = " " appends space instead of new line

print()  # Prints a newline

print("fatal error", file=sys.stderr)

####################################
"""Python 3.x division operator:"""
import sys

print('Python version is', sys.version[:3])

print('5 / 4 =', 5 / 4)

print('5 // 4 =', 5 // 4)

print('5 / 4.0 =', 5 / 4.0)

print('5 // 4.0 =', 5 // 4.0)

"""Python 3.x Unicode Strings:"""

import sys

print('Python version is', sys.version[:3])

print(type('default string '))  # unicode
print(type(b'string with b '))  # bytes and default both different in python 3

"""Python 3.x range:"""

import sys

print('Python version is', sys.version[:3])

for x in range(1, 5):  # if you replace range with xrange here it will throw an error
    print(x, end=" ")

"""Python 3.x list comprehension:"""
import sys

print('Python version is', sys.version[:3])

x = 100

print("global x before iteration: ", x)

print('comprehension: ', [x for x in range(5)])

print("global x after iteration: ", x)

