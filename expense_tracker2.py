import os

def initialize_csv(file_name):
    try:    
        with open(file_name, 'x') as file:
            file.write("Date, Category, Amount\n")
        print(f"System: Created a new CSV Database: {file_name}")
    except FileExistsError:
        print(f"System: CSV database '{file_name}' found, Ready for use")

def add_to_csv(file_name):
    print("\n-----New Expense Entry----\n")
    date = input("Enter Date(eg: YYYY-MM-DD): ")
    category =input("Enter category(eg: Food, Rent): ")
    amount = input("Enter Amount: ")
    with open(file_name, 'a') as file:
        file.write(f"{date}, {category}, {amount}\n")
    print("Expense recorded successfully!")

def remove_edit(file_name):
    

def generate_csv_report(file_name):
    total = 0.0
    try:
        with open(file_name, 'r') as file:
            next(file)
            
            print(f"\n{'DATE':<12} | {'CATEGORY':<15} | {'AMOUNT':<10}")
            print("-" * 45)

            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3: 
                    d, cat, amt = parts
                    total += float(amt)
                    print(f"{d:<12} | {cat:<15} | ${float(amt):>8.2f}")
            
            print("-" * 45)
            print(f"{'TOTAL':<29} | ${total:>8.2f}\n")
                    
    except FileNotFoundError:
        print("Error: Database file missing.")
    except ValueError:
        print("Error: Found invalid data in amount column")

csv_file = "Expense_2026.csv"

initialize_csv(csv_file)

while True:
    print("1. Add Expense")
    print("2. Generate Report")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        add_to_csv(csv_file)
    elif choice == "2":
        generate_csv_report(csv_file)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")