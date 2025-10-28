# 🎮 EXPLICACIÓN ULTRA DETALLADA DEL CÓDIGO COMPLETO DE HANGMAN

## 📚 ÍNDICE

1. [Importaciones](#-parte-1-importaciones)
2. [Mostrar el Logo](#-parte-2-mostrar-el-logo)
3. [Configuración Inicial](#️-parte-3-configuración-inicial)
4. [Elegir Palabra Secreta](#-parte-4-elegir-palabra-secreta)
5. [Crear Display Inicial](#-parte-5-crear-display-inicial)
6. [El Bucle Principal](#-parte-6-el-bucle-principal)
7. [Mostrar Información al Jugador](#-parte-7-mostrar-información-al-jugador)
8. [Verificar Letras Repetidas](#-parte-8-verificar-letras-repetidas)
9. [Construir el Display](#-parte-9-construir-el-display-la-parte-más-importante)
10. [Verificar si la Letra es Incorrecta](#-parte-10-verificar-si-la-letra-es-incorrecta)
11. [Verificar Victoria](#-parte-11-verificar-victoria)
12. [Mostrar el Dibujo](#-parte-12-mostrar-el-dibujo)
13. [Resumen de Decisiones de Diseño](#-resumen-de-decisiones-de-diseño)
14. [Conceptos Clave Aprendidos](#-conceptos-clave-aprendidos)

---

## 📦 PARTE 1: IMPORTACIONES
```python
import random
from hangman_words import word_list
from hangman_art import logo, stages
```

### **🔍 Análisis línea por línea:**

#### **Línea 1: `import random`**

**¿Qué hace?**
- Importa el módulo `random` que nos permite elegir cosas al azar

**¿Por qué lo necesitamos?**
- Para elegir una palabra aleatoria de la lista

**❓ ¿Por qué NO usar otra cosa?**

| Alternativa | Por qué NO |
|-------------|-----------|
| Elegir siempre la primera palabra | ❌ El juego sería aburrido, siempre la misma palabra |
| Pedir al usuario que elija | ❌ El jugador vería la palabra (¡trampa!) |
| Usar el índice del día | ❌ Complicado y repetitivo cada día |

**✅ `random` es la mejor opción porque da variedad sin esfuerzo.**

---

#### **Línea 2: `from hangman_words import word_list`**

**¿Qué hace?**
- Importa SOLO la variable `word_list` del archivo `hangman_words.py`

**Sintaxis explicada:**
```python
from [archivo] import [cosa_específica]
```

**❓ Alternativas y por qué NO usarlas:**
```python
# Opción 1: import hangman_words
# Tendríamos que escribir: hangman_words.word_list
# ❌ Más largo y tedioso

# Opción 2: Poner la lista directamente aquí
word_list = ["python", "casa", "gato", ...]
# ❌ Hace el archivo muy largo y difícil de leer
# ❌ Si quieres cambiar palabras, debes buscar en todo el código

# Opción 3: from hangman_words import *
# ❌ Importa TODO (incluso lo que no necesitas)
# ❌ Puede causar conflictos de nombres

# ✅ Nuestra opción: Limpia, clara, solo lo necesario
from hangman_words import word_list
```

---

#### **Línea 3: `from hangman_art import logo, stages`**

**¿Qué hace?**
- Importa DOS cosas: `logo` y `stages`

**Nota:** Cuando importas múltiples cosas, las separas con comas.
```python
from archivo import cosa1, cosa2, cosa3
```

**❓ ¿Por qué importar y no copiar el arte aquí?**

| Opción | Ventaja | Desventaja |
|--------|---------|------------|
| Importar desde otro archivo | ✅ Código organizado<br>✅ Fácil de modificar<br>✅ Reutilizable | Necesitas múltiples archivos |
| Poner todo aquí | ✅ Un solo archivo | ❌ Archivo gigante<br>❌ Difícil de leer<br>❌ Código mezclado con arte |

**✅ Importar es la práctica profesional.**

---

## 🎨 PARTE 2: MOSTRAR EL LOGO
```python
print(logo)
```

**¿Qué hace?**
- Imprime el logo del juego (el título grande en ASCII art)

**❓ ¿Por qué usar `print()` y no otra cosa?**
```python
# Opción 1: Nuestra opción
print(logo)
# ✅ Simple, directo, claro

# Opción 2: print(f"{logo}")
# ❌ Innecesariamente complicado (f-string sin razón)

# Opción 3: sys.stdout.write(logo)
# ❌ Demasiado técnico para algo simple

# Opción 4: No mostrar nada
# ❌ El juego se ve aburrido sin título
```

**✅ `print(logo)` es perfecto: simple y efectivo.**

---

## ⚙️ PARTE 3: CONFIGURACIÓN INICIAL
```python
lives = 6
game_over = False
correct_letters = []
guessed_letters = []
```

### **Línea por línea:**

#### **`lives = 6`**

**¿Qué hace?**
- Crea una variable que guarda el número de vidas del jugador

**❓ ¿Por qué 6 y no otro número?**

| Número | Razón |
|--------|-------|
| 6 | ✅ Tradicional (6 partes del ahorcado)<br>✅ Balance perfecto |
| 3 | ❌ Muy difícil (juego frustrante) |
| 10 | ❌ Muy fácil (juego aburrido) |
| Infinito | ❌ Sin desafío |

**❓ ¿Por qué una variable y no un número fijo?**
```python
# Opción 1: Usar variable (nuestra opción)
lives = 6
lives -= 1  # Fácil de modificar
# ✅ Puedes cambiar, restar, sumar

# Opción 2: Usar el número directamente
if 6 == 0:  # ¿Qué?
# ❌ No tiene sentido
# ❌ No puedes modificarlo
```

---

#### **`game_over = False`**

**¿Qué hace?**
- Una "bandera" (flag) que indica si el juego terminó

**❓ ¿Por qué `False` al inicio?**
```python
game_over = False  # El juego NO ha terminado (está corriendo)
```

Más tarde:
```python
game_over = True  # El juego SÍ terminó (para el loop)
```

**❓ ¿Por qué NO usar otras alternativas?**

| Alternativa | Por qué NO |
|-------------|-----------|
| `game_over = 0` / `game_over = 1` | ❌ Menos claro que True/False |
| `game_status = "running"` | ❌ Más texto, más complicado |
| No usar variable | ❌ ¿Cómo controlas cuándo para el juego? |

**✅ Booleanos (True/False) son perfectos para "sí/no".**

---

#### **`correct_letters = []`**

**¿Qué hace?**
- Lista vacía que guardará las letras correctas

**❓ ¿Por qué una lista y NO otra cosa?**

| Estructura | Ventaja | Desventaja |
|------------|---------|------------|
| Lista `[]` | ✅ Puedes agregar elementos<br>✅ Mantiene orden<br>✅ Fácil de verificar | |
| String `""` | Funciona, pero menos claro | ❌ Más difícil de buscar |
| Set `{}` | Más rápido para búsquedas | ❌ No mantiene orden (no importa aquí) |
| Diccionario | ❌ Demasiado complejo para esto | |

**Ejemplo de uso:**
```python
correct_letters = []
correct_letters.append("a")  # Agrega "a"
correct_letters.append("e")  # Agrega "e"
# Resultado: ["a", "e"]

if "a" in correct_letters:  # Verifica si está
    print("Ya adivinaste la 'a'")
```

**✅ Lista es perfecta: simple y funcional.**

---

#### **`guessed_letters = []`**

**¿Qué hace?**
- Lista vacía que guardará TODAS las letras intentadas (correctas e incorrectas)

**❓ ¿Por qué DOS listas (`correct_letters` y `guessed_letters`)?**
```python
# Escenario: Jugador intenta "a", "z", "e"
# Palabra secreta: "casa"

correct_letters = ["a"]  # Solo las que SÍ están en "casa"
guessed_letters = ["a", "z", "e"]  # TODAS las que intentó
```

**¿Para qué sirve cada una?**

| Lista | Propósito |
|-------|-----------|
| `correct_letters` | Mostrar el display: `"_a_a"` |
| `guessed_letters` | Evitar repeticiones: "Ya intentaste 'z'" |

**❓ ¿Por qué NO usar solo una lista?**
```python
# Si solo tuviéramos correct_letters:
correct_letters = ["a"]

# Jugador intenta "z" por segunda vez
if "z" in correct_letters:  # ❌ "z" NO está aquí
    print("Ya la intentaste")  # Nunca se ejecuta
# ❌ No podemos detectar letras incorrectas repetidas
```

**✅ Dos listas = dos propósitos diferentes.**

---

## 🎲 PARTE 4: ELEGIR PALABRA SECRETA
```python
chosen_word = random.choice(word_list)
```

### **Desglose completo:**

**`random.choice(word_list)`**
- `random`: El módulo que importamos
- `.choice()`: Función que elige un elemento aleatorio
- `word_list`: La lista de palabras

**¿Cómo funciona internamente?**
```python
word_list = ["python", "casa", "gato"]

# random.choice() hace algo así:
# 1. Genera número aleatorio entre 0 y 2 (len de la lista)
# 2. Digamos que sale 1
# 3. Devuelve word_list[1] → "casa"

chosen_word = random.choice(word_list)  # Podría ser cualquiera
```

**❓ Alternativas y por qué NO usarlas:**
```python
# Opción 1: Nuestra opción
chosen_word = random.choice(word_list)
# ✅ Simple, una línea, fácil

# Opción 2: Con índice manual
import random
index = random.randint(0, len(word_list) - 1)
chosen_word = word_list[index]
# ❌ Dos líneas para lo mismo
# ❌ Puedes cometer errores con los índices

# Opción 3: Usar random.sample()
chosen_word = random.sample(word_list, 1)[0]
# ❌ Más complicado
# ❌ Devuelve una lista, necesitas [0]

# Opción 4: Primera palabra siempre
chosen_word = word_list[0]
# ❌ Sin variedad, aburrido
```

**✅ `random.choice()` es la forma más Pythonica (idiomática).**

---

## 📝 PARTE 5: CREAR DISPLAY INICIAL
```python
placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)
print("\n")
```

### **Línea 1: `placeholder = "_" * len(chosen_word)`**

**Desglose:**
```python
chosen_word = "gato"  # 4 letras
len(chosen_word)  # Devuelve 4
"_" * 4  # Devuelve "____"
placeholder = "____"
```

**Tabla de ejecución:**

| Si `chosen_word` es... | `len()` devuelve... | `"_" *` devuelve... | `placeholder` es... |
|------------------------|---------------------|---------------------|---------------------|
| `"sol"` | 3 | `"___"` | `"___"` |
| `"python"` | 6 | `"______"` | `"______"` |
| `"casa"` | 4 | `"____"` | `"____"` |

**❓ Alternativas:**
```python
# Opción 1: Nuestra opción
placeholder = "_" * len(chosen_word)
# ✅ Una línea, elegante

# Opción 2: Loop manual
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
# ❌ 3 líneas para lo mismo
# ❌ Más lento

# Opción 3: List comprehension + join
placeholder = "".join(["_" for letter in chosen_word])
# ❌ Demasiado complejo para algo simple

# Opción 4: Hardcoded
placeholder = "______"
# ❌ Solo funciona si todas las palabras tienen 6 letras
# ❌ No flexible
```

**✅ Multiplicar strings es perfecto aquí.**

---

### **Línea 2: `print("Word to guess: " + placeholder)`**

**¿Qué hace?**
- Imprime: `Word to guess: ____`

**Concatenación explicada:**
```python
"Word to guess: " + "____"
# El + une (concatena) dos strings
# Resultado: "Word to guess: ____"
```

**❓ Alternativas:**
```python
# Opción 1: Nuestra opción (concatenación)
print("Word to guess: " + placeholder)
# ✅ Simple, directo

# Opción 2: f-string
print(f"Word to guess: {placeholder}")
# ✅ También válido (más moderno)

# Opción 3: Múltiples argumentos
print("Word to guess:", placeholder)
# ✅ También funciona (agrega espacio automático)

# Opción 4: format()
print("Word to guess: {}".format(placeholder))
# ❌ Más viejo, más verboso
```

**✅ Cualquiera de las primeras 3 opciones está bien. Es cuestión de preferencia.**

---

### **Línea 3: `print("\n")`**

**¿Qué hace?**
- Imprime una línea en blanco

**`\n` explicado:**
- `\n` = "newline" = salto de línea
- Es un carácter especial

**Ejemplo:**
```python
print("Hola")
print("\n")
print("Mundo")

# Salida:
# Hola
#
# Mundo
```

**❓ Alternativas:**
```python
# Opción 1: Nuestra opción
print("\n")
# ✅ Explícito

# Opción 2: print() vacío
print()
# ✅ También funciona (hace lo mismo)

# Opción 3: Múltiples \n
print("\n\n\n")
# ✅ Para más espacio

# Opción 4: No poner nada
# ❌ El juego se ve apretado, difícil de leer
```

**✅ `print("\n")` o `print()` son equivalentes aquí.**

---

## 🔄 PARTE 6: EL BUCLE PRINCIPAL
```python
while not game_over:
```

### **Análisis profundo:**

**¿Qué hace?**
- Repite el código interior mientras `game_over` sea `False`

**Tabla de verdad:**

| `game_over` | `not game_over` | ¿Se ejecuta el loop? |
|-------------|-----------------|----------------------|
| `False` | `True` | ✅ SÍ |
| `True` | `False` | ❌ NO (sale del loop) |

**Ejemplo paso a paso:**
```python
game_over = False

while not game_over:  # not False = True → ENTRA
    print("Jugando...")
    # ... código del juego ...
    if lives == 0:
        game_over = True  # Ahora es True

# Próxima iteración:
while not game_over:  # not True = False → NO ENTRA (termina)
```

**❓ ¿Por qué `while` y NO `for`?**

| Loop | Cuándo usarlo |
|------|---------------|
| `while` | ✅ Cuando NO sabes cuántas veces repetir<br>✅ Basado en una condición<br>✅ "Mientras algo sea verdad" |
| `for` | ❌ Cuando sabes exactamente cuántas veces<br>❌ "Para cada elemento" |

**Ejemplo comparativo:**
```python
# ❌ MAL: Intentar usar for
for i in range(???):  # ¿Cuántas veces? No sabemos
    # Jugador puede ganar en 4 intentos o en 20

# ✅ BIEN: Usar while
while not game_over:  # Se repite hasta que termine
    # Puede ser 1 vuelta o 100, no importa
```

**❓ Alternativas al `while not game_over`:**
```python
# Opción 1: Nuestra opción
while not game_over:
# ✅ Claro: "mientras el juego NO haya terminado"

# Opción 2: while game_over == False:
# ✅ Funciona igual, pero más verboso

# Opción 3: while True con break
while True:
    # ... código ...
    if lives == 0:
        break
# ❌ Menos claro (no se ve la condición arriba)

# Opción 4: Usar una función recursiva
def play_game():
    if not game_over:
        # ... código ...
        play_game()  # Se llama a sí misma
# ❌ Demasiado complejo
# ❌ Puede causar errores de recursión
```

**✅ `while not game_over` es la opción más clara y Pythonica.**

---

## 💬 PARTE 7: MOSTRAR INFORMACIÓN AL JUGADOR
```python
print(f"****************************{lives}/6 LIVES LEFT****************************")
guess = input("Guess a letter: ").lower()
```

### **Línea 1: El f-string**
```python
print(f"****************************{lives}/6 LIVES LEFT****************************")
```

**Desglose:**
```python
lives = 3  # Ejemplo

# La f antes de las comillas activa el "f-string"
f"****************************{lives}/6 LIVES LEFT****************************"

# {lives} se reemplaza por el valor de la variable
# Resultado: "****************************3/6 LIVES LEFT****************************"
```

**❓ ¿Por qué f-string y NO otra cosa?**
```python
# Opción 1: f-string (nuestra opción)
print(f"{lives}/6 LIVES LEFT")
# ✅ Moderno, claro, fácil de leer

# Opción 2: Concatenación
print(str(lives) + "/6 LIVES LEFT")
# ❌ Necesitas convertir a string manualmente
# ❌ Más propenso a errores

# Opción 3: format()
print("{}/6 LIVES LEFT".format(lives))
# ❌ Más viejo, menos legible

# Opción 4: % formatting
print("%d/6 LIVES LEFT" % lives)
# ❌ Muy viejo, confuso
```

**✅ F-strings son el estándar moderno de Python (desde 3.6+).**

---

### **Línea 2: `input().lower()`**
```python
guess = input("Guess a letter: ").lower()
```

**Desglose paso a paso:**
```python
# Paso 1: input() pide datos al usuario
input("Guess a letter: ")  
# Usuario escribe: "A"
# Devuelve: "A" (string)

# Paso 2: .lower() convierte a minúsculas
"A".lower()  
# Devuelve: "a"

# Paso 3: Se guarda en la variable
guess = "a"
```

**❓ ¿Por qué `.lower()` es crucial?**
```python
# Sin .lower():
chosen_word = "casa"
guess = "A"  # Usuario escribió mayúscula

if "A" == "a":  # ❌ False (Python es case-sensitive)
    print("Correcto")
# No se ejecuta, aunque "a" SÍ está en "casa"

# Con .lower():
guess = "A".lower()  # guess = "a"

if "a" == "a":  # ✅ True
    print("Correcto")
# Funciona perfectamente
```

**❓ Alternativas:**
```python
# Opción 1: Nuestra opción (.lower())
guess = input("Guess a letter: ").lower()
# ✅ Convierte a minúsculas inmediatamente

# Opción 2: Convertir la palabra a mayúsculas
chosen_word = "CASA"
guess = input("Guess a letter: ").upper()
# ✅ También funciona
# ❌ Pero las palabras en minúsculas son más comunes

# Opción 3: Comparación case-insensitive
if guess.lower() == letter.lower():
# ❌ Conviertes CADA VEZ que comparas (ineficiente)

# Opción 4: No usar .lower()
# ❌ El juego solo funciona si escribes en minúsculas
# ❌ Muy frustrante para el usuario
```

**✅ `.lower()` una vez al inicio es lo más eficiente.**

---

## 🔍 PARTE 8: VERIFICAR LETRAS REPETIDAS
```python
if guess in guessed_letters:
    print(f"\nYou've already guessed '{guess}'. Try another letter.")
    continue

guessed_letters.append(guess)
```

### **Línea 1: `if guess in guessed_letters:`**

**¿Qué hace?**
- Verifica si la letra ya fue intentada antes

**Operador `in` explicado:**
```python
guessed_letters = ["a", "e", "z"]

"a" in guessed_letters  # True (sí está)
"b" in guessed_letters  # False (no está)
"e" in guessed_letters  # True (sí está)
```

**Tabla de ejecución:**

| `guess` | `guessed_letters` | `guess in guessed_letters` | ¿Qué pasa? |
|---------|-------------------|----------------------------|------------|
| `"a"` | `[]` | `False` | Se agrega a la lista |
| `"e"` | `["a"]` | `False` | Se agrega a la lista |
| `"a"` | `["a", "e"]` | `True` | Muestra mensaje de error |

**❓ ¿Por qué usar `in` y NO otra cosa?**
```python
# Opción 1: Nuestra opción (operador in)
if guess in guessed_letters:
# ✅ Una línea, claro, Pythonico

# Opción 2: Loop manual
already_guessed = False
for letter in guessed_letters:
    if letter == guess:
        already_guessed = True
if already_guessed:
# ❌ 5 líneas para lo mismo

# Opción 3: Usar sets
guessed_letters_set = set()
if guess in guessed_letters_set:
# ✅ Más rápido para listas GIGANTES
# ❌ Innecesario aquí (máximo 26 letras)

# Opción 4: No verificar
# ❌ Usuario puede intentar "a" 100 veces
# ❌ Mala experiencia de usuario
```

**✅ `in` con listas es perfecto para 26 letras máximo.**

---

### **Línea 2: `print(f"\nYou've already guessed '{guess}'. Try another letter.")`**

**Nota el `\n` al inicio:**
```python
print(f"\nYou've already guessed...")
#       ↑ Agrega línea en blanco antes del mensaje
```

**Comparación visual:**
```python
# Sin \n:
****************************3/6 LIVES LEFT****************************
You've already guessed 'a'. Try another letter.

# Con \n:
****************************3/6 LIVES LEFT****************************

You've already guessed 'a'. Try another letter.
```

**✅ El `\n` hace el juego más legible.**

---

### **Línea 3: `continue`**

**¿Qué hace `continue`?**
- Salta el resto del loop y vuelve al inicio

**Flujo sin `continue`:**
```python
while not game_over:
    if guess in guessed_letters:
        print("Ya la intentaste")
        # ❌ El código continúa ejecutándose
        # ❌ El jugador pierde una vida injustamente
    
    # Este código se ejecuta incluso con letra repetida
    lives -= 1
```

**Flujo con `continue`:**
```python
while not game_over:
    if guess in guessed_letters:
        print("Ya la intentaste")
        continue  # ✅ Salta TODO lo de abajo
                  # ✅ Vuelve al inicio del while
    
    # Este código NO se ejecuta si hay continue
    lives -= 1
```

**Diagrama de flujo:**
```
┌─────────────────────────┐
│  while not game_over:   │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ ¿Ya intentó esta letra? │
└────┬────────────┬───────┘
     │ SÍ         │ NO
     ▼            ▼
┌─────────┐  ┌──────────────┐
│ Mensaje │  │ Continuar    │
│continue │  │ con el juego │
└────┬────┘  └──────┬───────┘
     │              │
     │              ▼
     │         [resto del código]
     │              │
     └──────────────┘
            ▼
    [Vuelve al while]
```

**❓ Alternativas:**
```python
# Opción 1: Nuestra opción (continue)
if guess in guessed_letters:
    print("Ya intentaste esa")
    continue
# ✅ Claro, salta al inicio del loop

# Opción 2: Usar else
if guess not in guessed_letters:
    # Todo el código del juego aquí
else:
    print("Ya intentaste esa")
# ❌ Indenta TODO el código
# ❌ Menos legible

# Opción 3: Usar banderas
should_process = True
if guess in guessed_letters:
    should_process = False
if should_process:
    # resto del código
# ❌ Variable extra innecesaria

# Opción 4: No verificar repeticiones
# ❌ Usuario pierde vida por intentar letra repetida
# ❌ Frustrante
```

**✅ `continue` es la forma más limpia de saltar iteraciones.**

---

### **Línea 4: `guessed_letters.append(guess)`**

**¿Qué hace?**
- Agrega la letra a la lista de letras intentadas

**Ejemplo de ejecución:**
```python
guessed_letters = []

# Jugador intenta "a"
guessed_letters.append("a")
# guessed_letters = ["a"]

# Jugador intenta "e"
guessed_letters.append("e")
# guessed_letters = ["a", "e"]

# Jugador intenta "z"
guessed_letters.append("z")
# guessed_letters = ["a", "e", "z"]
```

**❓ ¿Por qué `.append()` y NO otra cosa?**
```python
# Opción 1: .append() (nuestra opción)
guessed_letters.append(guess)
# ✅ Método estándar para agregar a listas

# Opción 2: Concatenación
guessed_letters = guessed_letters + [guess]
# ❌ Crea una nueva lista cada vez (ineficiente)
# ❌ Más verboso

# Opción 3: .insert()
guessed_letters.insert(0, guess)
# ❌ Más lento (reordena toda la lista)
# ❌ El orden no importa aquí

# Opción 4: .extend()
guessed_letters.extend([guess])
# ❌ Diseñado para agregar múltiples elementos
# ❌ Innecesario aquí
```

**✅ `.append()` es el método estándar y más eficiente.**

---

## 🎨 PARTE 9: CONSTRUIR EL DISPLAY (LA PARTE MÁS IMPORTANTE)
```python
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
```

### **Esta es la parte CRÍTICA del juego. Vamos muy despacio.**

---

### **Línea 1: `display = ""`**

**¿Qué hace?**
- Inicializa un string vacío que construiremos

**❓ ¿Por qué empezar vacío?**
```python
# Cada vuelta del while, reconstruimos desde cero
while not game_over:
    display = ""  # Borramos lo anterior
    # Construimos el display nuevo basado en letras actuales
```

**❓ ¿Por qué NO mantener el display entre iteraciones?**
```python
# ❌ MAL: Mantener display
display = "____"  # Primera vez
# Jugador adivina "a" en "casa"
display = "_a_a"  # Se actualiza
# Jugador adivina "c"
# ¿Cómo sabemos dónde poner la "c" si ya tenemos "_a_a"?
# ❌ Complica la lógica

# ✅ BIEN: Reconstruir cada vez
display = ""  # Empezamos de cero
# Recorremos TODA la palabra con todas las letras adivinadas
# Resultado correcto: "ca_a"
```

**Analogía:** Es como un rompecabezas. Cada vez que encuentras una pieza nueva, NO intentas encajarla en el rompecabezas parcial. Más fácil es **volver a armar todo** con todas las piezas que tienes.

---

### **Línea 2: `for letter in chosen_word:`**

**¿Qué hace?**
- Recorre cada letra de la palabra secreta

**Ejemplo ultra detallado:**
```python
chosen_word = "casa"

for letter in chosen_word:
    # Iteración 1: letter = "c"
    # Iteración 2: letter = "a"
    # Iteración 3: letter = "s"
    # Iteración 4: letter = "a"
```

**❓ ¿Por qué recorrer la palabra secreta y NO las letras adivinadas?**
```python
# ❌ MAL: Recorrer letras adivinadas
correct_letters = ["a", "e"]
for letter in correct_letters:
    # Solo recorremos 2 letras
    # ¿Dónde están en la palabra? No sabemos

# ✅ BIEN: Recorrer palabra secreta
chosen_word = "casa"
for letter in chosen_word:
    # Recorremos las 4 posiciones
    # Sabemos exactamente el orden
```

**Clave:** Necesitamos mantener el **orden** de la palabra original.

---

### **Las tres condiciones (IF / ELIF / ELSE):**

Ahora viene lo más importante. Vamos SUPER despacio:
```python
if letter == guess:
    display += letter
    correct_letters.append(guess)
elif letter in correct_letters:
    display += letter
else:
    display += "_"
```

---

#### **CONDICIÓN 1: `if letter == guess:`**

**¿Qué pregunta?**
- "¿La letra actual de la palabra es igual a la letra que el jugador acaba de adivinar?"

**Ejemplo:**
```python
chosen_word = "casa"
guess = "a"
correct_letters = []  # Aún no ha adivinado nada antes

# Recorriendo "casa":

# Iteración 1:
letter = "c"
if "c" == "a":  # False
    # No se ejecuta

# Iteración 2:
letter = "a"
if "a" == "a":  # True ✅
    display += "a"  # display = "a"
    correct_letters.append("a")  # correct_letters = ["a"]

# Iteración 3:
letter = "s"
if "s" == "a":  # False
    # No se ejecuta

# Iteración 4:
letter = "a"
if "a" == "a":  # True ✅
    display += "a"  # display = "aa"
    correct_letters.append("a")  # correct_letters = ["a", "a"]
```

**¿Por qué agregamos a `correct_letters`?**
- Para la **próxima** ronda
- Si el jugador adivina "c" después, necesitamos recordar que ya adivinó "a"

---

#### **CONDICIÓN 2: `elif letter in correct_letters:`**

**¿Qué pregunta?**
- "Si no es la letra actual, ¿es una letra que ya adivinamos antes?"

**Ejemplo (siguiente ronda):**
```python
chosen_word = "casa"
guess = "c"  # Ahora adivina "c"
correct_letters = ["a", "a"]  # De la ronda anterior

# Recorriendo "casa":

# Iteración 1:
letter = "c"
if "c" == "c":  # True ✅
    display += "c"  # display = "c"
    correct_letters.append("c")  # correct_letters = ["a", "a", "c"]

# Iteración 2:
letter = "a"
if "a" == "c":  # False
elif "a" in ["a", "a", "c"]:  # True ✅
    display += "a"  # display = "ca"

# Iteración 3:
letter = "s"
if "s" == "c":  # False
elif "s" in ["a", "a", "c"]:  # False
    # No se ejecuta, va al else

# Iteración 4:
letter = "a"
if "a" == "c":  # False
elif "a" in ["a", "a", "c"]:  # True ✅
    display += "a"  # display = "caa" (falta la última)
```

**¿Por qué esta condición es necesaria?**
- Para mostrar letras de rondas anteriores
- Sin esto, solo verías la letra que acabas de adivinar

---

#### **CONDICIÓN 3: `else:`**

**¿Qué pregunta?**
- "Si no es ninguna de las anteriores, entonces la letra aún no fue adivinada"

**Ejemplo (continuando):**
```python
# Iteración 3 (de arriba):
letter = "s"
if "s" == "c":  # False
elif "s" in ["a", "a", "c"]:  # False
else:  # ✅ Se ejecuta esto
    display += "_"  # display = "ca_"
```

---

### **VISUALIZACIÓN COMPLETA DE UNA PARTIDA:**
```python
chosen_word = "gato"
correct_letters = []
```

#### **Ronda 1: Jugador adivina "a"**

| Iteración | `letter` | `guess` | `correct_letters` antes | Condición que se cumple | `display` |
|-----------|----------|---------|-------------------------|-------------------------|-----------|
| 1 | `"g"` | `"a"` | `[]` | `else` | `"_"` |
| 2 | `"a"` | `"a"` | `[]` | `if letter == guess` | `"_a"` |
| 3 | `"t"` | `"a"` | `["a"]` | `else` | `"_a_"` |
| 4 | `"o"` | `"a"` | `["a"]` | `else` | `"_a__"` |

**Resultado:** `"_a__"` y `correct_letters = ["a"]`

---

#### **Ronda 2: Jugador adivina "t"**

| Iteración | `letter` | `guess` | `correct_letters` antes | Condición que se cumple | `display` |
|-----------|----------|---------|-------------------------|-------------------------|-----------|
| 1 | `"g"` | `"t"` | `["a"]` | `else` | `"_"` |
| 2 | `"a"` | `"t"` | `["a"]` | `elif letter in correct_letters` | `"_a"` |
| 3 | `"t"` | `"t"` | `["a"]` | `if letter == guess` | `"_at"` |
| 4 | `"o"` | `"t"` | `["a", "t"]` | `else` | `"_at_"` |

**Resultado:** `"_at_"` y `correct_letters = ["a", "t"]`

---

#### **Ronda 3: Jugador adivina "g"**

| Iteración | `letter` | `guess` | `correct_letters` antes | Condición que se cumple | `display` |
|-----------|----------|---------|-------------------------|-------------------------|-----------|
| 1 | `"g"` | `"g"` | `["a", "t"]` | `if letter == guess` | `"g"` |
| 2 | `"a"` | `"g"` | `["a", "t", "g"]` | `elif letter in correct_letters` | `"ga"` |
| 3 | `"t"` | `"g"` | `["a", "t", "g"]` | `elif letter in correct_letters` | `"gat"` |
| 4 | `"o"` | `"g"` | `["a", "t", "g"]` | `else` | `"gat_"` |

**Resultado:** `"gat_"` y `correct_letters = ["a", "t", "g"]`

---

### **❓ ¿Por qué usar IF / ELIF / ELSE y NO otras cosas?**
```python
# Opción 1: Nuestra opción (if/elif/else)
if letter == guess:
    display += letter
elif letter in correct_letters:
    display += letter
else:
    display += "_"
# ✅ Solo UNA condición se ejecuta
# ✅ Claro y eficiente

# Opción 2: Tres IF separados
if letter == guess:
    display += letter
if letter in correct_letters:  # ❌ Se puede ejecutar TAMBIÉN
    display += letter
if letter != guess:
    display += "_"
# ❌ Múltiples condiciones pueden ejecutarse
# ❌ display podría tener "aa_" en lugar de "a"

# Opción 3: IFs anidados
if letter == guess:
    display += letter
else:
    if letter in correct_letters:
        display += letter
    else:
        display += "_"
# ✅ Funciona
# ❌ Más difícil de leer (anidación)

# Opción 4: Operador ternario
display += letter if (letter == guess or letter in correct_letters) else "_"
# ❌ No agrega a correct_letters
# ❌ Menos legible
```

**✅ IF/ELIF/ELSE es la estructura más clara para decisiones múltiples.**

---

### **Línea final: `print("Word to guess: " + display)`**

**¿Qué hace?**
- Muestra el resultado al jugador

**Ejemplo de salida:**
```
Word to guess: _a__
```

---

## ❌ PARTE 10: VERIFICAR SI LA LETRA ES INCORRECTA
```python
if guess not in chosen_word:
    print(f"\nYou guessed '{guess}', that's not in the word. You lose a life.")
    lives -= 1

    if lives == 0:
        game_over = True
        print(f"\n***********************IT WAS '{chosen_word}'! YOU LOSE**********************")
```

### **Línea 1: `if guess not in chosen_word:`**

**¿Qué hace?**
- Verifica si la letra NO está en la palabra

**Ejemplos:**
```python
chosen_word = "casa"

"a" not in "casa"  # False (sí está)
"z" not in "casa"  # True (no está)
"c" not in "casa"  # False (sí está)
```

**❓ ¿Por qué usar `not in` y NO otra cosa?**
```python
# Opción 1: not in (nuestra opción)
if guess not in chosen_word:
# ✅ Pythonico, claro

# Opción 2: Negación de in
if not (guess in chosen_word):
# ✅ Funciona igual
# ❌ Paréntesis innecesarios

# Opción 3: Loop manual
found = False
for letter in chosen_word:
    if letter == guess:
        found = True
if not found:
# ❌ 5 líneas vs 1 línea

# Opción 4: Usar .find()
if chosen_word.find(guess) == -1:
# ❌ Menos intuitivo
# ❌ Específico de strings
```

**✅ `not in` es la forma más Pythonica.**

---

### **Línea 2: Mensaje de error**
```python
print(f"\nYou guessed '{guess}', that's not in the word. You lose a life.")
```

**Elementos del mensaje:**
- `\n`: Línea en blanco para separar
- `{guess}`: La letra que intentó
- Feedback claro sobre qué pasó

**✅ Buen UX (experiencia de usuario):** Ser claro sobre lo que pasó y por qué.

---

### **Línea 3: `lives -= 1`**

**¿Qué hace?**
- Resta una vida

**Operador `-=` explicado:**
```python
lives = 6
lives -= 1  # Mismo que: lives = lives - 1
# Ahora lives = 5

lives -= 1
# Ahora lives = 4
```

**Tabla de ejecución:**

| Antes | Operación | Después |
|-------|-----------|---------|
| `lives = 6` | `lives -= 1` | `lives = 5` |
| `lives = 5` | `lives -= 1` | `lives = 4` |
| `lives = 1` | `lives -= 1` | `lives = 0` |

**❓ Alternativas:**
```python
# Opción 1: -= (nuestra opción)
lives -= 1
# ✅ Conciso, estándar

# Opción 2: Resta explícita
lives = lives - 1
# ✅ También correcto
# ❌ Más verboso

# Opción 3: Decrementar manualmente
lives = 5  # Si antes era 6
# ❌ Propenso a errores
# ❌ No escalable
```

**✅ `lives -= 1` es el estándar.**

---

### **Líneas 4-6: Verificar derrota**
```python
if lives == 0:
    game_over = True
    print(f"\n***********************IT WAS '{chosen_word}'! YOU LOSE**********************")
```

**¿Qué hace?**
- Si se acabaron las vidas, termina el juego y revela la palabra

**❓ ¿Por qué `== 0` y NO `<= 0`?**
```python
# Opción 1: == 0 (nuestra opción)
if lives == 0:
# ✅ Más específico

# Opción 2: <= 0
if lives <= 0:
# ✅ Más seguro (por si hay un bug y lives llega a -1)
# ❌ Innecesario si el código está bien

# Opción 3: < 1
if lives < 1:
# ✅ También funciona
# ❌ Menos claro que == 0
```

**En este caso, ambas opciones 1 y 2 están bien. Es preferencia personal.**

---

## 🏆 PARTE 11: VERIFICAR VICTORIA
```python
if "_" not in display:
    game_over = True
    print("\n****************************YOU WIN****************************")
```

### **Línea 1: `if "_" not in display:`**

**¿Qué hace?**
- Verifica si ya NO hay guiones bajos en el display

**Lógica:**
- Si `display = "casa"` → No hay "_" → ¡Ganaste!
- Si `display = "ca_a"` → Sí hay "_" → Aún falta

**Ejemplos:**
```python
"_" not in "casa"  # True (no hay guiones → ganó)
"_" not in "ca_a"  # False (sí hay guiones → falta)
"_" not in "____"  # False (todo son guiones → falta mucho)
```

**❓ ¿Por qué esta lógica y NO otra?**
```python
# Opción 1: Verificar guiones bajos (nuestra opción)
if "_" not in display:
# ✅ Simple, directo
# ✅ Una línea

# Opción 2: Comparar con la palabra
if display == chosen_word:
# ✅ También funciona
# ❌ Menos obvio por qué funciona

# Opción 3: Verificar longitud de correct_letters
if len(correct_letters) == len(set(chosen_word)):
# ✅ Correcto técnicamente
# ❌ Requiere entender sets
# ❌ Más complejo

# Opción 4: Contador manual
count = 0
for letter in chosen_word:
    if letter in correct_letters:
        count += 1
if count == len(chosen_word):
# ❌ Demasiado complejo
# ❌ Múltiples líneas
```

**✅ Verificar `"_" not in display` es la forma más simple y clara.**

---

### **Líneas 2-3: Mensaje de victoria**
```python
game_over = True
print("\n****************************YOU WIN****************************")
```

**¿Por qué poner `game_over = True`?**
- Para que el `while not game_over` termine
- Sin esto, el juego continuaría infinitamente

---

## 🎨 PARTE 12: MOSTRAR EL DIBUJO
```python
print(stages[lives])
print("\n")
```

### **`stages[lives]` - CONCEPTO CRUCIAL**

**¿Cómo funciona?**
```python
stages = [
    '''[dibujo completo]''',  # stages[0] = 0 vidas
    '''[5 partes]''',          # stages[1] = 1 vida
    '''[4 partes]''',          # stages[2] = 2 vidas
    '''[3 partes]''',          # stages[3] = 3 vidas
    '''[2 partes]''',          # stages[4] = 4 vidas
    '''[1 parte]''',           # stages[5] = 5 vidas
    '''[vacío]'''              # stages[6] = 6 vidas
]

# Si lives = 3:
print(stages[3])  # Muestra el dibujo con 3 partes
```

**Tabla de correspondencia:**

| `lives` | `stages[lives]` | Dibujo |
|---------|-----------------|--------|
| 6 | `stages[6]` | Vacío (no has perdido) |
| 5 | `stages[5]` | Solo cabeza |
| 4 | `stages[4]` | Cabeza + cuerpo |
| 3 | `stages[3]` | + brazo izquierdo |
| 2 | `stages[2]` | + ambos brazos |
| 1 | `stages[1]` | + pierna izquierda |
| 0 | `stages[0]` | Completo (perdiste) |

**¿Por qué funciona tan bien?**

La lista `stages` está ordenada **inversamente** a las vidas:
- Más vidas = índice mayor = dibujo más vacío
- Menos vidas = índice menor = dibujo más completo

**Ejemplo de ejecución:**
```python
lives = 6
print(stages[6])  # Muestra horca vacía

# Jugador falla una vez
lives -= 1  # lives = 5
print(stages[5])  # Muestra cabeza

# Jugador falla otra vez
lives -= 1  # lives = 4
print(stages[4])  # Muestra cabeza + cuerpo

# ... y así sucesivamente
```

**❓ ¿Por qué usar el número de vidas como índice directo?**
```python
# Opción 1: Nuestra opción (usar lives como índice)
print(stages[lives])
# ✅ Una línea, directo, elegante

# Opción 2: Calcular el índice
index = 6 - lives
print(stages[index])
# ❌ Cálculo innecesario
# ❌ Más propenso a errores

# Opción 3: If/elif para cada caso
if lives == 6:
    print(stages[6])
elif lives == 5:
    print(stages[5])
# ... etc
# ❌ 7 condiciones en lugar de 1 línea
# ❌ Extremadamente verboso

# Opción 4: Diccionario
stage_map = {6: stages[6], 5: stages[5], ...}
print(stage_map[lives])
# ❌ Estructura extra innecesaria
```

**✅ Es brillante usar el número de vidas como índice directo.**

---

### **Desglose del arte ASCII en `stages`:**
```python
stages = [
    # stages[0] - 0 vidas restantes (PERDISTE)
    '''
       --------
       |      |
       |      O      ← Cabeza
       |     \\|/    ← Cuerpo + ambos brazos
       |      |      ← Torso
       |     / \\    ← Ambas piernas
       -
    ''',
    
    # stages[1] - 1 vida restante
    '''
       --------
       |      |
       |      O      ← Cabeza
       |     \\|/    ← Cuerpo + ambos brazos
       |      |      ← Torso
       |     /       ← Solo pierna izquierda
       -
    ''',
    
    # stages[2] - 2 vidas restantes
    '''
       --------
       |      |
       |      O      ← Cabeza
       |     \\|/    ← Cuerpo + ambos brazos
       |      |      ← Torso
       |             ← Sin piernas
       -
    ''',
    
    # stages[3] - 3 vidas restantes
    '''
       --------
       |      |
       |      O      ← Cabeza
       |     \\|     ← Cuerpo + brazo izquierdo
       |      |      ← Torso
       |             ← Sin piernas
       -
    ''',
    
    # stages[4] - 4 vidas restantes
    '''
       --------
       |      |
       |      O      ← Cabeza
       |      |      ← Solo cuerpo
       |      |      ← Torso
       |             ← Sin extremidades
       -
    ''',
    
    # stages[5] - 5 vidas restantes
    '''
       --------
       |      |
       |      O      ← Solo cabeza
       |             ← Sin cuerpo
       |             
       |             
       -
    ''',
    
    # stages[6] - 6 vidas restantes (INICIO)
    '''
       --------
       |      |      ← Solo la horca
       |             ← Vacío
       |             
       |             
       |             
       -
    '''
]
```

**Notas sobre el arte ASCII:**
- `\` necesita `\\` en Python (escape character)
- Los espacios mantienen la alineación
- Las comillas triples `'''` permiten múltiples líneas

---

## 📊 RESUMEN DE DECISIONES DE DISEÑO

| Pregunta | Decisión | Por qué |
|----------|----------|---------|
| ¿Qué loop usar? | `while` | No sabemos cuántas iteraciones |
| ¿Cómo detectar letras repetidas? | Lista `guessed_letters` | Necesitamos histórico completo |
| ¿Cómo mostrar progreso? | Lista `correct_letters` | Para reconstruir display |
| ¿Cuándo reconstruir display? | Cada vuelta del loop | Más simple que actualizar parcial |
| ¿Cómo verificar victoria? | `"_" not in display` | Más intuitivo |
| ¿Cómo saltar iteración? | `continue` | Más limpio que anidar |
| ¿Cómo mostrar dibujo? | `stages[lives]` | Índice directo, elegante |
| ¿Cómo convertir input? | `.lower()` | Case-insensitive |
| ¿Cómo elegir palabra? | `random.choice()` | Una línea, Pythonico |

---

## 🎓 CONCEPTOS CLAVE APRENDIDOS

### **1. Listas para guardar estado**
```python
correct_letters = []  # Letras correctas
guessed_letters = []  # Todas las letras intentadas
```
**Uso:** Mantener información entre iteraciones del loop.

---

### **2. Banderas booleanas**
```python
game_over = False
while not game_over:
    # ...
    if lives == 0:
        game_over = True  # Cambia la bandera para terminar
```
**Uso:** Controlar cuándo termina un loop.

---

### **3. Loops condicionales**
```python
while not game_over:  # Mientras una condición sea verdad
    # código
```
**Vs:**
```python
for i in range(10):  # Cantidad específica de veces
    # código
```

---

### **4. Reconstrucción iterativa**
```python
# En cada vuelta del loop:
display = ""  # Empezar de cero
for letter in chosen_word:
    # Reconstruir todo el display
```
**Principio:** A veces es más fácil reconstruir que actualizar parcialmente.

---

### **5. Operadores de pertenencia**
```python
"a" in "casa"      # True (sí está)
"z" in "casa"      # False (no está)
"a" not in "casa"  # False (sí está)
"z" not in "casa"  # True (no está)
```
**Uso:** Verificar si un elemento existe en una secuencia.

---

### **6. Control de flujo**
```python
if condition1:
    # código
elif condition2:  # Solo se ejecuta si condition1 es False
    # código
else:  # Solo se ejecuta si todas son False
    # código

continue  # Salta al inicio del loop
break     # Sale completamente del loop
```

---

### **7. Strings inmutables**
```python
# Strings NO se pueden modificar directamente
palabra = "casa"
# palabra[0] = "p"  # ❌ ERROR

# En su lugar, construimos nuevos strings
display = ""
display += "c"  # display = "c"
display += "a"  # display = "ca"
```

---

### **8. F-strings (formateo moderno)**
```python
nombre = "Ana"
edad = 25

# Forma moderna (Python 3.6+)
print(f"Hola {nombre}, tienes {edad} años")

# Forma antigua
print("Hola " + nombre + ", tienes " + str(edad) + " años")
```

---

### **9. Operadores de asignación compuestos**
```python
x = 10
x += 5   # x = x + 5  → x = 15
x -= 3   # x = x - 3  → x = 12
x *= 2   # x = x * 2  → x = 24
x /= 4   # x = x / 4  → x = 6.0
```

---

### **10. Listas como índices**
```python
stages = ["dibujo0", "dibujo1", "dibujo2", ...]
lives = 3

# Usar una variable como índice
print(stages[lives])  # Muestra stages[3]
```
**Principio:** Las listas pueden indexarse con variables, no solo números fijos.

---

## 🔍 CONCEPTOS AVANZADOS

### **¿Por qué `display += letter` funciona?**
```python
display = ""
display += "c"  # Internamente: display = display + "c"
display += "a"  # Internamente: display = display + "a"
# display = "ca"
```

**Aunque los strings son inmutables, `+=` crea un nuevo string cada vez:**
```python
# Lo que realmente pasa:
display = ""          # ID en memoria: 001
display = "" + "c"    # Crea nuevo string, ID: 002
display = "c" + "a"   # Crea nuevo string, ID: 003
# El ID cambia, pero usamos el mismo nombre de variable
```

---

### **¿Por qué usar `.append()` para listas pero `+=` para strings?**
```python
# Listas (mutables)
lista = []
lista.append("a")  # Modifica la lista existente
# ID en memoria: 100 (no cambia)

# Strings (inmutables)
texto = ""
texto += "a"  # Crea un nuevo string
# ID en memoria: cambia de 200 a 201
```

**Principio:**
- Objetos mutables (listas): se modifican en su lugar
- Objetos inmutables (strings): se crean nuevos cada vez

---

### **¿Por qué el orden de las condiciones if/elif/else importa?**
```python
# ✅ CORRECTO
if letter == guess:
    display += letter
elif letter in correct_letters:
    display += letter
else:
    display += "_"

# ❌ INCORRECTO (orden cambiado)
if letter in correct_letters:  # Se ejecuta primero
    display += letter
elif letter == guess:  # Nunca se ejecuta si la letra ya está en correct_letters
    correct_letters.append(guess)  # ¡No se agrega!
```

**Principio:** En `if/elif/else`, solo se ejecuta la PRIMERA condición verdadera.

---

## 💡 TRUCOS Y BUENAS PRÁCTICAS

### **1. Nombra variables descriptivamente**
```python
# ❌ MAL
l = []
cl = []
gl = []

# ✅ BIEN
lives = 6
correct_letters = []
guessed_letters = []
```

---

### **2. Usa espacios en blanco para legibilidad**
```python
# ❌ MAL
if guess in guessed_letters:print("Ya intentaste esa");continue

# ✅ BIEN
if guess in guessed_letters:
    print("Ya intentaste esa")
    continue
```

---

### **3. Agrupa código relacionado**
```python
# ✅ BIEN
# Configuración inicial
lives = 6
game_over = False
correct_letters = []
guessed_letters = []

# Elegir palabra
chosen_word = random.choice(word_list)

# Loop principal
while not game_over:
    # ...
```

---

### **4. Comenta el "por qué", no el "qué"**
```python
# ❌ MAL (obvio)
lives -= 1  # Resta 1 a lives

# ✅ BIEN (explica por qué)
lives -= 1  # Jugador falló, pierde una vida
```

---

### **5. Usa constantes para valores "mágicos"**
```python
# ❌ MAL
lives = 6
if lives == 0:
    # ...

# ✅ MEJOR
MAX_LIVES = 6
lives = MAX_LIVES
if lives == 0:
    # ...
```

---

## 🎯 EJERCICIOS PARA PRACTICAR

### **Ejercicio 1: Modificar vidas iniciales**
Cambia el juego para que empiece con 10 vidas en lugar de 6.

**Pista:** Solo necesitas cambiar 2 líneas.

---

### **Ejercicio 2: Mostrar letras intentadas**
Después de cada intento, muestra todas las letras que el jugador ya intentó.

**Pista:** Usa `guessed_letters` y `print()`.

---

### **Ejercicio 3: Validar input**
Haz que el juego solo acepte letras individuales (rechaza números, palabras completas, etc.)

**Pista:** Usa `len(guess)` y `.isalpha()`.

---

### **Ejercicio 4: Contador de puntos**
Agrega un sistema de puntos:
- +10 puntos por letra correcta
- -5 puntos por letra incorrecta
- Muestra el puntaje final

---

### **Ejercicio 5: Modo difícil**
Crea un modo donde no se muestran las vidas restantes (solo el dibujo).

---

## 🔗 RECURSOS ADICIONALES

- [Python Official Documentation - Strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Python Official Documentation - Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Official Documentation - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python - Python while Loops](https://realpython.com/python-while-loop/)
- [Real Python - Python Lists and Tuples](https://realpython.com/python-lists-tuples/)

---

## 📌 REPASO RÁPIDO

Si vuelves a este documento después de un tiempo, empieza por aquí:

1. **¿Cómo funciona el loop principal?**
   - `while not game_over` repite hasta que `game_over` sea `True`

2. **¿Cómo se construye el display?**
   - Recorre cada letra de la palabra secreta
   - Compara con las letras adivinadas
   - Muestra letra o `_` según corresponda

3. **¿Por qué dos listas?**
   - `correct_letters`: para construir el display
   - `guessed_letters`: para evitar repeticiones

4. **¿Cómo se determina victoria/derrota?**
   - Victoria: `"_" not in display`
   - Derrota: `lives == 0`

5. **¿Cómo funciona `stages[lives]`?**
   - Usa el número de vidas como índice directo
   - Menos vidas = índice menor = dibujo más completo

---

## 🎉 CONCLUSIÓN

Este juego de Hangman es un excelente ejemplo de:
- Gestión de estado con variables
- Control de flujo con loops y condicionales
- Manipulación de strings y listas
- Diseño de experiencia de usuario (UX)

**Recuerda:** No necesitas memorizarlo todo. Con práctica, estos patrones se volverán naturales.

**¡Sigue programando y experimentando!** 💪🚀

---

**Última actualización:** [Tu fecha aquí]
**Versión:** 1.0
**Autor:** [Tu nombre aquí]
