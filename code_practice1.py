# def list_equals(l1, l2):
#     return l1==l2

# print(list_equals([1, 2, 3],[1, 2, 3]))
# print(list_equals([1, 2, 3],[3, 2, 1]))


# # Intersection

# def intersection(l1, l2):
#     return(set(l1) & set(l2))

# print(intersection([1, 3, 4, 5], [3, 5, 6])) 

# # Leap year

# def is_leap(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# print(is_leap(2024))

# age = 20

# if age >= 18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

# num = int(input("Please enter a number: "))


# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
# num1 = float(input("Enter your number: "))

# if num1 > 0:
#     print("Positive numbers")
# elif num1 < 0:
#     print("Negative number")
# else:
#     print("Zero")


# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))

# if a > b:
#     print("Larger number is:", a)
# elif a < b:
#     print("larger number is:", b)
# else:
#     print("Both are equal")

# year = int(input("Enter your year: "))

# if (year % 4 == 0 or year % 100 == 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

    # bubble sort

# my_list = [23, 45, 56, 78, 22, 21, 11]

# n = len(my_list)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_list[j] > my_list[j+1]:
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
# print(my_list)

# _my_list = [23, 45, 56, 78, 22, 21, 11]

# n = len(_my_list)
# for i in range(n-1):
#     swapped = False
#     for j in range(n-i-1):
#         if _my_list[j] > _my_list[j+1]:
#             _my_list[j], _my_list[j+1] = _my_list[j+1], _my_list[j]
#             swapped = True
#     if not swapped:
#         break   

# print(_my_list)

# binary search

