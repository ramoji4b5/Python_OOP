"""
The range() function

range() is a built-in function provided by Python. This function is commonly used with a for loop for looping over a range of numbers. This function returns a sequence of numbers that,
by default, starts with zero, increments by 1, and ends at a specified number passed as an argument.

range(stop): It takes one argument and is the default version of the range() function. It will generate a sequence of numbers starting from 0, incrementing by 1, and ending at the specified number count. For example, range(15) will generate the numbers starting at 0 and ending at 14.
range(start, stop): This will take as an argument the starting and the ending numbers and will generate the sequence incrementing by 1. For example,
range(5, 10) will generate a sequence of numbers starting at 5 and ending at 9, by default incremented by 1.
range(start, increment, stop): This version takes the start value, step value by which the series will increment(positive integer) or decrement(negative integer), and ending values parameters and generates the sequence. For example,
range(6, 2, 21) will generate all the even numbers between 6 and 21. There will be an increment of 2 in successive values as the step size is 2.
"""

#Program to iterate through a list using range()
city = ['London', 'Paris', 'Mumbai', 'Sydney', 'California']
size = len(city)
#iterating over the list using the range() function
for x in range(size):
    print("I Love", city[x])


city = ['London', 'Paris', 'Mumbai', 'Sydney', 'California']
#size = len(city)
#iterating over the list using the range() function
for x in city:
    print("I hate", x)
