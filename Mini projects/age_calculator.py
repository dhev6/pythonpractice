from datetime import date

print("--- Simple Age Calculator ---")

def simple_age_calculator():
    while True:
        try:
            year = int(input("Enter Year of Birth : "))
            month = int(input("Enter Month of Birth: "))
            day = int(input("Enter Day of Birth: "))
            birth_date = date(year, month, day)
            today = date.today()
            if birth_date > today:
                print("Error: Birth date cannot be in the future.")
            age = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            print(f"You are currently {age} years old.")
        except ValueError:
            print("\nInvalid input. Please enter numbers for the year, month, and day.")
        
simple_age_calculator()
