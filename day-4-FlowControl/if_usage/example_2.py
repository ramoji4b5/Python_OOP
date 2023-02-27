while True:
    num = int(input("enter the number: "))
    if (num < 0):
      print("The number you have entered is Negative")
      print("You are in the if block")
      break
    else:
      print("The number you have entered is Positive")
      print("You are in the else block")

    print("This is outside the if-else statement block but in side while loop")
