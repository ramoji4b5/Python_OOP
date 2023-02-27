my_dict={'Name':'Ravi',"Age":'32'}

#creating an empty dictionary
my_dict={}
#creating a dictionary with integer keys
fruits={'1':'apple','2':'banana','3':'cherry'}
#creating a dictionary with mixed keys
random_dict={'1':'red','Name':'Anushka'}
print(my_dict)
print(fruits)
print(random_dict)

Dict = dict([(1, 'Scaler'), (2, 'Academy')])
print("\nCreate a Dictionary by using  dict(): ")
print(Dict)

my_dict={'Name':'Ravi',"Age":'32','ID':'258RS569'}
print(my_dict['ID']) #accessing using the ID key
print(my_dict['Age']) #accessing using the Age
#print(my_dict['Phone']) #accessing using a key that is not present


#creating an empty dictionary
my_dict={}
print(my_dict)
#adding elements to the dictionary one at a time
my_dict[1]="James"
my_dict[2]="Jim"
my_dict[3]="Jake"
print(my_dict)
#modifying existing entry
my_dict[2]="Apple"
print(my_dict)
#adding multiple values to a single key
my_dict[4]="Banana,Cherry,Kiwi"
print(my_dict)
#adding nested key values
my_dict[5]={'Nested' :{'1' : 'Scaler', '2' : 'Academy'}}
print(my_dict)
#Deleting Dictionary Elements
my_dict={1: 'James', 2: 'Apple', 3: 'Jake', 4: 'Banana,Cherry,Kiwi'}
del my_dict[4]
print(my_dict)

my_dict={1: 'James', 2: 'Apple', 3: 'Jake', 4: 'Banana,Cherry,Kiwi'}
my_dict.clear()
print(my_dict)




