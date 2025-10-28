## hangman.py
```python
# hangman.py
import random

# TODO-1 COMPLETADO: Importar la lista de palabras desde hangman_words.py
from hangman_words import word_list

# TODO-3 COMPLETADO: Importar el logo y los stages desde hangman_art.py
from hangman_art import logo, stages

# Mostrar el logo al inicio del juego
print(logo)

# =============================================================================
# CONFIGURACIÓN INICIAL DEL JUEGO
# =============================================================================

lives = 6
game_over = False
correct_letters = []
guessed_letters = []

# Elegir una palabra aleatoria de la lista importada
chosen_word = random.choice(word_list)

# DESCOMENTAR LA SIGUIENTE LÍNEA SOLO PARA HACER PRUEBAS (es trampa en el juego real)
# print(f"[MODO PRUEBA] La palabra secreta es: {chosen_word}")

# Crear el display inicial con guiones bajos
placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)
print("\n")

# =============================================================================
# BUCLE PRINCIPAL DEL JUEGO
# =============================================================================

while not game_over:

    # TODO-6 COMPLETADO: Mostrar cuántas vidas quedan
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4 COMPLETADO: Verificar si la letra ya fue intentada
    if guess in guessed_letters:
        print(f"\nYou've already guessed '{guess}'. Try another letter.")
        continue
    
    guessed_letters.append(guess)

    # Construir el display
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5 COMPLETADO: Informar si la letra no está en la palabra
    if guess not in chosen_word:
        print(f"\nYou guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            # TODO-7 COMPLETADO: Mostrar la palabra correcta al perder
            print(f"\n***********************IT WAS '{chosen_word}'! YOU LOSE**********************")

    # Verificar si el jugador ganó
    if "_" not in display:
        game_over = True
        print("\n****************************YOU WIN****************************")

    # TODO-2 COMPLETADO: Mostrar el dibujo del ahorcado según las vidas restantes
    print(stages[lives])
    print("\n")
```
