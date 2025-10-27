# Rock Paper Scissors Lizard Spock - Advanced Version
# Using modulus pattern for 5-option circular game logic

import random

# ASCII Art for all 5 options
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

lizard = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
       (o_o)
'''

spock = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
        \\//
'''

print("🖖 WELCOME TO ROCK, PAPER, SCISSORS, LIZARD, SPOCK! 🦎\n")
print("Game rules:")
print("✊ Rock crushes Scissors & Lizard")
print("📄 Paper covers Rock & disproves Spock")
print("✌️ Scissors cut Paper & decapitate Lizard")
print("🦎 Lizard eats Paper & poisons Spock")
print("🖖 Spock vaporizes Rock & smashes Scissors\n")

# Get user choice
choice = int(input("What do you choose?\n0 = Rock ✊\n1 = Paper 📄\n2 = Scissors ✌️\n3 = Lizard 🦎\n4 = Spock 🖖\nYour choice: "))

# Validate input
if choice < 0 or choice > 4:
    print("❌ Invalid choice! Please choose 0-4.")
else:
    # Store choices in list
    choices = [rock, paper, scissors, lizard, spock]
    choice_names = ["Rock ✊", "Paper 📄", "Scissors ✌️", "Lizard 🦎", "Spock 🖖"]
    
    # Show user's choice
    print(f"\nYou chose: {choice_names[choice]}")
    print(choices[choice])
    
    # Computer's random choice
    computer = random.randint(0, 4)
    print(f"Computer chose: {choice_names[computer]}")
    print(choices[computer])
    
    # THE MAGIC: Mathematical pattern with modulus
    result = (choice - computer) % 5
    
    # Determine outcome based on result
    if result == 0:
        print("🤝 It's a DRAW!")
    elif result == 1 or result == 2:
        print("🎉 YOU WIN! Well played!")
    else:  # result == 3 or result == 4
        print("😢 YOU LOSE! Better luck next time!")
    
    # Bonus: Show what beats what
    win_conditions = {
        0: "crushes Scissors & Lizard",    # Rock
        1: "covers Rock & disproves Spock", # Paper
        2: "cuts Paper & decapitates Lizard", # Scissors
        3: "eats Paper & poisons Spock",   # Lizard
        4: "vaporizes Rock & smashes Scissors" # Spock
    }
    
    if result != 0:
        if result == 1 or result == 2:
            print(f"✨ {choice_names[choice]} {win_conditions[choice]}!")
        else:
            print(f"💥 {choice_names[computer]} {win_conditions[computer]}!")
