# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

len_names = len(names)-1

who = random.randint(0, len_names)
pay = names[who]
print(f"{pay} is going to buy the meal today!")