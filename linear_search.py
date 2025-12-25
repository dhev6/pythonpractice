def linearSearch(arr, targetValue):
    for i in range(len(arr)):
        if arr[i] == targetValue:
            return i
    return -1

my_list = [2,3,5,7,8,9,13]
x = 8

result = linearSearch(my_list, x)

if result != -1:
    print("Found at index", result)
else:
    print("not Found")