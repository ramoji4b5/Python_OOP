def SayHello(name):
    if name :
        print("hello",name)
        print("Welcome "+name+" for python programming")
    else:
        print("enter the name")
        Name = input()
        SayHello(Name)

#SayHello("Ramoji")
#SayHello()

##############
def foo_bar():
    print("Hello!")
    if True:
        print("Bye")
    else:
        print("See you soon")


print("Indentation in Python")
foo_bar()

#To check if your name is a valid identifier or not, you can use the inbuilt function “isidentifier()”.

print("var".isidentifier())
print("@var".isidentifier())

#To view all the keywords your version of python supports, you can open

import keyword
print(keyword.kwlist)

def foo_bar():
    print("Hello!")
    if True:
        print("Bye")
    else:
        print("See you soon")


print("Indentation in Python")


