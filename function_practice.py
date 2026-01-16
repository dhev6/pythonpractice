def my_function(name, place):
    print(name, "live's in", place)

my_function(name = "Dhev", place = "Chennai")

def My_function(bikes):
    for bike in bikes:
        print(bike)

my_bikes = ["Yamaha", "Suzuki", "Bajaj", "Honda"]
My_function(my_bikes)

def your_function(*numbers):
    if len(numbers) == 0:
        return none
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(your_function(3, 7, 2, 99, 1))

def function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print( key + ":", value)
function("Dhev", age = 23, city = "Chennai", Hobby = "Coding")


def d_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguements:", args)
    print("Keyword arguements:", kwargs)

d_function("Userinfo", "Dhev", "Dhanush", age = 23, city = "chennai")

def dd_function(a, b, c):
    return a *  b + c

numbers = [22, 66, 3]
result = dd_function(*numbers)
print(result)

def fd_function(fname, lname):
    print("hello", fname, lname)

person = {"fname":"Dhev", "lname":"dhanush"}
fd_function(**person)