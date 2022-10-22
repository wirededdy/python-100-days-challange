# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_name = name1.lower() + " "+ name2.lower()
print(combine_name)
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
true = t + r + u + e
print(true)
l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")
love = l + o + v + e
print(love)
score = str(true) + str(love)
score_int = int(score)
if score_int < 10 or score_int > 90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")

elif score_int >= 40 and score_int <= 50:
    print(f"Your score is {score_int}, you are alright together.")

else:
    print(f"Your score is {score_int}.")