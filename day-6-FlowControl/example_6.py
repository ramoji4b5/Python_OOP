"""
break, pass, and continue statements are provided in Python to handle instances,
where you need to escape a loop fully when an external condition is triggered or when you want to bypass a section of the loop and begin the next iteration.
These statements can also help you gain better control of your loop.
"""
nums = [7, 2, 3, 1, 5, 4, 6, 8, 9]
count = 0
while count < 7:
  print(nums[count])
  count += 1
  if nums[count] == 4:
    break
print("End")
print("####################################")
nums = [1, 2, 3, 5, 6, 7, 8, 9]
count = 0
while count < 7:
  print(nums[count])
  count += 1
  if nums[count] == 4:
    break
print("End")
