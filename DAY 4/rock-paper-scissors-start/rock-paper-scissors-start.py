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
player_pick =int(input("Plese make your pic 0for Rock, 1 for Paper and 2 for scissors"))
com_pick = random.randint(0,2)
# if com_pick == 0 and player_pick:
#     print(rock)
#     print("rock")
# elif pick == 1:
#     print(paper)
#     print("paper")
# else:
#     print(scissors)
#     print("scissors")
if com_pick == player_pick:
    print("Draw")
elif com_pick == 0 and player_pick == 2:
    print("Computer WON 😁")
elif com_pick == 1 and player_pick == 0:
    print("Computer WON 😁")
elif com_pick == 2 and player_pick == 1:
    print("Player 1 has WON 😁")
elif com_pick < player_pick:
    print("Player 1 has WON 😁")