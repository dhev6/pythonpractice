my_list = [1,2,4,9,12,3,14,11]

n = len(my_list)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if my_list[j] < my_list[min_index]:
            min_index = j
    min_value = my_list.pop(min_index)
    my_list.insert(i, min_value)

print(my_list)
