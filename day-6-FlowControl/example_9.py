import os
def ensure_nonexistence(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

"""
 If…Elif Chains
Say in an interview, you’re asked a basic FizzBuzz question, except with a little twist. 
If the input number is divisible by 3, print Fizz. 
If divisible by 5, print Buzz. If divisible by 15, print nothing, and if divisible by 20, print Twist.
"""

for num in range(100):
  if num % 20 == 0:
    print("Twist")
  elif num % 15 == 0:
    pass
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0:
    print("Fizz")
  else:
    print(num)
