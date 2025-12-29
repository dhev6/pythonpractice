import math

print("welome to percentage calculator\n")

def user_input():
    while True:
        try:
            student_name = input("please enter your name: ")
            subject_1 = int(input("enter your mark here: "))
            subject_2 = int(input("enter your mark here: "))
            subject_3 = int(input("enter your mark here: "))
            x = []
            x.append(subject_1)
            x.append(subject_2)
            x.append(subject_3)
            if subject_1 > 100  or subject_2 > 100 or subject_3 > 100:
                print("invalid input, please enter a correct number")
                continue
            total_marks = sum(x)
            print(f"{student_name}'s total mark is", total_marks)
            average = sum(x)/3
            print(f"{student_name}'s average score is", average)
            percentage = (total_marks/300) * 100
            print(f"{student_name}'s percentage is", percentage)
            break
        except ValueError:
            print("invalid integer, please try again")

            
    
user_input()






