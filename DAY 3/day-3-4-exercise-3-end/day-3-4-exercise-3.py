# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
price = 0
if size == "s":
    price += 15
    print("price is $15")
    if add_pepperoni == "y":
        price += 2
        print("price add $2")
elif size == "m":
    price += 20
    print("price is $20")
    if add_pepperoni == "y":
        price += 3
        print("price add $3")
else:
    price += 25
    print("price is $25")
    if add_pepperoni == "y":
        price += 3
        print("price add $3")

if extra_cheese == "y":
    price += 1
    print("price add $1")
Total = price
print(f"Your total cost is {price}")

