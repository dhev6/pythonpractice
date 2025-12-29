import math

print("welome to percentage calculator\n")

def user_input():
    student_name = input("please enter your name: ")

    while True:
        try:
            subject_1 = int(input("enter your 1st mark here: "))
            if subject_1 <= 100:
                break
            print("invalid input, please enter a correct number")
        except ValueError:
            print("invalid input, please try again") 

    while True:
        try:      
            subject_2 = int(input("enter your mark 2nd here: "))
            if subject_2 <= 100:
                break
            print("invalid input, please enter a correct number")
        except ValueError:
            print("invalid input, please try again") 

    while True:
        try:
            subject_3 = int(input("enter your 3rd mark here: "))
            if subject_3 <= 100:
                break
            print("invalid input, please enter a correct number")
        except ValueError:
            print("invalid input, please try again") 

    x = []
    x.append(subject_1)
    x.append(subject_2)
    x.append(subject_3)
    total_marks = sum(x)
    print(f"{student_name}'s total mark is", total_marks)
    average = sum(x)/3
    print(f"{student_name}'s average score is", average)
    percentage = (total_marks/300) * 100
    print(f"{student_name}'s percentage is", percentage)
user_input()
    
def end_message():
    user_choice = input("do you want to continue (yes/no): ").lower()
    if user_choice == 'yes':
        user_input()
    elif user_choice == 'no':
        print("thank you for using percentage calculator!")
    else:
        print("invalid input, please try again!")
end_message()

    







