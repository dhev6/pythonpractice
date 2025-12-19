import random

print("welcome to number guessing game\n")
print("I'm thinking of a number between 1 and 100.\n")

target = random.randint(1, 100)
print(f"your clue is {target * 2}\n")


def user_choice():
    attempt = 1
    while True:
        try:
            user_choice = int(input(f"{attempt} attempt: enter your number: "))
            if user_choice < 1 or user_choice > 100:
                print("Please enter a number between 1 and 100.")
                continue
            attempt += 1
            if attempt > 5:
                print("game over!")
                end_message()
                break
            if user_choice < target:
                print(f"\nhigher! \n")
            elif user_choice > target:
                print(f"\nlower! \n")
            else:
                print(f"correct! it took you {attempt} tries")
                break
        
        except ValueError:
            print("invalid input, please enter a whole number")

def end_message():
    user_input = input("do you want to play another game? (yes/no)").lower()
    if user_input == "yes":
        user_choice()
    if user_input == "no":
        print("thank you for using")

user_choice()