def check_odd_even():

    print("\n---EVEN/ODD CHECKER---\n")

    while True:
        try:
            number = int(input("enter a integer: "))
            break
        except ValueError:
            print("Invalid input, please enter a whole number(integer).")
    if number % 2 == 0: 
        print(f"Result: the number {number} is even")
    else:
        print(f"Result: the number {number} is odd")

check_odd_even()