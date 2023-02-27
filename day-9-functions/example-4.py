def print_details(name="Elon Musk", age=50):
    print(f"{name} is {age} years old.")


print_details("Jeff Bezos", 57)  # Output: Jeff Bezos is 57 years old.
print_details()  # Line 4- Output: Elon Musk is 50 years old.
"""The default arguments are specified at the end, 
meaning any arguments specified to the right of a default argument must also be a default one."""


def divide_two(a, b):
    res = a / b
    return res


res = divide_two(12, 3)
print(res)  # Output: 4

# both keyword arguments
res = divide_two(a=3, b=12)
print(res)  # Output: 0.25

# one positional, one keyword argument
res2 = divide_two(36, b=12)
print(res2)  # Output: 3

# both keyword arguments, order changed
res3 = divide_two(b=12, a=48)
print(res3)  # Output: 4

#Python Arbitrary Arguments
def print_animals(*animals):
    for animal in animals:
        print(animal)

print_animals("Lion", "Elephant", "Wolf", "Gorilla")


def print_food(**foods):
    for food in foods.items():
        print(food)
print_food(Lion="Carnivore", Elephant="Herbivore", Gorilla="Omnivore")


def print_animal_details(*animals, **foods):
    for animal in animals:
        print(animal)
    for food in foods.items():
        print(food)

print_animal_details("Lion", "Elephant", "Wolf", "Gorilla",
                     Lion="Carnivore", Elephant="Herbivore", Gorilla="Omnivore")


def add_nums(num1, num2=12):
    print(num1 + num2)


add_nums(num1=11, num2=13)  # Output: 24

# no value for default argument
add_nums(num1=11)  # Output: 23

# no value for required argument
#add_nums(num2=13)  # Will throw an error
