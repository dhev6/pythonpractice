# import numpy as np

# arr = np.array([1, 2, 3, 4, 5], dtype="i4")

# print(arr)
# print(arr.dtype)

# print(np.__version__)

# print(type(arr))

# arr1 = np.array([[1, 2, 3],[4, 5, 6]])
# print(arr1)
# print(arr1[1, 2])

# print(arr1.ndim)

# arr3 = np.array([1, 2, 3, 4, 5], ndmin=5)

# print(arr3)
# print("number of dimensions: ", arr3.ndim )

# arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr2)
# print(arr2[1, 1, 2])

# arr1 = np.array([[1, 2, 3],[4, 5, 6]], dtype = "S")
# print(arr1)
# print(arr1.dtype)

# arrays = np.array(["Rock", "Paper", "Scissor"])
# print(arrays.dtype)

# arr4 = np.array([1.2, 3.4, 5.7])
# newarr = arr4.astype("i")

# print(newarr)
# print(newarr.dtype)

# arr5 = np.array([1, 2, 3, 4, 5])

# newarr1 = arr5.astype(bool)

# print(newarr1)
# print(newarr1.dtype)

# arr_n = np.array([1, 2, 3, 4, 5])
# x = arr_n.copy()
# arr_n[0] = 42

# print(arr_n)
# print(x)

# arr_new = np.array([1, 2, 3, 4, 5])
# y = arr_new.view()
# arr_new[0] = 42

# print(arr_new)
# print(y)


# arr_new1 = np.array([1, 2, 3, 4, 5])

# x = arr_new1.copy()
# y = arr_new1.view()

# print(x.base)
# print(y.base)

# arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr6.shape)

# array2 = np.array([1, 2, 3, 4, 5, 6], ndmin=5)
# print(array2)
# print(array2.shape)


# array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# newarr2 = array4.reshape(3, 3)
# print(newarr2)

# array5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# newarr4 = (array5.reshape(2, 5).base)
# print(newarr4)

# new = np.array([1, 2, 3, 4, 5, 6, 7, 8, ])
# narr1 = new.reshape(2, 2, -1)
# print(narr1)

# arr7 = np.array([[1, 2, 3],[4, 5, 6]])
# narr2 = arr7.reshape(-1)
# print(narr2)

# arr10 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in np.nditer(arr10, flags=["buffered"], op_dtypes=["S"]):
#     print(x)

# arr11 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in np.nditer(arr11[:2, ::3]):
#     print(x)


# new2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, ])

# for dhev, x in np.ndenumerate(new2):
#     print(dhev, x)

# # join

# arr22 = np.array([1, 2, 3, 4])

# arr23 = np.array([5, 6, 7, 8])

# ARR = np.concatenate((arr22, arr23))

# print(ARR)


# arr31 = np.array([[1, 2, 3],[4, 5, 6]])

# arr44 = np.array([[1, 2, 3],[4, 5, 6]])

# dhev = np.stack((arr31, arr44), axis=1)
# print(dhev)

# arr31 = np.array([[1, 2, 3],[4, 5, 6]])

# arr44 = np.array([[1, 2, 3],[4, 5, 6]])

# dhev = np.hstack((arr31, arr44))
# print(dhev)

# arr31 = np.array([[1, 2, 3],[4, 5, 6]])

# arr44 = np.array([[1, 2, 3],[4, 5, 6]])

# dhev = np.vstack((arr31, arr44))
# print(dhev)

# arr31 = np.array([[1, 2, 3],[4, 5, 6]])

# arr44 = np.array([[1, 2, 3],[4, 5, 6]])

# dhev = np.dstack((arr31, arr44))
# print(dhev)

# # Split

# array5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# nwarr = np.array_split(array5, 2)
# print(nwarr[0])
# print(nwarr[1]) 

# array5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# nwarr = np.array_split(array5, 3)
# print(nwarr)

# # Search

# array5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# x = np.where(array5 == 4)

# print(x)

# # Sort

# array44 = np.array([4, 5, 6, 7, 8])

# r = np.searchsorted(array44, 4, side='right')

# print(r)

# array45 = np. array([9, 2, 5, 6, 3])

# print(np.sort(array45))

# # Filter

# narray = np.array([23, 45, 54, 44, 22])

# x = [True, False, True, False, True]

# newarrat = narray[x]

# print(newarrat)

# narray = np.array([23, 39, 54, 44, 22])

# new_filter = []

# for x in narray:
#     if x > 39:
#         new_filter.append(True)
#     else:
#         new_filter.append(False)

# newarr43 = narray[new_filter]

# print(new_filter)
# print(newarr43)

# narray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# new_filter = []

# for x in narray:
#     if x % 2 == 0:
#         new_filter.append(True)
#     else:
#         new_filter.append(False)

# newarr43 = narray[new_filter]

# print(new_filter)
# print(newarr43)

# _array = np.array([23, 39, 54, 44, 22])

# filterarray = _array > 39

# new_arf = _array[filterarray]

# print(filterarray)
# print(new_arf)


# _array = np.array([23, 39, 54, 44, 22])

# filterarray = _array % 2 == 0

# new_arf = _array[filterarray]

# print(filterarray)
# print(new_arf)


# # FILE HANDLING

# # f = open("file_handling.txt")
# # print(f.readline())
# # f.close()

# # with open("file_handling.txt", "a") as dhev:
# #     dhev.write("Please check your connection")

# # with open("file_handling.txt") as dhev:
# #     print(dhev.read())

#     # with open("file_handling.txt", "w") as dhev:
#     #     dhev.write("Please check your connection")

#     # with open("file_handling.txt") as dhev:
#     #     print(dhev.read())

# import os

# # f = "new_filehandling.txt"

# # if os.path.exists("new_filehandling.txt"):
# #     try:    
# #         with open("new_filehandling.txt") as file:
# #             print(file.read())
# #     except FileExistsError:
# #         print(f"Error: The file '{f}' doesnt exits")
# # else:
# #     f = open("new_filehandling.txt", "x")
# #     print('File Create successfully, you can use it now.')


# # with open("new_filehandling.txt", 'a') as file:
# #     file.write("Welcome to numpy program")

# # Second method

# filename = "2_file.txt"

# if not os.path.exists(filename):
#     with open(filename, 'x') as f:
#         f.write("Welcome to numpy!\n")  
#     print("File successfully created, You can use it now.")
# else:
#     with open(filename, 'a') as file:
#         file.write("Welcome to numpy!\n")
#     with open(filename, 'r') as file:
#         print(file.read())
    
# # Remove file.

# if os.path.exists("file_handling.txt"):
#     os.remove("file_handling.txt")
# else:
#     print("The file doesn't exits!")


# # JSON 

# import json


# x = '{"Name":"Dhev","Age": 23,"Place":"Chennai"}'

# y = json.loads(x)

# print(y["Age"])

# x = {"Name":"Dhev",
#      "Age": 23,
#      "Place":"Chennai"
# }

# y = json.dumps(x)

# print(y)


# import json

# x = {
#   "name": "Dhev",
#   "age": 23,
#   "married": False,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [ 
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # use four indents to make it easier to read the result:
# print(json.dumps(x, indent=4,sort_keys=True, separators=(". ", " = ")))


import csv

header = ['Name', 'Score']
data = [['Dhev', 99], ['Bob', 85], ['Miles', 79]]

with open('grades.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

with open('grades.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Score']) > 80:
            print(f"{row['Name']} passed with honors")



    