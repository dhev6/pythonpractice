greeting = "hello, welcome to python programming."
x = greeting.endswith ("programming.")
print(x)
movies = "a\tv\te\tn\tg\te\tr\ts"
x = movies.expandtabs(20)
print(x)
txt = "there can be a big disaster without the help of small people."
x = txt.find("disaster")
print(x)    
txt = "only {price:.2f} dollars"
print(txt.format(price = 56))
txt = "my name is {} and I am {} years old".format("ragnar", 30)
print(txt)
avengers = "sun is {:,} kilometers away from the earth"
print(avengers.format(290073639270))  


def get_choices():
    player_choice = "rock"
    computer_choice = "paper"

    return computer_choice

choices = get_choices()
print(choices)

dict = {"name": "dhanush", "country": "choices"}
