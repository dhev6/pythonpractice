import numpy as np

arr = np.array([1, 2, 3, 4, 5], dtype="i4")

print(arr)
print(arr.dtype)

print(np.__version__)

print(type(arr))

arr1 = np.array([[1, 2, 3],[4, 5, 6]])
print(arr1)
print(arr1[1, 2])

print(arr1.ndim)

arr3 = np.array([1, 2, 3, 4, 5], ndmin=5)

print(arr3)
print("number of dimensions: ", arr3.ndim )

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr2)
print(arr2[1, 1, 2])

arr1 = np.array([[1, 2, 3],[4, 5, 6]], dtype = "S")
print(arr1)
print(arr1.dtype)

arrays = np.array(["Rock", "Paper", "Scissor"])
print(arrays.dtype)

arr4 = np.array([1.2, 3.4, 5.7])
newarr = arr4.astype("i")

print(newarr)
print(newarr.dtype)

arr5 = np.array([1, 2, 3, 4, 5])

newarr1 = arr5.astype(bool)

print(newarr1)
print(newarr1.dtype)

arr_n = np.array([1, 2, 3, 4, 5])
x = arr_n.copy()
arr_n[0] = 42

print(arr_n)
print(x)

arr_new = np.array([1, 2, 3, 4, 5])
y = arr_new.view()
arr_new[0] = 42

print(arr_new)
print(y)


arr_new1 = np.array([1, 2, 3, 4, 5])

x = arr_new1.copy()
y = arr_new1.view()

print(x.base)
print(y.base)

arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr6.shape)

array2 = np.array([1, 2, 3, 4, 5, 6], ndmin=5)
print(array2)
print(array2.shape)


array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newarr2 = array4.reshape(3, 3)
print(newarr2)

array5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newarr4 = (array5.reshape(2, 5).base)
print(newarr4)

new = np.array([1, 2, 3, 4, 5, 6, 7, 8, ])
narr1 = new.reshape(2, 2, -1)
print(narr1)

arr7 = np.array([[1, 2, 3],[4, 5, 6]])
narr2 = arr7.reshape(-1)
print(narr2)

arr10 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in np.nditer(arr10, flags=["buffered"], op_dtypes=["S"]):
    print(x)

arr11 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in np.nditer(arr11[:2, ::3]):
    print(x)


new2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, ])

for dhev, x in np.ndenumerate(new2):
    print(dhev, x)

arr22 = np.array([1, 2, 3, 4])

arr23 = np.array([5, 6, 7, 8])

ARR = np.concatenate((arr22, arr23))

print(ARR)


arr31 = np.array([[1, 2, 3],[4, 5, 6]])

arr44 = np.array([[1, 2, 3],[4, 5, 6]])

dhev = np.stack((arr31, arr44), axis=1)
print(dhev)

arr31 = np.array([[1, 2, 3],[4, 5, 6]])

arr44 = np.array([[1, 2, 3],[4, 5, 6]])

dhev = np.hstack((arr31, arr44))
print(dhev)

arr31 = np.array([[1, 2, 3],[4, 5, 6]])

arr44 = np.array([[1, 2, 3],[4, 5, 6]])

dhev = np.vstack((arr31, arr44))
print(dhev)

arr31 = np.array([[1, 2, 3],[4, 5, 6]])

arr44 = np.array([[1, 2, 3],[4, 5, 6]])

dhev = np.dstack((arr31, arr44))
print(dhev)