my_list = [1, 2, 3, 4, 5]
i = 0
for i in my_list:
    if i == 3:
        print("found")
        break
    i += 1
else:
    print("not found")

my_list = [1, 2, 4, 5]
i = 0
while i < len(my_list):
    if my_list[i] == 3:
        print("found")
        break
    i += 1
else:
    print("not found")