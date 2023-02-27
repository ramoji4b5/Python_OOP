list1=[1,2,3,4,5]
list2=["P","Y","T","H","O","N"]
print(type(list1))
print(type(list2))
good_string = 'python'
print(list(good_string))

good_tuple=('s','c','a','l','e','r')
print(list(good_tuple))

good_set ={'a','b','c'}
print(list(good_set))
good_dict={'a':1,'b':2}
print(good_dict.values())
print(type(good_dict))
print(list(good_dict))

x = [10,20,"Aditya",2.5,"Trivedi",50,60]
y = [10,20,50,"Aditya",2.5,"Trivedi",60]
print(x==y)

Student = ["Aditya", 26389, "CS"]
print("Printing Student details...")
print("Name : %s, ID: %d, Branch: %s"%(Student[0],Student[1],Student[2]))
print("Name: {0},ID: {1},Branch:{2}".format(Student[0],Student[1],Student[2]))

#Nested List
nested_list = ["Hello",[8,0,2,1]]

# Nested indexing
print(nested_list[0][0])
print(nested_list[1][3])

#Negative indexing
demo_list = ['P','y','t','h','o','n']

#accessing last item
print(demo_list[-1])

#accessing third last item
print(demo_list[-3])

#Slicing in list
#list_name(start:stop:step)
# List slicing in Python
demo_list = ['B','U','C','K','K','Y']

# prints elements from index 1 to index 3
print(demo_list[1:4])

# prints elements from index 5 to end
print(demo_list[3:])

# prints elements from beginning to end by taking 2 step each time
print(demo_list[::2])

#correcting the wrong list
prime = [4,6,8,9,10]

# changing the first item
prime[0] = 2

print(prime)

# changing 2nd to last items
prime[1:] = [3,5,7,11]
print(prime)

prime = [2,3,5]

#adding a single element using append() method
prime.append(7)

print(prime)

#adding multiple elements using extend() method
prime.extend([11, 13])

print(prime)

sample = [1,2,3]

#adding new list in above one
print(sample + [4,5,6])

#repeating the list 4 times using *
print(["Hello"]*4)

#list_name.insert(index,element)
sample=[1,3]

#inserting 2 at index 1
sample.insert(1,2)

print(sample)

demo_list = ['M','U','M','B','A','I']

# deleting item at index 2
del demo_list[2]

print(demo_list)

# deleting multiple items from index 1 to 3
del demo_list[1:3]

print(demo_list)

demo_list = ['A','D','I','T','Y','A']
demo_list.remove('A')

# Output: ['D','I','T','Y','A']
print(demo_list)

# Output: 'I'
print(demo_list.pop(1))

# Output: ['D','T','Y','A']
print(demo_list)

# Output: 'A'
print(demo_list.pop()) #pop without index by default deletes the last element

# Output: ['D','T','Y']
print(demo_list)

demo_list.clear() #deletes all the elements from the list

# Output: []
print(demo_list)

#In Python, list comprehension is a simple and clever approach to generate
# new lists from iterables such as tuples, strings, arrays, and lists.

mul_list = [i*2 for i in range(1,6)]
print(mul_list)

mul_list=[]
for i in range(1,6):
    mul_list.append(2*i)
print(mul_list)
# if statements can be included in a list comprehension if desired.
# Items for the new list can be filtered out using an optional if condition.
even_squares = [i**2 for i in range(2,10) if i%2==0]
print(even_squares)

even_squares = []

for i in range(2, 10):
    if i % 2 == 0:
        even_squares.append(i ** 2)

print(even_squares)

#A	Function	Description
#1	max(list)	It returns the list's most large element.
#2	min(list)	It returns the list's most small element.
#3	len(list)	It returns the lenght of the list.
#4	list(seq)	It converts any sequence into list.
#5	sum()	It returns the summation of all the elements in the list.
#6	reduce()	It applies an operation to all of the list elements with the given argument stores the intermediate output and only returns the final summing result.
#7	any()	It returns true if any item of the list is true. if the list is empty, return false
#8	map()	It returns a list of the results after applying the given function to each item of the specified iterable
#9	all()	It returns true if all items is true or if the list is empty
#10	cmp(list1, list2)	It compares the elements of both the lists.

"""List Membership Test
Using the keyword in, we can see if an item is present in a list or not. 
We will get boolean(True/False) value as a result."""

demo_list = ['P', 'y', 't', 'h', 'o', 'n']

print('P' in demo_list)

print('a' in demo_list)

print('c' not in demo_list)


for car in ['Ferrari La Ferrari','MCLaren GT','Lamborghini Veneno']:
    print("I want",car,";)")





