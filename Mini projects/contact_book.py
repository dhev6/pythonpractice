contacts = {}

def add_contacts():
    number = int(input("Enter phone number: "))
    name = input("Enter name: ")
    contacts[name] = number
    print(f"Contact {name} added successfully!")


def view_contacts():
    if not contacts:
        print("Your contact is empty!")
    else:
        print("\n-----your contact list-----\n")
        for name, number in contacts.items():
            print(f"name: {name} | number: {number}")

while True:
    choice = input("\n1. Add contact\n2. View contacts\n3. Exit\n(choose an option): ")
    if choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        break
    else:
        print("Invalid choice, Please try again.")