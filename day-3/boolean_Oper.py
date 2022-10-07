x = 5
y = 10
z = 11
print((x > y) and (y > z))
print((x > y) and (y < z))
print((x < y) and (y > z))
print((x < y) and (y < z))

x = True
y = False
print(not x)
print(not y)

print(1 < 2 < 3)
print(1 < 2 and 2 < 3)

print(1 == 1.0 > 0.75)
print(2 == 2.0 < 1.5)
print(3 < 2 < "2")

grade = 95
print(100 >= grade >= 80)

print(3 < 2 < (1//0))

"""None as a Boolean Value
In Python, None is considered as a Boolean False. 
None can also be used as a default value in the case of Short-circuit chains."""

print(bool(None))

"""
n Python, 0 is considered to be False. Every other number, 
whether positive or negative, is True. Even Inf and Nan are considered to be True.
"""
print(bool(5))
print(bool(0))
print(bool('inf'))
"""In Python, the len() value (Length) of objects is considered while evaluating their truthiness (whether True or False).
 Thus, an empty string, array or set will result in a Boolean False value."""

print(bool(""))
print(bool([]))
print(bool({}))

a=0
print("test" ,a!=0 and 2/a>2)

print('out is :','1'>'2'>0)

