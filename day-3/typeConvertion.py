"""
 In Implicit type conversion,
 Python automatically converts one data type to another data type without any user's need.

 To know the type of data a variable holds, you can use the function type().

 Explicit data type conversion is where you force a Python compiler to convert a data type into another.
 When python itself does data type conversion, it's called Implicit Data Type Conversion.
 """
# implicit
num1 = 2
num2 = 12.2
res = num1 + num2
print("Data type of num1: ", type(num1))
print("Data type of num2: ", type(num2))
print("Data type of res: ", type(res))
print("Value of res: ", res)

"""
Implicit type conversion will occur only if the data types used in the statement are compatible. 
If the data types are incompatible, then a type error will be raised.
"""
""" Adding String and Integer:"""
num1 = 2
num2 = 5
res = num1/num2
print("Data type of num1: ", type(num1))
print("Data type of num2: ", type(num2))
print("Data type of res: ", type(res))
print("Value of res: ", res)

"""What is Explicit Type Conversion in Python ?"""

"""
The conversion of one data type into another, done via user intervention or manually as per the requirement,
is known as explicit type conversion. It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), etc.

Explicit type conversion is also known as Type Casting in Python.
"""

# Functions
#
# int()
# float()
# ord()
# float()
# hex()
# oct()
# tuple()
# set()
# list()
# dict()
# str()

# assigning string to x
str = "0010101"
#string type casted to int base 2
base_two = int(str,2)
#default base value 10
base_ten = int(str)
print("Type casted into base 2 :",base_two)
print("Type casted into default base value 10: ",base_ten)
# str = "02xd"
# conv_num= int(str,16)
# print('octal values is' +conv_num)

# assigning string to x
sample_str = "0010101"
num = 85
#type casting
conv_str = float(sample_str)
conv_num = float(num)
print("String converted into floating-point: ",conv_str)
print("Integer converted into floating-point: ",conv_num)

"""
This ord() function converts characters into their integer ASCII value.
 ASCII stands for American Standard Code For Information Interchange.
 expecting input of type string
"""

alphabet = ord('Y')
number = ord('5')
#number1 = ord(1)
print("Ascii value of character 'Y': ",alphabet)
print("Ascii value of character digit '5': ",number)
#print("Ascii value of character digit 5: ",number1)

"""
Using the hex() function, the user can convert an integer into a hexadecimal string. 
This function only allows integers to be changed into hexadecimal.
"""

# int to hex
num = 45
conv_num = hex(num)
print("Integer type-casted into hexadecimal string is: ",conv_num)

# int to octal
xval = 45
conv_xvaL = oct(xval)
print("Integer type-casted into octal string is: ",conv_xvaL)

#string to tuple
input_string = 'Scaler Academy'
print(tuple(input_string))

#string to set
x = 'success'
print(set(x))
"""using the list() function, we have managed to convert the string “Scaler” 
into a list that contains characters as list elements."""
x = 'Scaler'
print(list(x))

"""
we converted the sets in pairs into a dictionary.
One thing to remember is that the key should be unique in nature; otherwise, 
the existing value will be replaced and overwritten.
"""
x = (('a',3),('f',4),('t',9))
print(dict(x))



a = 121
b = 42.0
print(type(a))
print(type(a))
print("Integer into String: ",str(a))
print("Floating point into String: ",str(b))
type(str(a))
print(type(str(a)))

val1 = '25'
val2 = 45
# (z = val1+val2) it will give type error because both have different data types.
temp =  int(val1) + val2
print("Final result :",temp)

#int to float
a = 45
print(float(a))
# float to int
b = 75.0
print(int(b))
#int to string
c = 125
print(str(c))
# string to int and float
d = '56'
print(int(d))
print(float(d))


