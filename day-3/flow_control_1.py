"""
Let’s understand the flow control in python through another example. Let’s imagine ‘n’ number of students
who have to go to the examination hall to give their paper. But some of them are lazy and for lazy students,
there are some special rules.

Special rules:
No marks deduction if arrived at the examination hall on time.
If 10 mins late, then 10 marks will be deducted.
If 30 mins late, then 30 marks will be deducted.
Zero marks if later than 30 mins.
"""

time = 19

if time == 9:
    print("On time")

if time > 9 and time <= 19:
    print("10 minutes late")

if time > 19 and time <= 39:
    print("30 minutes late")

if time > 39:
    print("Zero marks")
