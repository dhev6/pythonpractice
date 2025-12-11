import math

print("welcome to simple calculator")

def choice():
    number_1 = input("enter first number:")
    number_2 = input("enter second number:")
    choice = input("enter operator (+,-,*,/):")
    if choice == "+":
        choice = int(y) + int(z)
    if choice == "-":
        choice = int(y) - int(z)
    if choice == "*":
        choice = int(y) * int(z)
    if choice == "/":
        choice = int(y) / int(z)

print(f"the result is {choice}")

while True:
    try:
        y = input("enter first number:")
        z = input("enter second number:")
        choice = input("enter operator (+,-,*,/):")
        if choice in ['+','-','*','/']:
            break
        else:
            print("invalid input, please try again")
    except ValueError:
        print("invalid option, please try again")
    print(f"the result is {choice}")