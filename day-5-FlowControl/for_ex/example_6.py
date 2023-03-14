"""
Looping through a string in Python
In Python, we can loop through a string. The string is an iterable object containing the sequence of characters. Although Strings are immutable, we can perform operations using the characters to get the desired result.

Let's see the above methods in the below code snippet. There are many ways of iterating through the string in python using a for a loop.

Method 1: We can iterate over the string character by character until the string gets exhausted. The for loop in each iteration takes one letter from the string and stores it in the variable character, then prints it.
Method 2: Another way to iterate over the string is using indexing. Since indexing starts at 0, so we can use the range() function which we have seen above. The range() function will take as an argument the stop value, which serves as the end value for the loop.
Method 3: One more way to iterate over the string is the enumerate() method. The enumerate() takes the string as an argument and returns a key-value pair. Key being the index number by default and value of the corresponding letter in the string. Key can also be other numbers as a counter the starting of which can be passed as an argument.
"""

# Python program to iterate over a string using a for loop.
string_var = 'Interviewbit'
# Method 1: Iterating over string
for character in string_var:
    print(character, end=' ')
print('\n')
# Method 2: Iterating using indexing
for i in range(len(string_var)):
    print(string_var[i], end=' ')
print('\n')
# Method 3: Iterating using enumerate()
for k, v in enumerate(string_var):
    print(k,v, end=' ')
