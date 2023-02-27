"""To Check The Limits"""

# random list of numbers
my_list1 = [14, 10, 12, 17]
# defining limit from 10 to 20
lower_bound = 10
upper_bound = 20
for i in my_list1:
    if i < lower_bound or i > upper_bound:
        print("all elements are not in the limit!")
        break
else:
    print("all the elements in the list are in the limit")

