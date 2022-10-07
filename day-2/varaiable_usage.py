value=111
print("Value as per the first declaration:", value)
value=222
print("Re-declared value:", value)

"""Assigning a single value to variables in Python"""
num1=num2=num3=1052
print(num1)
print(num2)
print(num3)



"""Multiple assignments"""
whole_number,str,decimal=10,"Hello World",22.50
print(whole_number)
print(str)
print(decimal)

"""Local Variable & Global Variable in Python 
The variables declared inside a function and used only within the scope of that particular function are known as local variables"""
num=30 #global variable
def sum():
    num1=10 #local variable
    num2=25 #local variable
    sum=num1+num2
    print(sum)
sum()
print(num1) #accessing the variable outside the scope

"""deleting variables"""
no_of_chocolates=10
del no_of_chocolates
print(no_of_chocolates)

"""Object References"""
message="Welcome to India"
print(message)
print(type(message))

"""Object Identity"""

# Now that we have understood that variables in Python point to their respective objects let’s try to understand how objects are uniquely identified.
# Python ensures that no two variables will have the same identifier or id. The built-in Python function id() is used to identify the object id or identifier.

message="Welcome to India"
final_message="Goodbye"
print(id(message))
print(id(final_message))

"""Example of Python Keywords"""
# a = 'Scaler academy'
# 'Scaler' in a
# True

"""Python REPL Commands:"""
"""Python comes installed with its interpreter, the interactive Read-Eval-Print Loop (REPL) environment. Here you can obtain the keywords with the following command:"""

"""
help("keywords")

Here is a list of the Python keywords. Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
"""

import keyword
print(keyword.kwlist)

keyword.iskeyword("hi")

"""Types of Keywords in Python

Value Keywords --> True, False , None
Operator Keywords --> AND, OR, NOT, IS(checking identity) , IN
Control Keywords --> if, else, elif
Iteration Keywords --> for, While, break, Continue

"""

# Display numbers 5 to 10

# for loop example
for x in range(5, 11):
    print(x)

#################################

n = 5
# while loop example
while n < 11:
    print(n)
    n += 1

# My Calculator
a = int(input())
b = int(input())
print('enter operation: +, -, *, /')
opt = input()

if opt == '+':
    print(a + b)
elif opt == '-':
    print(a - b)
elif opt == '*':
    print(a * b)
elif opt == '/':
    print(a / b)
else:
    print('invalid input')



