def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left+right) // 2
    
        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

my_list = [2,3,5,6,8,9,12,15,16,17]
x = 6

result = binarySearch(my_list, x)

if result != -1:
    print("found at index", result)
else:
    print("not found")