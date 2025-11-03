# ============================================================
# PASO 1: IMPORTAR HERRAMIENTAS NECESARIAS
# ============================================================

import random                    # Para elegir personas aleatorias
from art import logo, vs         # Traer decoraciones del archivo art.py
from game_data import data       # Traer lista de personas del archivo game_data.py


# ============================================================
# PASO 2: CREAR FUNCIÓN PARA FORMATEAR TEXTO
# ============================================================

def format_data(account):
    """Convierte un diccionario en texto legible"""
    name = account["name"]              # Extraer nombre
    description = account["description"] # Extraer descripción
    country = account["country"]        # Extraer país
    return f"{name}, a {description}, from {country}"  # Devolver texto formateado


# ============================================================
# PASO 3: CREAR FUNCIÓN PARA VERIFICAR RESPUESTA
# ============================================================

def check_answer(user_guess, a_followers, b_followers):
    """Verifica si el usuario eligió la cuenta con más seguidores"""
    if a_followers > b_followers:       # Si A tiene más seguidores
        return user_guess == "a"        # Usuario gana si eligió "a"
    else:                               # Si B tiene más seguidores
        return user_guess == "b"        # Usuario gana si eligió "b"


# ============================================================
# PASO 4: INICIALIZAR EL JUEGO
# ============================================================

print(logo)                             # Mostrar logo del juego
score = 0                               # Empezar puntaje en 0
game_should_continue = True             # Variable para controlar el bucle
account_b = random.choice(data)         # Elegir primera persona aleatoria


# ============================================================
# PASO 5: BUCLE PRINCIPAL DEL JUEGO
# ============================================================

while game_should_continue:             # Repetir mientras el juego continúe
    
    # --- Preparar las dos cuentas a comparar ---
    account_a = account_b               # B del turno anterior ahora es A
    account_b = random.choice(data)     # Elegir nueva persona B
    
    # Evitar que A y B sean la misma persona
    while account_a == account_b:
        account_b = random.choice(data) # Elegir otra B si son iguales
    
    # --- Mostrar la comparación en pantalla ---
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    # --- Pedir respuesta al usuario ---
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # --- Limpiar pantalla ---
    print("\n" * 20)                    # Imprimir 20 líneas vacías
    print(logo)                         # Mostrar logo de nuevo
    
    # --- Obtener número de seguidores ---
    a_follower_count = account_a["follower_count"]  # Seguidores de A
    b_follower_count = account_b["follower_count"]  # Seguidores de B
    
    # --- Verificar si el usuario acertó ---
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # --- Dar feedback según la respuesta ---
    if is_correct:                      # Si acertó
        score += 1                      # Sumar 1 punto
        print(f"You're right! Current score: {score}")
    else:                               # Si falló
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False    # Terminar el juego
