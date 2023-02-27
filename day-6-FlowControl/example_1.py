fruits = ["mango", "papaya", "grapes", "banana"]
is_grapes = False
for i in fruits:
   if i == "grapes":
       is_grapes = True
       print("Grapes Found in the fruits list!")
       break

if is_grapes == False:
   print("No Grapes found in the list!")


"""
Python has this unique feature and concept of for-else and while-else. 
There are many languages, like C, C++, and Java which do not support this feature.
"""

########What is For Else and While Else in Python?#########################

""" 
Else block will be executed only if the loop isn't terminated by a break.
if a loop is executed successfully without termination then the else block will be executed.
but the else block will be executed only once.
"""

"""
For-else Syntax in Python
#######################
for i in range(n) :
   #code
else:
   #code

"""
"""While-else Syntax in Python

while condition:
   #code
else:
   #code

"""
""" usage examples:
To be used in a searching program
To check the limits
To handle exceptions

"""