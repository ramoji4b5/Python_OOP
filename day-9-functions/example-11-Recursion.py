"""A process in which a function calls itself is called recursion."""
#Recursive function in Python has two parts:
#Base Case -
#General (Recursive) Case
def rec_func_name():
   if(True):                     # base case
       pass
       #simple statement without recursion
   else:                                # general case
       pass
       #statement calling rec_func_name()

def sum(n):
    if n <= 1:   # base case
        return n
    else:        # general or recursive case
        ans = sum(n - 1)
    return n + ans
print(sum(6))

"""
All recursive functions have two distinct phases of working - the winding and unwinding phase. 
The winding phase embarks with the recursive function being called the first time and moves ahead until 
the last recursive call. In this phase, no return statements are executed. 
The winding phase terminates when the base case's condition becomes true in a call. 
That's when the unwinding phase begins. In this phase, all recursive functions return in 
the reverse order till the first instance of the function returns.
"""

