"""IDENTITY OPERATOR"""

number1 = 5
number2 = 5
number3 = 10
print(number1 is number2)  # check if number1 is equal to number2
print(number1 is not number3)  # check if number1 is not equal to number3

"""MEMBERSHIP """
list1 = [1,2,3,4,5]
print(6 in list1) #in operator
print( 6 not in list1) # not in OPERATOR

"""Bit wise Operators"""
number1 = 4  # 0100 in binary
number2 = 3  # 0011 in binary
print("& operation- ", number1 & number2)  # AND
print("| operation- ", number1 | number2)  # OR
print("^ operation- ", number1 ^ number2)  # XOR
print("~ operation- ", ~number2)  # negation It always returns -(n+1)
print("<< operation- ", number1 << 1)  # shift left by 1 bit
print(">> operation- ", number1 >> 1)  # shift right by 1bit
a=7
b=5
c=4

print(a^b&c) # evaluates left to right preference



