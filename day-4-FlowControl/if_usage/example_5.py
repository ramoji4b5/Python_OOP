#Short Hand If Statement
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if y == x: print("Both the numbers are equal")

# short-hand if-else statement’
# statement_True if condition else statement_False
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

print("x greater than y") if x>y else print("y greater than x")
x if x>y else y