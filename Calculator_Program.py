def addition(num_1, num_2):
    return num_1 + num_2
def subtraction(num_1, num_2):
    return num_1 - num_2
def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    return num_1 / num_2

def modulu(num_1, num_2):
    return num_1 % num_2

def even_odd(num_1):
    return "even" if num_1 % 2 == 0 else "odd"

def calculator():
    print("Welcome to NINO Calculator")
    print("----------------------------")

    while True:
        print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modul\n6. Even & Odd Check\n7. Exit")
        choose = int(input("Choose an option between 1 - 7: "))
        if choose in [1, 2, 3, 4, 5]:
            num_1 = int(input("Enter First Number      : "))
            num_2 = int(input("Enter Second Number     : "))

            if choose == 1:
                result = addition(num_1, num_2)
                operation = "Addition"
                symbol = "+"
            elif choose == 2:
                result = subtraction(num_1, num_2)
                operation = "Subtraction"
                symbol = "-"
            elif choose == 3:
                result = multiplication(num_1, num_2)
                operation = "Multiplication"
                symbol = "*"
            elif choose == 4:
                result = division(num_1, num_2)
                operation = "Division"
                symbol = "/"
            elif choose == 5:
                result = modulu(num_1, num_2)
                operation = " modulas"
                symbol = "%"
            if result is not None:
                print(f"The {operation} is : {num_1} {symbol} {num_2} = {result}")
            elif choose == 6:
                num_1 = int(input("Enter a Number to check Even or Odd : "))
                result = even_odd(num_1)
                print(f"{num_1} is a : {result} number.")
                another = input("DO you want to check another? YES / NO : ")
                if another == "YES":
                    continue
                else:
                    print("Program Closed!!!")
                    break

            elif choose == 7:
                print("Thank You ! Program is Close.")
            break
        else:
                print("Your input is Invalid")
                another = input("DO you want to check another? YES / NO : ")
                if another == "YES":
                    continue
                else:
                    print("Program Closed!!!")
                    break
calculator()








