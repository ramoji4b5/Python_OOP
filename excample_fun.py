# fibonacci series generation.
# @author : ramoi
def fib_gen():
  a,b=0,1
  count = 0
  n = input("enter the no of terms ins fibonacci series generation :\n")
  print(type(n))
  while count < int(n):
    #yield a
    print('---', a)
    a,b=b,a+b
    count = count +1
fib_gen()

