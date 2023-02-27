"""Syntax of for loop in Python"""
"""
for val in sequence:
    loop body
"""
# Python program to count the number of even integers in the list.

# List of integers
integers = [8, 3, 7, 4, 6, 21, 9]
# variable to store the count
count = 0
# iterate over the list
for val in integers:
    if val % 2 == 0:
        count += 1
print("The count of even numbers is", count)
