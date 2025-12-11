git add .
git commit -m "adding validation in calculator"
git push origin main

import math

print("welcome to simple calculator")

def choice():
    while True:
        try:
            number_1 = int(input("choose a first number between 1 to 8:"))
            number_2 = int(input("choose a second number between 1 to 8:"))
            choice = input("enter operator (+,-,*,/):")
            if number_1 in range(1,8) or number_2 in range(1,8) or choice in ['+','-','*','/']:   
                break
            else:
                print("invalid number, please try again")
        except ValueError:
            print("invalid number, please try again")
   
    if choice == "+": 
        choice = int(number_1) + int(number_2)
    if choice == "-":
        choice = int(number_1) - int(number_2)
    if choice == "*":
        choice = int(number_1) * int(number_2)
    if choice == "/":
        choice = int(number_1) / int(number_2)

    print(f"the result is {choice}")

choice()