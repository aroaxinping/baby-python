# 🎮 Number Guessing Game - Código Explicado Paso a Paso

## 📋 Código Completo con Explicaciones

```python
# ============================================================================
# PASO 1: IMPORTAR LIBRERÍAS NECESARIAS
# ============================================================================
import random
# random: librería para generar números aleatorios
# La necesitamos para crear el número secreto que el jugador debe adivinar


# ============================================================================
# PASO 2: DEFINIR CONSTANTES GLOBALES
# ============================================================================
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

# ¿Por qué MAYÚSCULAS? Es una convención en Python para indicar que son CONSTANTES
# (valores que NO deben cambiar durante la ejecución del programa)
# 
# ¿Por qué globales? Porque las usaremos en varias partes del código
# y queremos poder cambiarlas fácilmente en un solo lugar


# ============================================================================
# PASO 3: FUNCIÓN PARA GENERAR EL NÚMERO SECRETO
# ============================================================================
def choose_number():
    """
    Genera un número aleatorio entre 1 y 100
    
    Returns:
        int: Un número entero aleatorio entre 1 y 100 (ambos inclusive)
    
    Proceso lógico:
    1. Usar random.randint() para generar el número
    2. Devolver ese número para usarlo en otras partes del programa
    """
    number = random.randint(1, 100)
    # random.randint(a, b) genera un número aleatorio entre 'a' y 'b' (INCLUSIVE)
    # Ejemplo: randint(1, 100) puede dar 1, 50, 100, etc.
    
    return number
    # return: devuelve el valor para que otra parte del código lo use
    # Ejemplo de uso: secret = choose_number() → secret tendrá un número del 1-100


# ============================================================================
# PASO 4: FUNCIÓN PARA COMPARAR EL INTENTO CON EL NÚMERO SECRETO
# ============================================================================
def check_guess(guess, number, attempts):
    """
    Compara el número adivinado con el número secreto y da feedback
    
    Args:
        guess (int): El número que el jugador adivinó
        number (int): El número secreto que debe adivinar
        attempts (int): Cantidad de intentos restantes
    
    Returns:
        bool: True si adivinó correctamente, False si no
    
    Proceso lógico:
    1. Comparar guess con number
    2. Si son iguales → ¡Ganó!
    3. Si guess > number → "Too high"
    4. Si guess < number → "Too low"
    5. Informar intentos restantes
    6. Devolver True/False para saber si el juego debe continuar
    """
    
    # CASO 1: ¡ADIVINÓ CORRECTAMENTE! 🎉
    if guess == number:
        print(f"You got it! The answer was {number}")
        return True  
        # Devuelve True para indicar que el jugador GANÓ
        # Esto hará que el bucle del juego se detenga
    
    # CASO 2: El número es DEMASIADO ALTO 📉
    elif guess > number:
        print("Too high.")
        # Ejemplo: Si el secreto es 50 y adivinas 70 → 70 > 50 → "Too high"
        # Mensaje para el jugador: "Baja tu número"
    
    # CASO 3: El número es DEMASIADO BAJO 📈
    else:  # guess < number
        print("Too low.")
        # Ejemplo: Si el secreto es 50 y adivinas 20 → 20 < 50 → "Too low"
        # Mensaje para el jugador: "Sube tu número"
    
    # INFORMAR INTENTOS RESTANTES
    attempts -= 1  
    # Restamos 1 para calcular cuántos quedan DESPUÉS de este intento
    # Nota: Esto solo calcula, no modifica la variable original
    
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        # Solo mostramos esto si AÚN quedan intentos
        # Si attempts = 0, no tiene sentido decir "te quedan 0 intentos"
    
    return False  
    # Devuelve False porque NO adivinó correctamente
    # El juego debe continuar


# ============================================================================
# PASO 5: FUNCIÓN PRINCIPAL DEL JUEGO (EL CEREBRO)
# ============================================================================
def play_game():
    """
    Función principal que controla todo el flujo del juego
    
    Proceso lógico (ESTE ES EL ORDEN CORRECTO):
    1. Mostrar bienvenida
    2. Pedir nivel de dificultad
    3. Asignar número de intentos según el nivel
    4. Generar el número secreto
    5. BUCLE: Mientras haya intentos y no haya ganado
       5.1. Pedir un número al jugador
       5.2. Validar que sea un número válido
       5.3. Comparar con el número secreto
       5.4. Restar un intento
       5.5. Volver al paso 5.1 si no ganó y quedan intentos
    6. Mostrar mensaje final (victoria o derrota)
    """
    
    # ========================================
    # FASE 1: BIENVENIDA Y CONFIGURACIÓN
    # ========================================
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    
    # Pedir nivel de dificultad
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    # .lower() convierte todo a minúsculas para evitar problemas
    # Ejemplo: "EASY", "Easy", "easy" → todos se convierten en "easy"
    
    # Asignar intentos según el nivel elegido
    if level == "easy":
        attempts = EASY_LEVEL_ATTEMPTS  # 10 intentos
    else:
        attempts = HARD_LEVEL_ATTEMPTS  # 5 intentos
        # Si escribe cualquier cosa que no sea "easy", usamos hard
    
    # ========================================
    # FASE 2: GENERAR EL NÚMERO SECRETO
    # ========================================
    secret_number = choose_number()
    # Llamamos a la función que creamos antes
    # Esta función devuelve un número aleatorio del 1-100
    # Lo guardamos en secret_number para compararlo después
    
    # ========================================
    # FASE 3: BUCLE DEL JUEGO (LA PARTE MÁS IMPORTANTE)
    # ========================================
    won = False  
    # Variable bandera (flag) que indica si el jugador ganó
    # Empieza en False porque aún no ha ganado
    # Cuando adivine, la cambiamos a True para salir del bucle
    
    # BUCLE WHILE: Se repite mientras se cumplan AMBAS condiciones
    while attempts > 0 and not won:
        # Condición 1: attempts > 0 → Mientras tenga intentos disponibles
        # Condición 2: not won → Mientras NO haya ganado (won == False)
        # 
        # El bucle se detiene cuando:
        # - Se acaban los intentos (attempts = 0), O
        # - El jugador gana (won = True)
        
        # Mostrar intentos restantes al inicio de cada ronda
        print(f"\nYou have {attempts} attempts remaining.")
        
        # ========================================
        # PEDIR Y VALIDAR EL INTENTO DEL JUGADOR
        # ========================================
        try:
            # try: Intentamos ejecutar código que PODRÍA fallar
            # (en este caso, si el usuario escribe texto en vez de número)
            
            guess = int(input("Make a guess: "))
            # int() convierte el texto en número entero
            # Ejemplo: "42" (texto) → 42 (número)
            # Si el usuario escribe "hola", int() genera un error (ValueError)
            
            # Llamar a check_guess para comparar y obtener resultado
            won = check_guess(guess, secret_number, attempts)
            # won será True si adivinó, False si no
            # Esta línea es CRÍTICA: actualiza la variable won
            
            attempts -= 1  
            # Restamos 1 intento DESPUÉS de cada adivinanza
            # IMPORTANTE: Esto modifica la variable attempts del bucle
            # Ejemplo: Si tenía 10, ahora tiene 9
            # Cuando llegue a 0, el bucle se detendrá
            
        except ValueError:
            # except: Se ejecuta SOLO si hay un error en el try
            # ValueError: Error específico cuando int() no puede convertir
            
            print("Please enter a valid number!")
            # No restamos intentos si el usuario se equivocó de tipo
            # continue hace que el bucle vuelva a empezar sin ejecutar lo que sigue
            continue
    
    # ========================================
    # FASE 4: FIN DEL JUEGO - MENSAJE FINAL
    # ========================================
    # Llegamos aquí cuando el bucle termina
    # ¿Por qué terminó? Hay dos opciones:
    
    if not won:
        # Si won = False (NO ganó), significa que se acabaron los intentos
        print(f"\nYou've run out of guesses. The number was {secret_number}. You lose!")
    
    # Si won = True, ya mostramos el mensaje de victoria en check_guess()
    # Por eso no necesitamos un else aquí


# ============================================================================
# PASO 6: PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================
# Esta es la primera línea que se ejecuta cuando corres el programa
play_game()
# Llamamos a la función principal que controla todo el juego
```

---

## 🧠 Diagrama de Flujo Lógico

```
INICIO
  │
  ▼
┌─────────────────────────┐
│ Mostrar bienvenida      │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Pedir nivel (easy/hard) │
└───────────┬─────────────┘
            │
            ▼
      ┌─────┴─────┐
      │ if level  │
      │ == "easy" │
      └─────┬─────┘
            │
    ┌───────┴───────┐
    │               │
    ▼               ▼
attempts=10    attempts=5
    │               │
    └───────┬───────┘
            │
            ▼
┌─────────────────────────┐
│ secret = random(1-100)  │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ won = False             │
└───────────┬─────────────┘
            │
            ▼
    ┌───────────────┐
    │ while         │◄─────┐
    │ attempts > 0  │      │
    │ and not won   │      │
    └───────┬───────┘      │
            │              │
            ▼              │
┌─────────────────────────┐│
│ guess = input(número)   ││
└───────────┬─────────────┘│
            │              │
            ▼              │
      ┌─────────┐          │
      │ guess   │          │
      │ == num? │          │
      └────┬────┘          │
           │               │
    ┌──────┼──────┐        │
    │      │      │        │
    ▼      ▼      ▼        │
  igual  mayor  menor      │
    │      │      │        │
    │      ▼      ▼        │
    │   "high" "low"       │
    │      │      │        │
    │      └──┬───┘        │
    │         │            │
    │         ▼            │
    │   attempts -= 1      │
    │         │            │
    │         └────────────┘
    │
    ▼
  won = True
    │
    ▼
┌─────────────────────────┐
│ Salir del bucle         │
└───────────┬─────────────┘
            │
            ▼
      ┌─────────┐
      │ won ==  │
      │  True?  │
      └────┬────┘
           │
    ┌──────┴──────┐
    │             │
    ▼             ▼
  YES           NO
    │             │
    │             ▼
    │    "You lose!"
    │    "Number was X"
    │             │
    └──────┬──────┘
           │
           ▼
         FIN
```

---

## 📝 Conceptos Clave Explicados

### 1. ¿Por qué usar funciones?

**Sin funciones (código repetitivo):**
```python
# Generar número
number = random.randint(1, 100)

# Más tarde en el código...
number2 = random.randint(1, 100)  # Repetimos lo mismo

# Y otra vez...
number3 = random.randint(1, 100)  # ¡Muy repetitivo!
```

**Con funciones (código reutilizable):**
```python
def choose_number():
    return random.randint(1, 100)

# Ahora podemos usar esto cuantas veces queramos
number1 = choose_number()
number2 = choose_number()
number3 = choose_number()
```

---

### 2. ¿Cómo funciona el bucle while?

**Analogía:** Es como preguntar "¿puedo seguir jugando?"

```python
while attempts > 0 and not won:
    # Este código se repite mientras:
    # 1. Tenga intentos (attempts > 0)
    # 2. Y no haya ganado (not won)
```

**Ejemplo visual:**
```
Intento 1: attempts=10, won=False → ¿10>0? SÍ, ¿not False? SÍ → CONTINÚA
Intento 2: attempts=9,  won=False → ¿9>0?  SÍ, ¿not False? SÍ → CONTINÚA
Intento 3: attempts=8,  won=True  → ¿8>0?  SÍ, ¿not True?  NO → ¡PARA!

O si se acaban los intentos:
Intento 10: attempts=1, won=False → ¿1>0?  SÍ, ¿not False? SÍ → CONTINÚA
Intento 11: attempts=0, won=False → ¿0>0?  NO → ¡PARA!
```

---

### 3. ¿Por qué usar try/except?

**Problema sin try/except:**
```python
guess = int(input("Make a guess: "))
# Si el usuario escribe "hola"
# → ¡CRASH! El programa se detiene con error
```

**Solución con try/except:**
```python
try:
    guess = int(input("Make a guess: "))
except ValueError:
    print("Please enter a valid number!")
    # El programa NO se detiene, solo muestra el mensaje
```

---

### 4. Variables bandera (flags)

```python
won = False  # Bandera que indica si ganó
```

**¿Por qué se llaman banderas?**
- Como una bandera que se sube cuando algo pasa
- Empieza "abajo" (False)
- Cuando el evento ocurre, se "sube" (True)

**Uso en el juego:**
```python
won = False  # Bandera abajo = aún no ganó

if guess == number:
    won = True  # ¡Bandera arriba! = ganó

# Más tarde, checamos la bandera
if won:
    print("¡Felicidades!")
```

---

### 5. Parámetros y argumentos

**Definición de función (parámetros):**
```python
def check_guess(guess, number, attempts):
    #              ↑      ↑        ↑
    #         parámetros: variables que la función espera recibir
```

**Llamada de función (argumentos):**
```python
won = check_guess(50, secret_number, 10)
    #              ↑        ↑         ↑
    #         argumentos: valores que pasamos a la función
```

**Mapeo:**
```
check_guess(50, secret_number, 10)
            │         │         │
            ▼         ▼         ▼
def check_guess(guess, number, attempts):
```

---

## 🔍 Debugging Tips

### Si el juego no funciona, checa:

1. **¿El número se genera correctamente?**
   ```python
   # Agrega esto temporalmente para ver el número:
   secret_number = choose_number()
   print(f"DEBUG: El número es {secret_number}")  # Eliminar después
   ```

2. **¿Los intentos se restan correctamente?**
   ```python
   # Agrega esto en el bucle:
   print(f"DEBUG: Intentos restantes = {attempts}")
   ```

3. **¿El bucle funciona?**
   ```python
   # Agrega esto al inicio del bucle:
   print(f"DEBUG: Inicio del bucle - attempts={attempts}, won={won}")
   ```

---

## 💡 Retos para Mejorar el Juego

1. **Contador de rondas:** Mostrar en qué intento está el jugador
2. **Historial:** Guardar los números que ya intentó
3. **Pistas especiales:** "¡Estás muy cerca!" si está a ±5 del número
4. **Play again:** Preguntar si quiere jugar otra vez
5. **Modo extremo:** Solo 3 intentos
6. **Puntuación:** Dar más puntos si adivina en menos intentos

---

