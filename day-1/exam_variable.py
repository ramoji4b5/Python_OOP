"""What are variables? To store any data values, we use containers called variables. There is no specific command in python to declare a variable. A variable is created the moment a value is assigned to it."""

y = 9
x = "Foo"
print(x)
print(y)
"""Using the continuation character backslash, you can explicitly divide a statement into multiple lines (“\”)."""
message = "This is a long statement that I want to write, but the " \
          "problem is that it doesn't fit in one single line. So this is how \n" \
          "I've written it for readability."
print(message)
"""Blank Lines in Python"""
print("Line # 1")
print()
print("Line # 3")
###########################
print("Using single or double quotation marks")
print('')
print("")
print("Works!")
"The third way is to use a newline character (\n) at the end of the statement:"
print("Using newline\nto create a new line!")

##############Waiting for User
"""Taking input in the Python programming language is done by the input() function. The program with input() function will not run till 
the program is not provided input by the user through the console."""

print("Enter name")
name = input()

