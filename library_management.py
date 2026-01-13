books = {
    "101": {"title": "It Ends With Us", "author": "Collen Hoover"},
    "102": {"title": "Ugly Love", "author": "Collen Hoover"},   
    "103": {"title": "One Arranged murder", "author": "Chetan Bhagat"}
}

members = {
    "M01": {"name": "Dhev", "borrowed":set()}
}

available_isbns = {"101", "102", "103"}

while True:
    print("\n" + "="*30)
    print(" MINI LIBRARY SYSTEM ")
    print("="*30)
    print("1. View Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Register New Member")
    print("5. Add New Book")
    print("6. Exit")

    choice = input("Selec an option(1-6): ")

    if choice == "1":   
        print("\n-----Available Books-----")
        if not available_isbns:
            print("All books are currently borrowed!")
        else:
            for  isbn in available_isbns:
                print(f"ID: {isbn} | {books[isbn]['title']} by {books[isbn]['author']}")
            
    elif choice == "2":
        m_id = input("Enter Member ID: ")
        isbn = input("Enter Book ISBN: ")   
        
        if m_id in members and isbn in available_isbns:
            available_isbns.remove(isbn)
            members[m_id]["borrowed"].add(isbn)
            print(f"\nSUCCESS: {members[m_id]['name']} borrowed '{books[isbn]['title']}'")
        else:
            print("\nERROR: Invalid ID or Book is unavailable.")

    elif choice == "3":
        m_id = input("Enter Member ID: ")
        isbn = input("Enter Book ISBN: ")   
        if m_id in members and isbn in members[m_id]["borrowed"]:
            members[m_id]["borrowed"].remove(isbn)
            available_isbns.add(isbn)
            print(f"\nSUCCESS: '{books[isbn]['title']}' returned.")
        else:
            print("\nERROR: Return record not found.")

    elif choice == "4":
        new_id = f"M0{len(members) + 1}"
        new_name = input("Enter new member name: ")
        members[new_id] = {"name": new_name, "borrowed": set()}
        print(f"\nSUCCESS: Registered {new_name} with ID: {new_id}")
    
    elif choice == "5": 
        new_isbn = input("Enter new ISBN: ")
        if new_isbn in books:
            print("ERROR: This ISBN already exists in the system.")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            books[new_isbn] = {"title": title, "author": author}
            available_isbns.add(new_isbn)
            print(f"\nSUCCESS: Added '{title}' to the library.")
        
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

