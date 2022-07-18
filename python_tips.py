# Iterate using ensumarate insted of range(len())
from sqlalchemy import true

data  = [1,2,-4,-3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0
print(data)
data = [1,2,-3,-4]

for idx,num in enumerate(data):
    if num < 0:
        data[idx] = 0
print(data)

########################
#list comprehension  instead of raw for loops
squares = []
for i in range(10):
    squares.append(i*i)
print(squares)

square = [k*k for k in range(10)]
print('new squares', square)

# sort complex iterable with sorted
data = [1,5,2,3,8]
sorted_data = sorted(data, reverse=True)
print(sorted_data)

data =[{"name": "Ram", "age" :31},
       {"name": "laksh", "age" :29},
       {"name": "swami","age" : 32},
       {"name": "Anu", "age":27},
       { "name": "roji", "age":28}
       ]

list_dist_sort = sorted(data, key=lambda x:x["age"])
print(list_dist_sort)

