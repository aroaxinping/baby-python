import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def choose_number():
    """Elige un número aleatorio entre 1 y 100"""
    number = random.randint(1, 100)
    return number


def check_guess(guess, number, attempts):
    """Compara el número adivinado con el correcto"""
    if guess == number:
        print(f"You got it! The answer was {number}")
        return True  # Indica que ganó
    elif guess > number:
        print("Too high.")
    else:  # guess < number
        print("Too low.")
    
    # Mostrar intentos restantes
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
    return False  # Indica que no ha ganado aún


def play_game():
    """Función principal del juego"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    
    # Elegir dificultad
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if level == "easy":
        attempts = EASY_LEVEL_ATTEMPTS
    else:
        attempts = HARD_LEVEL_ATTEMPTS
    
    # Elegir el número secreto
    secret_number = choose_number()
    
    # Bucle del juego
    won = False
    while attempts > 0 and not won:
        print(f"\nYou have {attempts} attempts remaining.")
        
        # Pedir al usuario que adivine
        try:
            guess = int(input("Make a guess: "))
            won = check_guess(guess, secret_number, attempts)
            attempts -= 1
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    # Si se acabaron los intentos
    if not won:
        print(f"\nYou've run out of guesses. The number was {secret_number}. You lose!")


# Iniciar el juego
play_game()
