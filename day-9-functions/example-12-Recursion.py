def dispn(n):
    if n == 0:
        return  # Base case
    print(n)
    dispn(n - 1)  # Tail Recursive Call

dispn(5)

def dispn(n):
    if n == 0:
        return  # Base case
    dispn(n - 1)  # Not a Tail Recursive Call
    print(n)
dispn(5)

def GCD(a, b):
    if b == 0:
        return a  # Base case
    return GCD(b, a % b)  # Tail Recursive Call
print(GCD(49, 35))

def fact(n):
    if n == 0:
        return 1  # Base case
    return (n * fact(n - 1))  # Not a tail-recursive call
print(fact(5))


def tailr(n):
    if n > 0:
        print(n, end=" ")
        tailr(n - 1)
p = 5
tailr(p)
def headr(n):
    if n > 0:
        headr(n - 1)
        print(n, end=" ")
p = 5
headr(5)


def A(n):
    if n > 0:
        print("", n, end='')
        B(n + 1)


def B(n):
    if n > 1:
        print("", n, end='')
        A(n - 5)
A(20)
print("\n")
print("*********************")
def fib(n):
    if n == 0:
        return 0  # Base Case
    elif n == 1 or n == 2:
        return 1  # Base Case
    return (fib(n - 1) + fib(n - 2))  # Recursive Case

print(fib(8))


res = 0
start = 1


def reverseDigits(num):
    global res
    global start
    if num > 0:
        reverseDigits(int(num / 10))
        res += (num % 10) * start
        start *= 10
    return res


print(reverseDigits(524))


def isAscending(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return True
    return arr[0] <= arr[1] and isAscending(arr[1:])
arr = [1, 4, 2, 3, 5]
print(isAscending(arr))

arr = [1, 2, 3, 4, 5]
print(isAscending(arr))

def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']


def countVowels(str, n):
    if n == 1:
        return isVowel(str[n - 1])

    return countVowels(str, n - 1) + isVowel(str[n - 1])
str = "Hello World!"
print(countVowels(str, len(str)))


def isPalindrome(str):
    if len(str) <= 1:
        return True
    else:
        return str[0] == str[-1] and isPalindrome(str[1:-1])
print(isPalindrome('ABCBA'))
print(isPalindrome('ABCA'))


def strRev(str):
    if len(str) == 0:
        return
    temp = str[0]
    strRev(str[1:])
    print(temp, end='')
print(strRev('Hannah'))










