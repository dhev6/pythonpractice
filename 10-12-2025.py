# for x in range(1, 6):
#     a = ""
#     for y in range(5-x):
#         a += "* "
#     print(a)

z = 0
for x in range(1, 16):
    a = ''
    for y in range(6-x):
        a += str(x+y)+' '
    print(a)


# for x in range(1, 100):
#     if x%3 == 0 and x%5 == 0:
#         print("clickclock")
#     elif x%3 == 0:
#         print("click")
#     elif x%5 == 0:
#         print("clock")
#     else:
#         print(x)