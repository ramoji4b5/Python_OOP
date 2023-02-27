"""Lambda Function in Python"""
#lambda [arguments] : expression

print((lambda x,y : x*y)(5,6))


# Regular function
def sum(num1, num2):
    return (num1 + num2)
# Equivalent lambda function
sum_lambda = lambda num1, num2: num1 + num2
print(sum(5, 4))  # 9
print(sum_lambda(5, 4))  # 9

"""
So why do we use the lambda function instead of the regular function? 
The actual power of the lambda functions can be utilized when they are used with some other in-built functions 
like filter(), map(), or reduce().
"""

"""Use of the Python Lambda Function Inside the filter() Function"""
#Syntax: filter(function, list)
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# one liner code to make list of even numbers using filter() function
even_no = list(filter((lambda x: x % 2 == 0), numbers))
# even numbers list
print(even_no)  # [2, 4, 6, 8]
"""Use of the Python Lambda Function Inside the map() Function"""
#Syntax : map( function, list)
# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# One liner code to create the list of squares of the numbers using map() function
sq_numbers = list(map((lambda x: x * x), numbers))
# Printing the new list
print(sq_numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""Use of the Python Lambda Function Inside reduce() Function"""
#Syntax : reduce( function, list)
# importing reduce() function from functools module
from functools import reduce
# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6]
# One liner code to do the addition of all numbers using reduce() function
sum = reduce((lambda x, y: x + y), numbers)
# Result of addition
print(sum)  # 21

from functools import reduce
numbers = [ 1, 2, 'a', 4, 5, 6]
#sum = reduce((lambda x, y: x + y), numbers)
#print(sum)
numbers = [1,2,3,4,5,6,7,8]
reduced = list(filter((lambda x : x % 6 == 0), numbers))
print(reduced)
