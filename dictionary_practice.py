chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
x = chennai["Pincode"]
print(x)

chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
x = chennai.keys()
print(x)
chennai["India"] = "yes"
print(x)
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
x = chennai.values()
print(x)
chennai["pincode"] = 600028
print(x)
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
x = chennai.items()
print(x)
chennai["code"] = 600028
print(x)
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
if "Landmark" in chennai:
    print("yes 'landmark' is there in chennai")

chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
chennai["Pincode"] = "Chennai",68
print(chennai)

chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
chennai.update({"Area":"Kovalam"})
print(chennai)

chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
chennai.pop("Area")
print(chennai)

chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
chennai.popitem()
print(chennai)