"""To be Used in a Searching Program

for-else:
while-else:
"""

# list of fruits
while True:
    search_fruits = input("enter the fruit name:")
    my_list = ["papaya","banana","pineapple","mango","grapes"]
    # iterating through the fruit list
    #search_fruits ="mango"
    for i in my_list:
       if i == search_fruits:
           print(search_fruits+" found!")
           break
    else:
       print(search_fruits+" not found!")

# list of fruits
my_list = ["papaya","banana","pineapple","mango","grapes"]

size = len(my_list) #length/size of the list
i=0

# iterating through the fruit list
while i<size:
   if my_list[i] == 'mango':
       print("mango found!")
       break
   i+=1
else:
   print("mango not found!")
