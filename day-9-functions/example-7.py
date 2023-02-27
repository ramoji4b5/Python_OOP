"""**kwargs in Python"""
"""**kwargs allows us to pass any number of keyword arguments.

In Python, these keyword arguments are passed to the program as a Python dictionary.

Python will consider any variable name with two asterisks(**) before it as a keyword argument."""


def makeSentence(**words):
    sentence = ''
    for word in words.values():
        sentence += word
    return sentence
print('Sentence:', makeSentence(a='Kwargs ', b='are ', c='awesome!'))


def whatTechTheyUse(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} uses {}".format(value, key))
    return result
print(whatTechTheyUse(Google='Angular', Facebook='react', Microsoft='.NET'))

"""So if you are using standard arguments along with *args and **kwargs, then you have to follow this order-
1.Standard Arguments
2.*args
3.**kwargs
"""


def printingData(codeName, *args, **kwargs):
    print("I am ", codeName)
    for arg in args:
        print("I am arg: ", arg)
    for keyWord in kwargs.items():
        print("I am kwarg: ", keyWord)

printingData('007', 'agent', firstName='James', lastName='Bond')

"""Packing and Unpacking Using *args and **kwargs in Python"""
"""
Unpacking operators are used to unpack the variables from iterable data types like lists, tuples, and dictionaries.
A single asterisk(*) is used on any iterable given by Python.
The double asterisk(**) is used to iterate over dictionaries."""

carCompany = ['Audi','BMW','Lamborghini']
print(*carCompany)


techStackOne = {"React": "Facebook", "Angular" : "Google", "dotNET" : "Microsoft"}
techStackTwo = {"dotNET" : "Microsoft"}
mergedStack = {**techStackOne, **techStackTwo}
print(mergedStack)

"""Python Example to Understand Types of Function Argument"""
def eligibility_check(name, age):
    if (age>=18):
        print(f'Hey {name}, you are eligible to vote.')
    else:
        print(f'Hey {name}, you are not eligible to vote.')
"""Postional Arguments"""
eligibility_check('Anshika', 21)
"""Keyword Arguments:"""
eligibility_check(age = 21, name = 'Anshika')


# A Python program to demonstrate packing
# All arguments passed to fun2 are packed into tuple *args.
def fun2(*args):
    # Accessing the elements just like we access then from a tuple
    print(args[0])

    # Convert args tuple to a list so we can modify it
    args = list(args)

    # Modifying args
    args[0] = 'Scaler'
    args[1] = 'Academy'
    print(args)


# Driver code
fun2('Python', 'programming', 'preparation')


def add_numbers(*args):
  total = 0
  for num in args:
    total += num
  return total
add_numbers(2,3)
add_numbers(11, 54, 1, 2)


# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    # Printing dictionary items
    print(kwargs)
fun(name="Scaler Academy", ID="001", language="Python")


# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
fun(name="Scaler Academy", ID="001", language="Python")








