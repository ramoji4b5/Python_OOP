"""The break statement"""
# Python program using the break statement
numbers = [5, 9, 7, 13, 8, 1, 11]
for i in numbers:
    # Come out of the loop if an even number is encountered.
    if i%2 == 0:
        print("\nBreaking the Loop. Even Value Encountered.")
        break
    print(i, end=' ')

# Python program having an empty loop
name = 'Interviewbit'
for alphabet in name:
    pass
print(f'The last letter in the name is {alphabet}')

for i in range(5):
    pass
print("last index is:" ,i)

# Python program with the use of continue statement
country = ['India', 'China', 'UAE', 'United Kingdom']
for x in country:
    if x == 'China':
        continue
    print(x)
