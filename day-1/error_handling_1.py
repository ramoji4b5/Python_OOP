import sys

print('Python version is', sys.version[:3])

try:

    x=1/0
except NameError as err:  # 'as' is needed here in Python 3.x
    print(err, 'Error Caused')

#########################
"""
expected output is :

Python version is 3.8
name 'Some_inva
lid_code' is not defined Error Caused
"""

"""Raising Exception"""

#raise IOError(“error message”)
