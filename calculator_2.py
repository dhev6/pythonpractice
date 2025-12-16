import math

print("\n  welcome to simple calculator\n")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: cannot divide by zero"
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def modulus(n1 , n2):   
    if n2 == 0:
        return "Error: cannot calculate modulus with divisor"
    return n1 % n2

print("select operations:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Power (**)")
print("6. Modulus (%)")

while True:
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if choice == '1':
            print(f"{num1 + num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1 - num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1 * num2} = {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        
        elif choice == '6': 
            result = modulus(num2, num2)
            print(f"{num1} % {num2} = {result}")

        next_calculation = input("do you want to perform another calculation")
        if next_calculation.lower() != 'yes':
            break

    else:
        print("invalid input")


