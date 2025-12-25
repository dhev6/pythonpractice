my_list = [89,24,86,12,73,25]

n = len(my_list)
for i in range(n-1):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j],my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)

_my_list = [8,4,10,12,11]

n = len(_my_list)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if _my_list[j] > _my_list[j+1]:
            _my_list[j], _my_list[j+1] = _my_list[j+1], _my_list[j]
            swapped = True
    if not swapped:
        break
    
print(_my_list)