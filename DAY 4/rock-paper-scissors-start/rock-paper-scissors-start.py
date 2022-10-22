rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
pick = random.randint(0,2)
if pick == 0:
    print(rock)
    print("rock")
elif pick == 1:
    print(paper)
    print("paper")
else:
    print(scissors)
    print("scissors")