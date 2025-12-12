print("\n")
print("*" * 40)
print("\n   welcome to temperature converter\n")
print("*" * 40)
def celsius_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32   
    print(f"{celsius}°C is equal to {fahrenheit}°F")

# celsius_converter()

def fahrenheit_converter():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")

# fahrenheit_converter()

def choice():
    while True:
        try:
            choice = input("Type C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ").upper()
            if choice in ['C', 'F']:
                break
            else:
                print("invalid choice, please try again")
        except ValueError:
            print("invalid choice, please try again")
    if choice == "C":
        celsius_converter()
    if choice == "F":
        fahrenheit_converter()
    end_message()
# choice()

def end_message():
    user_choice = input("Do you want to convert another temperature? (yes/no): ").lower()
    if user_choice == 'yes':
        choice()
    elif user_choice == 'no':
        print("Thank you for using the temperature converter!")       
    else:
        print("invalid input, please try again!")
        end_message()
      

choice()
# end_message()

