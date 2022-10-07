""" Python takes all the input as a string input by default.
To convert it to any other data type, we have to convert the input explicitly."""
#syantax oof print
#print(object(s), sep=' ', end='\n', file=file, flush=False)

"""
print(object(s), sep=' ', end='\n', file=file, flush=False)

object(s) are the values to be printed on the screen. They are converted to strings before getting printed.

sep keyword is used to specify how to separate the objects inside the same print statement. 
By default, we have it as sep=' ', a space between two objects.

end is used to print a particular thing after all the values are printed. 
By default, we have end as \n, which provides a new line after each print() statement.

file is used to specify where to display the output. 
By default, it is sys.stdout (which is the screen).

flush specifies the boolean expression if the output is False or True. 
By default, it is False. In Python, the output from the print() goes into a buffer. Using the flush= True parameter helps in flushing the buffer as soon as we use the print() statement.
"""

print(0, 1, 2)
print(0, 1, 2, sep='$')
print(1, 2, sep='@', end='%')
print('\n', 1,2,end='/')

print("Scaler", end=' ')
print("Academy")
""" both words were printed in the same line because the end by default wasn’t ‘\n’, instead was ' ' (space)."""


students = 5000
print("Scaler has " + str(students) + " employees")

# Here we take two variables and do certain operations with it.
x = 3
y = 12
mul = x * y
print('The value of x is {} and y is {}'.format(x, y))
# Here we are specifying the order of the variables.
print('{2} is the multiplication of {0} and {1}'.format(x, y, mul))
# We can even use keyword arguments to format strings.

with open("in_out.txt", "w") as external_file:
    print('Hey! Welcome to {company}. In this article we will learn about {language}'.format(company='Scaler', language='Python'),file=external_file)
    external_file.close()


print('Hey! Welcome to {company}. In this article we will learn about {language}'.format(company='Scaler', language='Python'),sep='-', end='$')


#
# while True:
#     value1 = input("enter the institution name")
#     value2 = input("enter the course name")
#     print("Hey! Welcome to {company}. In this article we will learn about {language}".format(company=value1, language=value2))

# Here we take input from the user and then display it.
name = input("Enter your first name: ")
print("Hey! " + name)


# Here we will take an integer as input from the user.
age = int(input("Enter your age: "))
new = age + 1
name = input("Enter your name: ")
print("Hey! " + name + " Next year you will be " + str(new))

# Here we will take two numbers as input from the user.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
mul = num1 * num2
print("The multiplication of num1 & num2 is: %.2f" % mul)

