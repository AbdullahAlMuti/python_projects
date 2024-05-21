print("\n")
print(" Welcome to ODD and Even Checker")
while True:
    print("=== === === === === === === === ===")

    num = int(input("Enter your Number to check : "))
    if num % 2 == 0: # if num % 2 > 0: Both are same.
        print("Yes ! This number is an Even Number.")
    else:
        print("Ohh ! This is an ODD Number. ")
