l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
for num in l1:
    for ch in l2:
        print(num, ch)
        if num == 2 and ch == 'b' :
            print('BREAK')
            break
            
if 1 + 2 == 3:
  print("Correct math")
  pass
  print("This will also be printed.")
