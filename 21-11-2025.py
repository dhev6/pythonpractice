import random

print(random.randrange(1, 1000))
for x in "agriculture":
    print(x)

a = "wakanda, forever!"
print(len(a))
avengers = "ironman, captain america, thor, hulk, black widow, hawkeye"
print("captain america" in avengers)
avengers = "ironman, captain america, thor, hulk, black widow, hawkeye"
if "black 'panther" in avengers:
    print("yes, black panther is an avenger")
avengers = "ironman, captain america, thor, hulk, black widow, hawkeye"
print("superman" not in avengers)

avengers = "ironman, captain america, thor, hulk, black widow, hawkeye"
if "superman" not in avengers:
    print("no, superman is not an avenger")


me = 23
word = f"im dhanush and, I am {me}"
print(word)
country = "india"
continent = f"{country} is in asia"
print(continent)
vikings = "I am \"ragnar lothbrok\" from the tv series \"vikings\""
print(vikings)
# capitalize(hello)
# print(hello.upper())
print("hello.".capitalize())
print("HELLO.".lower())
print("hello. welcome to python programming.".casefold())
vikings = "ragnar lothbrok lagertha floki, bjorn son is ragnar lohbrok"
x = vikings.count("ragnar")
print(x) 
vikings = "I am \"ragnar lothbrok\" from the tv series \"vikings\""
print(vikings)
vikings = "the ragnar lothbrok is friend of floki, bjorn son is ragnar lothbrok"
x = vikings.count("ragnar lothbrok", 0, 30)
print(x)
avengers = "I am ironman"
x = avengers.encode()
print(x)
   
