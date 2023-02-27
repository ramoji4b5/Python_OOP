""""Python For loop with else"""

# Program to find whether a value is present or not in a sequence
numbers = [5, 9, 10, 7, 13, 3, 20, 11]
# Search Term
item = 15
for val in numbers:
    if val == item:
        print("Item Found.")
        break
else:
    print("Item Not Found!")
