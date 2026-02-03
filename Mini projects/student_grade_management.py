students = {}   

def add_students():
    sid = input("Enter Students ID: ")
    if sid in students:
        print("ID already exists!")
        return
    name = input("Enter Student Name: ")
    students[sid] = {"name": name, "grades": []}
    print(f"student {name} added.")

def add_grade():
    sid = input("Enter Students ID: ")
    if sid in students:
        try:
            grade = float(input("Enter Grade: "))
            students[sid]["grades"].append(grade)
            print("Grade Added.")
        except ValueError:
            print("Invalid input, please try again!")
    else:
        print("student not found.")

def show_report():
    print(f"\n{'ID':<10} {'Name':<15} {'Average':<10}")
    print("-" * 35)
    for sid, info in students.items():
        name = info["name"]
        grades = info["grades"]

        if len(grades) > 0:
            avg = sum(grades) / len(grades)
        else:
            avg = 0.0
        
        print(f"{sid:<10} {name:<15} {avg:<10.2f}")
    print("-" * 35)

while True:
    print("\n1. Add Student\n2. Add Grade\n3. Show Report\n4. Exit")
    choice = input("Select an option.")

    if choice == "1":
        add_students()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        show_report()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")