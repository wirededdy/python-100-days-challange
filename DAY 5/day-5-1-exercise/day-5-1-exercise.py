# # 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
length = len(student_heights)
total = 0

for n in range(length):

  total += student_heights[n]
avg = round(total/length)

print(total)
print(avg)