# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    print("Leap year")
    if year % 100 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")
        if year % 400 == 0:
            print("not Leap")

        else:
            print("Leap Year")
else:
    print("Not Leap Year")