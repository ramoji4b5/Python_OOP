# Supposing 1, 2, 3, 4, 5 are going to be function parameters
# We want to add these numbers
values = (1, 2, 3, 4, 5)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
#add_numbers(values)

# Supposing 1, 2, 3, 4, 5 are going to be function parameters
# We want to add these numbers
values = (1, 2, 3, 4, 5)

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)
    return total
add_numbers(*values)

details = ('1', 'Aryaman', 'Computer Science')
def func(roll_no, name, branch):
    print(f'Roll number {roll_no} is {name} from {branch} branch of Engineering.')

func(*details)


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# Using **kwargs to pass arguments to this function :
kwargs = {"arg1": "InterviewBit", "arg2": "Blog", "arg3": "Packing and Unpacking"}
myFun(**kwargs)
