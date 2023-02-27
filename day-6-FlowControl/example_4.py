# list of numbers
my_list = [1,2,0,5,3]

for denominator in my_list:
   try:
       30/denominator
   except ZeroDivisionError:
       print("zero division error!")
       break
else:
   print("No zero division error found!")
