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

import random
print("WELCOME TO THE ROCK, PAPER SCISSORS GAME!\n")
choice = (input("What do you choose?\nType 0 for rock, 1 for paper and 2 for scissors."))
if choice == "0":
    print(rock)

elif choice == "1":
    print(paper)

elif choice == "2":
    print(scissors)

rc1 = [rock,paper,scissors]
print("Computer choses: ")
computer = (random.choice(rc1))

if computer == rock:
    print(rock)
    if choice == "0":
        print("draw!")
    elif choice == "1":
        print("you win!")
    elif choice == "2":
        print("you lose!")

elif computer == paper:
    print(paper)
    if choice == "0":
        print("you lose!")
    elif choice == "1":
        print("draw!")
    elif choice == "2":
        print("you win!")

elif computer == scissors:
    print(scissors)
    if choice == "0":  # Rock vs Scissors
        print("you win!")  # ✓ Rock vence a Scissors
    elif choice == "1":  # Paper vs Scissors
        print("you lose!")  # ✓ Scissors vencen a Paper
    elif choice == "2":  # Scissors vs Scissors
        print("draw!")  # ✓ Empate