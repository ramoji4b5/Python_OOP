"""While Loop Control Statements in Python"""
##Continue Statement:
count = 0
while count < 10:
     count += 1;
     if(count == 5): continue
     print("The value of the count is " + str(count))
####Break Statement:
count = 0
while count < 10:
      count += 1;
      if(count == 5): break
      print("The value of the count is " + str(count))
##Pass Statement:
count = 0
while count < 10:
 count += 1;
 if(count == 5): pass
 print("The value of the count is " + str(count))
