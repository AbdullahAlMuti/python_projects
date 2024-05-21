#This is a Grade Test Program
while True:
    print("\n")
    print(" Welcome to Grade Calculator")
    print("=== === === === === === === ===")
    print('\n')
   
    print("------------------------------------------")
    print("1. Total Grade Calculator   : ")
    print("2. Individual Grade Checker : ")
    choice = int(input("Choose 1 - 2 for correct Calculator  : "))
    if choice == 1:

        bangla  = int(input("Enter your Bangla Suject Mark Here  : "))
        english = int(input("Enter your English Suject Mark Here : "))
        math    = int(input("Enter your Math Suject Mark Here    : "))
        python  = int(input("Enter your Python Suject Mark Here  : "))
        print("-------------------------------------------------------")
        total = bangla + english + math + python
        print("Your Total Mark is                  : " + str(total))
        average = total / 4
        print("Your average mark is                : " + str(average))

        if average >= 80:
            print("Congratulation ! You got A+")
            print("\n")
        elif average >= 70:
            print("Your grade is B+")
            print("\n")
        elif average >= 60:
            print("Your grade is C+")
            print("\n")
        elif average >= 50:
            print("Your grade is D+")
            print("\n")
        elif average <= 49:
            print("Sorry ! Your Failed.")
            print("But Remind F is not a Bad Grade.")
            print("\n")
        else:
            print("Invaild Marks")
            print("\n")
        ano = input("Do you want to check another ?")
        if ano == "Yes":
            continue
        else:
            break
    elif choice == 2:
        indi = int(input("Enter Your Subject Mark : "))
        if indi >= 80:
            print("Congratulation ! You got A+")
            print("\n")
        elif indi >= 70:
            print("Your grade is B+")
            print("\n")
        elif indi >= 60:
            print("Your grade is C+")
            print("\n")
        elif indi >= 50:
            print("Your grade is D+")
            print("\n")
        elif indi <= 49:
            print("Sorry ! Your Failed.")
            print("But Remind F is not a Bad Grade.")
            print("\n")
        else:
            print("Invaild Marks")
            print("\n")
        
        ano = input("Do you want to check another ?Yes/No")
        if ano == "Yes":
            continue
        else:
            break

