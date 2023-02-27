#if-else nested example:
num = int(input("Enter any number: "))

if num >= 0:
  if num == 0:
     print("The number you have entered is Zero")
  else:
     print("The number you have entered is Positive")
else:
  print("The number you have entered is Negative")

print("Outside nested-if")
