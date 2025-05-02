import random

list_of_compliments = ["oh...congratulations", "wow, look at you", "enjoy it as long as possible"]
list_of_insults = ["HA", "you might be dust soon", "balding yet?"]

name = input("Enter your name: \n")

print("Hello, " + name + "!")

age = input("how old are you? \n")

if int(age) > 30:
    print("wow you're old " + name + "!")
    print(str(random.choice(list_of_insults)))
else:
    print("you're still young ")
    print(str(random.choice(list_of_compliments)))

