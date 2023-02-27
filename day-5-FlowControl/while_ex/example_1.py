count = 0;
with open("user_list.txt",'a') as file_name:
    while count < 10:
        count += 1
        Name = input("enter the user name:")
        print(str(count) +". "+"Welcome " +Name + ","+"You have registered successfully.",sep="#",end="\n",file=file_name)
