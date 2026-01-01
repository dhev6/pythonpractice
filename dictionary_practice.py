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
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
for x in chennai:
    print(x)
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
for x in chennai:
    print(chennai[x])
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
for x in chennai.values():
    print(x)
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
for x in chennai.keys():
    print(x)
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
for x in chennai.items():
    print(x)
chennai = {
"Area": "Mathur",
"Landmark": "Lake",
"Pincode": 600068,
"TamilNadu": True
}
new_dict = dict(chennai)
print(new_dict)
India = {
    "State1" : {
        "Name" : "Tamilnadu",
        "area" : "mathur"
    },
    "State2" : {
    "name" : "Kerala",
    "area" : "kochi"
    },
    "State3" : {
    "name" : "Karnataka",
    "area" : "Bangalore"
    },
}
print(India)

State1 = {
    "Name" : "Tamilnadu",
    "area" : "mathur"
}
State2 = {
    "name" : "Kerala",
    "area" : "kochi"
}
State3 = {
    "name" : "Karnataka",
    "area" : "Bangalore"
}
India = {
    "state1" : State1,
    "state2" : State2,
    "state3" : State3
}
print(India)
State1 = {
    "Name" : "Tamilnadu",
    "area" : "mathur"
}
State2 = {
    "Name" : "Kerala",
    "area" : "kochi"
}
State3 = {
    "Name" : "Karnataka",
    "area" : "Bangalore"
}
India = {
    "State1" : State1,
    "State2" : State2,
    "State3" : State3
}
print(India["State2"]["Name"])

India = {
    "State1" : {
        "Name" : "Tamilnadu",
        "area" : "mathur"
    },
    "State2" : {
    "name" : "Kerala",
    "area" : "kochi"
    },
    "State3" : {
    "name" : "Karnataka",
    "area" : "Bangalore"
    },
}
for x, obj in India.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y]) 