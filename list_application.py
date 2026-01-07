def main():
    todo_list = []

    while True:
        print("/n---TO DO LIST MANAGER---")
        print("1. Add task")
        print("2. View task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("choose an option (1-5): ")

        if choice == "1":
            task_name = input("enter the task: ")
            task = {"task": task_name, "completed": False}
            todo_list.append(task)
            print("Task added!")
        
        elif choice == "2":
            print("\nYOUR TASKS")
            if not todo_list:
                print("List is empty.")
            else:
                for i, item in enumerate(todo_list, start=1):
                    status = "✓" if item ["completed"] else " "
                    print(f"{i}. [{status}] {item['task']}")
    
        
        elif choice == "3":
            for i , item in enumerate(todo_list, start=1):
                print(f"{i}.{item['task']}")

            try:
                task_num = int(input("Enter task number to complete: "))
                todo_list[task_num - 1]["completed"] = True
                print("Task updated")
            except (ValueError, IndexError):    
                print("Invalid task number.") 
                

        elif choice == "4":
            try: 
                task_num = int(input("Enter task number to delete: "))
                removed = todo_list.pop(task_num - 1)
                print(f"Deleted: {removed['task']}")
            except (ValueError, IndexError):    
                print("Invalid task number.") 

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

main()