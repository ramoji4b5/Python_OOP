"""
write a python program to do the convert of a list to array of list
input is ['is','si','ate','eat','heat','hate',.....]
output is [['is','si'],['ate','eat'],['heat','hate']]
"""

input = ['is','si','ate','eat','heat','hate']
# for x in range(len(input)):
#     print('data is {}'.format(input[x]))
list_2 =[]
list_3 = []
list_4 = []
final_list =[]

for x in input:

    print('data is {}'.format(x))
    if len(x)==2:
        print('data is',x)
        if list_2.isnull():
            list_2.append(x)
        else:
            print("insdie else"+x)
        break
    elif len(x)==3:
        list_3.append(x)
    else:
        list_4.append(x)
print(list_2)
print(list_4)
print(list_3)

final_list.append(list_2)
final_list.append(list_3)
final_list.append(list_4)


print(final_list)



