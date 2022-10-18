print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What is your age"))
    if age > 18:
        print("You will pay $12")
    elif age < 12:
        print("You will pay $5")
    else:
        print("You will pay $7")
else:
    print("You can't ride")
