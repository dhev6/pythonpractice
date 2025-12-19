import math

print("\nwelcome to multiplication tables!\n")

# def user_choice(): 
    while True:  
        try:
            num = int(input("Enter the number for the table: "))
            limit = int(input("How high should it go?: "))

            print(f"\n--- Multiplication Table for {num} ---")
            for i in range(1, limit + 1):
            
                print(f"{num} x {i:2} = {num * i:3}")

        except ValueError:
            print("Invalid input! Please enter whole numbers only.")
        


