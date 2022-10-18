# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_calc = weight/(height**2)

bmi = round(bmi_calc,0)

# print(bmi)

if bmi < 18.5:
    print(f"Yor bmi is {bmi} and Under you are underweight")

elif bmi < 25:
    print(f"Yor bmi is {bmi} and you are normal weight")

elif bmi < 30:
    print(f"Yor bmi is {bmi} and you are slightly overweight")

elif bmi < 35:
    print(f"Yor bmi is {bmi} and you are obese")

else:
    print(f"Yor bmi is {bmi} and you are clinically obese")


