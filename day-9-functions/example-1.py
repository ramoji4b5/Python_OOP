"""Function"""
"""User-defined:"""
def fun():
   print("Just a function having fun")
fun()
"""Built-in"""
x = abs(-7.25)
print(x)


def square(x):
    """The function returns the square of the input number"""
    print("The square of " + str(x) + " is to be found.")
    return x * x


print("The square is: " + str(square(10)))

"""In the pass-by-value, a copy of the parameter’s value is stored in the memory, 
and all changes are done to that. Hence, these changes aren’t reflected in the parameter 
in the function call. However, in pass-by reference, a copy of the address of the actual 
parameter is stored; thus, changes inside the Function will be reflected back in the program."""
"""Pass by Value"""
# Python code to demonstrate call by value
string = "Good Evening."
def greet(string):
    string = "Good Morning"
    print("Inside Function:", string)
greet(string)
print("Outside Function:", string)

# Python code to demonstrate call by reference
multiples_of_5 = [5, 10, 15, 20, 25, 30]
def append_to_list(list1):
    list1.append(35)
    print("Inside Function-ref: ", list1)

append_to_list(multiples_of_5)
print("Outside Function-ref: ", multiples_of_5)

# Python code to demonstrate call by value
multiples_of_5 = [5, 10, 15, 20, 25, 30]
print("Outside Function-value: ", multiples_of_5)
def append_to_list(multiples_of_5):
    multiples_of_5.append(35)
    print("Inside Function-Value: ", multiples_of_5)
append_to_list(multiples_of_5)
