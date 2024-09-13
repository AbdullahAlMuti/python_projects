

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = input("Enter choice(1/2/3/4/5): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter first number: "))

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if x == 0 or y == 0:
        return "Error: Division by zero"
    else:
        return x / y
def modulus(x, y):
    return x % y

if choice == '1':
    result = add(num1, num2)
    print(f"Addition : {num1} + {num2} = {result}")
    
elif choice == '2':
    result = subtract(num1, num2)
    print(f"Subtraction : {num1} - {num2} = {result}")
elif choice == '3':
    result = multiply(num1, num2)
    print(f"Multiplication : {num1} * {num2} = {result}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"Division : {num1} / {num2} = {result}")
elif choice == '5':
    result = modulus(num1, num2)
    print(f"Modulus : {num1} % {num2} = {result}")
else:
    print("Invalid Input")