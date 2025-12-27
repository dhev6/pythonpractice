my_list = [22,8,55,32,2,7,9,23]

n = len(my_list)
for i in range(1,n):
    insert_index = i
    current_value = my_list.pop(i)
    for j in range(i-1,-1,-1):  
        if my_list[j] > current_value:
            insert_index = j
    my_list.insert(insert_index,current_value)

print(my_list)

mylist = [22,8,55,32,2,7,9,23]  

n = len(mylist)
for i in range(1,n):            
    insert_index = i
    current_value = mylist[i]
    for j in range(i-1,-1,-1):
        if mylist[j] > current_value:
            mylist[j+1] = mylist[j]
            insert_index = j
        else:
            break
        
    mylist[insert_index] = current_value
print(mylist)
