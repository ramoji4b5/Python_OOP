"""String Example"""

single_string='Hello'
double_string="Hello World"
triple_string="""Welcome to Scaler"""
print(single_string)
print(double_string)
print(triple_string)
"""Since strings in Python are immutable, we can update the values of strings simply by reassigning these strings with new values."""
message="Welcome to Scaler"
print(message)
message="Hello World" #reassigning a new string
print(message)

"""How to access characters in a python string?
1. Indexing 
Indexing can either be positive or negative. Positive indexing starts from 0 and indexing from the beginning of the string. On the other hand, negative indexing starts from -1, and indexing starts from the end of the string.
2. Slicing
Unlike indexing, slicing returns a range of characters using the slicing syntax.
The syntax looks like this –
'str[start_index: end_index]'
"""

message="Welcome to Scaler"
len_str= len(message)
print(len_str)
print(message[4]) # positive indexing within the range
print(message[-2]) #negative indexing within the range
#print(message[33]) #indexing outside the range


message="Welcome to Scaler"
print(message[2:5]) # positive slicing
print(message[-10:-2]) #negative slicing
print(message[:5]) #slicing from the start
print(message[2:]) #slicing to the end

"""How to delete a string?
We have established that strings are immutable. In simple words, it means that once a string is assigned, we cannot make any changes to it. We cannot remove or delete any character of the string.

What we can do is delete the Python string entirely. We can do so by using the del keyword.
"""

message="Welcome to Scaler"
print(message)
del message
#print(message)

"""String Operators in Python
Arithmetic operators do not work on strings. But, we do have certain operators for performing special operations on strings in Python.
"""

message1="Hello World!"
message2="Welcome to Scaler"
print(message1+message2) # + operator
print(message1*3) # * operator
print(message1[6]) # [] operator
print(message2[0:7]) # [:] operator
str1="Hello"
if str1 in message1:# in operator
    print("It is a present!")
if str1 not in message2:# not in operator
    print("It is not present!")









