def main():
    i = 5
    print(f"Initial value of i in main: {i}")
    print(f"Initial address of i in main: {id(i)}")
    inc(i)
    print(f"Final value of i in main:{i}")
    print(f"Final address of i in main: {id(i)}")


def inc(n):
    print(f"Initial value of n in inc: {n}")
    print(f"Initial address of n in inc: {id(n)}")
    n = n + 1
    print(f"Final value of n in inc: {n}")
    print(f"Final address of n in inc: {id(n)}")


main()

def inc(n): # Accept an argument, return a value.
   return n+1
x = 4
x = inc(x) #reassign the value
print(x)


def hello(name):
    print ("Hello", name)
hello("Anna")


def hello(name1, name2, name3):
    print("Hello", name1, "\nHi", name2, "\nHola", name3)
hello("Sailee", "Kanchan", "Madhuri")

"""
There are four major types of arguments:

Required arguments
Keyword arguments
Default arguments
Variable-length arguments
"""


def hello(**name):
    print("Hello {0},{1}".format(name['fname'], name['lname']))


hello(fname="Anne", lname="Sullivan")
hello(lname="Pichai", fname="Sundar")
hello(fname="Narendra", mname="Damodar", lname="Modi")
#hello(fname="Bill")  # gives error

"""default arguments"""
def hello (name="Anna"):
   print("Hello", name)
hello()
hello("Rohan")

"""Variable-Length Arguments"""

def hello(*names):
    i=0
    print("Hello")
    for name in names:
        print(name)
hello("Anna", "Ema", "Sarah")




def add1(a,b):
    return a+b
##required arguments
print("example for required argument is {}".format(add1(2,3)))

def add2(a=1,b=2):
    return a+b

print(f"example for default argument is: {add2()}")

def add3(**kargs):
    sum = 0
    for value in kargs.values():
        sum = sum+value
    return sum
ex_dist ={"0":0,"1":1}

print("example for key word argument is:{}".format(add3(**ex_dist)))

def add4(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum
count = [1,2,3,4,5]
print("example for variable length argument is:{}".format(add4(1,2,3,5)))
print(f"example for variable length argument is: {add4(*count)}")





