"""Working of Packing and Unpacking simultaneously"""
def __init__(self, *args, **kwargs):
    pass
"""
Let us take an example of a simple Python program to determine a person’s eligibility to vote. 
We will input the user’s name and age to check_eligibility(), where packing takes place. 
Then eligibility to vote is checked for and the args is passed to the print_eligibility() function,
where unpacking takes place and the eligibility message is printed.
"""


def print_eligibility(name, age, eligibility):
    print(f'Hey {name}, you are {eligibility} to vote.')


def check_eligibility(*args):
    # Convert args tuple to a list so we can modify it
    args = list(args)
    if args[1] >= 18:
        elig = 'eligible'
    else:
        elig = 'not eligible'

    args.append(elig)
    print_eligibility(*args)


check_eligibility('Anshika', 15)

def fun(*args):
    total = 0
    for num in args:
        total += num*num
    return total

print(fun(1, 2, 5))

def fun(**args):
    total = 0
    for num in args:
        total += args[num]**2
    return total

print(fun(x=1, y=2, z=5))