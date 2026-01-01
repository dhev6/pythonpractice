Teams = {"Barcelon","Realmadrid","Liverpool","Chelsea"}
print(Teams)
Teams = {"Barcelon","Realmadrid","Liverpool","Chelsea"}
for x in Teams:
    print(x)
Teams = {"Barcelona","Realmadrid","Liverpool","Chelsea"}
print("Barcelona" in Teams)
Teams = {"Barcelona","Realmadrid","Liverpool","Chelsea"}
print("Realmadrid" not in Teams)
Teams = {"Barcelona","Realmadrid","Liverpool","Chelsea"}
Teams2 = ["Arsenal","Dortmund","Bayern","Tottenham"]
Teams.update(Teams2)
print(Teams)
Teams = {"Barcelona","Realmadrid","Liverpool","Chelsea"}
Teams.remove("Chelsea")
print(Teams)
Teams = {"Barcelona","Realmadrid","Liverpool","Chelsea"}
Teams.discard("Chelsea")
print(Teams)
Teams = {"Barcelona","Realmadrid","Liverpool","Chelsea"}
x = Teams.pop()
print(x)
print(Teams)
Teams = {"Barcelona","Realmadrid","Liverpool","Chelsea"}
Teams2 = {"Arsenal","Dortmund","Bayern","Tottenham"}
Teams3 = Teams | Teams2
print(Teams3)
Teams = {"Barcelona","Realmadrid","Liverpool","Chelsea"}
Teams2 = {"Arsenal","Dortmund","Bayern","Tottenham"}
Teams3 = Teams.intersection(Teams2)
print(Teams3)