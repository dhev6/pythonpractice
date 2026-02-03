def initialize_file(file_name):
    try:
        with open(file_name, 'x') as file:
            file.write("Date, Category, Amount\n")
        print(f"System: Created a new file named '{file_name}'.")
    except FileExistsError:
        print(f"System: Found existing file '{file_name}'. Loading data...")

def add_expenses(file_name):
    print("----Add Expenses-----\n")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category(e.g: Food, Rent): ")
    amount = input("Enter amount: ")

    with open(file_name, 'a') as file:  
        file.write(f"{date}, {category}, {amount}\n")
    print("Data saved!")

def show_summary(file_name):
    total = 0.0
    try:
        with open(file_name, 'r') as file:
            next(file, None)
            print("\n-----Current expenses------\n")
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    print(f"{parts[1].strip()}: {parts[2].strip()}")
                    total += float(parts[2])
            print(f"Total: ${total:.2f}\n")
    except FileNotFoundError:
        print("No file found yet")

file_name = "Expense.txt"

initialize_file(file_name)

while True:
    print("1. Add Expenses")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        add_expenses(file_name)
    elif choice == "2":
        show_summary(file_name)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")