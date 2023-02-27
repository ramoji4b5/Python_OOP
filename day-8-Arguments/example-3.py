class WebSite:
   def __init__(self):
       self.name = "InterviewBit"


website = WebSite()
myStr = "Padded website name with name on center and length 20 is: {:*^20}".format(website.name)
print(myStr)
###################dinamically_setting_length##################################33
myString = "Scaler"
length = 20
myStr = "Dynamically Left Aligned String is: {:<{}}".format(myString, length)
print(myStr)
################################################################################
myString = "Scaler"
length = 20
myStr = "Dynamically Right Aligned String is: {:>{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Center Aligned String is: {:^{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Padded String with input on left is: {:*<{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Padded string with input on right is: {:*>{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Padded string with input on center is: {:*^{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically truncated String with output length 3 is: {:.{}}.".format(myString, 3)
print(myStr)


##############################
myString = "Scaler"
length = 2
myStr = "Dynamically Right Aligned String is: {:>{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically Padded string with input on right is: {:*>{}}.".format(myString, length)
print(myStr)
myStr = "Dynamically truncated String with output length 3 is: {:.{}}.".format(myString, 3)
print(myStr)
