import math

print("*" * 40)
print("\nwelcome to prime number checker\n")
print("*" * 40, "\n")

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def get_valid_input():
    while True:
        try:
            user_input = int(input("Enter a positive integer to check: "))
            if user_input < 0:
                print("please enter a positive user_input")
                continue
            return user_input
        except ValueError:
            print(f"Invalid input: {user_input}, please enter a whole number")

num = get_valid_input()

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a composite number")
            