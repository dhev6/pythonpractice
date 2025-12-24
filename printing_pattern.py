 '''
 odd or even   
 num = 4 
 if num % 2 == 0:   
     print("Even")
 else:
     print("Odd
 items = [1, 2, 2, 3, 4, 4]
 unique_items = list(set(items))
 print(unique_items
 word = "madam"
 if word == word[::-1]:
     print("Palindrome")
 else:
     print("Not a palindrome)
'''


rows = int(input("please enter the number:"))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


rows = int(input("please enter the number: "))
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


rows = int(input("enter you number: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")   
    print()


rows = int(input("enter the row size for the pattern: "))
for i in range(rows, 0, -1):
    for j in range(rows - i):   
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()

