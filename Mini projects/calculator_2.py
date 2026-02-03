import math

print("\n  welcome to simple calculator\n")

def showmenu():
    print("select operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")      
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Exit")
    print("------------------------------")

def calculator():
    while True:
        showmenu()
        choice = input("Enter your choice (1 - 9): ")
            
        if choice == "9":
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5',]:
            try:
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
            except ValueError:
                print("Invalid input, please enter a number.")
                continue

            if choice == '1':
                print(f"Result: {num1 + num2} ")

            elif choice == '2':
                print(f"Result: {num1 - num2}")

            elif choice == '3':
                print(f"Result: {num1 * num2}")

            elif choice == '4':
                if num2 == 0:
                    print("Error division by zero")
                else:
                    print(f"Result: {num1} / {num2} ")

            elif choice == '5':
                print(f"Result: {math.pow(num1, num2)}")

        elif choice in ["6", "7", "8"]:
            num = float(input("Enter your number here: "))

            if choice == "6":
                print(f"Result: {math.sqrt(num)}")
            
            elif choice == "7":
                base = input("Enter base (Default is e): ")
                if base == "":
                    print(f"Result: {math.log(num)}")   
                else:
                    print(f"Result: {math.log(num, float(base))}")

            elif choice == "8":
                rad = math.radians(num)
                print(f"Result (sine {num}°): {math.sin(rad)}")
            
        
            next_calculation = input("do you want to perform another calculation: ")
            if next_calculation.lower() != 'yes':
                break

        else:
            print("invalid input")

calculator()


