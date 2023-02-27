myNum = -1234
myStr = "Left Aligned Number with length 10 is: {:<10}.".format(myNum)
print(myStr)

myNum = -1234
myStr = "Right Aligned Number with length 10 is: {:>10}".format(myNum)
print(myStr)

myString = "Scaler"
myStr = "Truncated String with length 3 is: {:.3}".format(myString)
print(myStr)

myString = "Scaler"
myStr = "Padded String with string on left and length 20 is: {:*<20}".format(myString)
print(myStr)


myString = "Scaler"
myStr = "Padded String with string on right and length 20 is: {:*>20}".format(myString)
print(myStr)

myString = "Scaler"
myStr = "Padded String with string on center and length 20 is: {:*^20}".format(myString)
print(myStr)

