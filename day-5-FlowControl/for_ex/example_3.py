# Python program to understand how for loop works internally
country = ['India', 'UAE', 'United Kingdom']
# Creating an iterator object for the list country
iter_object = iter(country)
#infinite while loop
while True:
    try:
        # Fetching the next item
        item = next(iter_object)
        print(item)
    except StopIteration:
        # if StopIteration is raised break the loop
        break
i=0
while i in range(len(country)):
    print("ramoji your wish country is :",country[i])
    i=i+1