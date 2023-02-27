def multiply(num1, num2):
    return num1 * num2

print("product:", multiply(2, 3))


def multiplyThreeNumbers(num1, num2, num3):
    return num1 * num2 * num3
print("product:", multiplyThreeNumbers(1, 2, 3))


def multiplyNumbers(*numbers):
    product = 1
    for n in numbers:
        product *= n
    return product
print("product:", multiplyNumbers(4, 4, 4, 4, 4, 4))

def sumNumbers(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(sumNumbers(1,2,3,4,5,6,7,8,9,10))

