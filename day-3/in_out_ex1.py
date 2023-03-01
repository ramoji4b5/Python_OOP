import sys
while True:
    value1 = input("enter the institution name")
    value2 = input("enter the course name")
    value3 = input("enter c to exit")
    with open("in_out.txt", "a") as external_file:
        print('Hey! Welcome to {company}. In this article we will learn about {language}'.format(company=value1,
                                                                                                 language=value2),
              file=external_file,end='\n')
        if value3 == "c":
            sys.exit()
        else:
            continue
        external_file.close()