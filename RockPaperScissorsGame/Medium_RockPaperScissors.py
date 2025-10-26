import random

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

print("WELCOME TO THE ROCK, PAPER SCISSORS GAME!\n")
choice = int(input("What do you choose?\nType 0 for rock, 1 for paper and 2 for scissors: "))

# Lista para acceder a los ASCII art por índice
game_images = [rock, paper, scissors]

# Mostrar elección del jugador
print(game_images[choice])

# Elección de la computadora (número aleatorio)
computer = random.randint(0, 2)
print("Computer chooses:")
print(game_images[computer])

# Lógica del juego con números
if choice == computer:
    print("Draw!")
elif (choice == 0 and computer == 2) or \
     (choice == 1 and computer == 0) or \
     (choice == 2 and computer == 1):
    print("You win!")
else:
    print("You lose!")