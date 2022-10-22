print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What is your age"))
    price =0
    if age > 18:
        price =12
        print("You will pay $12")
    elif age < 12:
        price =5
        print("You will pay $5")
    else:
        price =7
        print("You will pay $7")
    photos = (input("Please do you want Photos? "))
    if photos.lower() == "yes":
        price += 3
        print("You will pay $3")
    total= price
    print(f"Your total price is {price}")
else:
    print("You can't ride")
