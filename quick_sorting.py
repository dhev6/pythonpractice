
print("Quick Sort Algorithm")
print("*"*20)

def quick_sort(arr):
    if len(arr)==0:
        return arr

    pivot = arr[-1]

    left = []
    middle = []
    right = []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element == pivot:
            middle.append(element)
        else:
            right.append(element)

    return quick_sort(left) + middle + quick_sort(right)


newArr = [25, 34, 12, 0, 1, 7, 3, 6, 5]
print("\n Result")
print("*"*8)
print("Original Array", newArr) 
print("Converted Array", quick_sort(newArr), "\n")


# pivot = 5
# left, middle, right = []
# [25, 34, 12, 0, 1, 7, 3, 6, 5]  => 
# 25 -> right [25] 
# 34 -> right [25, 34 ]
# 12 -> right [25, 34, 12 ]
# 0  -> left [0] 
# 1 -> left [0, 1] 
# 7 -> right [25, 34, 12, 7]
# 3 -> left[0, 1, 3]
# 6 -> right [25, 34, 12, 7, 6 ]
# 5 -> middle [5]

# left [0, 1, 3,] => pivot -3 
# middle [5]
# right [25, 34, 12, 7, 6]