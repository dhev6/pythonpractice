variable = ["car", "bike", "cycle", "boat"]
print(len(variable))
print(variable[0])
city = list(("chennai", "mumbai", "kolkata", "haryana"))
print(city, len(city), city[-1])
city[3] = "delhi"
print(city)
variable.extend(city)
print(city, variable)
variable.remove("boat")
print(variable)
c = city.pop(2)
print(c)
variable = ["car", "bike", "cycle", "boat"]
for x in variable:
    print(x)
city = list(("chennai", "mumbai", "kolkata", "haryana"))
[print(x) for x in city]
variable = ["car", "bike", "cycle", "boat"]
new_list = [x for x in variable if "b" in x]
print(new_list)
city = list(("chennai", "mumbai", "kolkata", "haryana"))
new_list = [x for x in city if x != "mumbai"]
print(new_list)
city = list(("chennai", "mumbai", "kolkata", "haryana"))
new_list = ["hello" for x in city]
print(new_list)
new_list = [x if x != "haryana" else "kerala" for x in city]
print(new_list)
city = list(("chennai", "mumbai", "kolkata", "haryana"))
city.sort()
print(city)
city = ("chennai", "mumbai", "kolkata", "haryana")
city_1 = list(city)
city_1.append("bangalore")
city = tuple(city_1)
print(city)