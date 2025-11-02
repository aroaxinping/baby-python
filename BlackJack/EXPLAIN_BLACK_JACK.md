# 🃏 Blackjack en Python 

## 📋 Índice
1. [Introducción](#introducción)
2. [¿Cómo funciona el Blackjack?](#cómo-funciona-el-blackjack)
3. [Explicación del Código](#explicación-del-código)
4. [Conclusiones del Proyecto](#conclusiones-del-proyecto)
5. [Guía Rápida de Conceptos](#guía-rápida-de-conceptos)

---

## Introducción

Este proyecto implementa el juego de Blackjack (21) en Python. Es ideal para principiantes porque cubre conceptos fundamentales de programación: funciones, listas, condicionales, bucles y lógica de juego.

**Conceptos clave:** Funciones, listas, bucles while, condicionales if/elif/else, imports

---

## ¿Cómo funciona el Blackjack?

### Objetivo del juego
Conseguir **21 puntos** o acercarse lo máximo posible **sin pasarse**.

### Reglas básicas
1. **Inicio:** Jugador y dealer reciben 2 cartas cada uno
2. **Visibilidad:** El jugador ve sus 2 cartas + solo 1 carta del dealer
3. **Turno del jugador:** Decide si pedir más cartas o plantarse
4. **Turno del dealer:** Automático - debe pedir carta si tiene menos de 17 puntos
5. **Ganador:** Quien esté más cerca de 21 sin pasarse

### Valores de las cartas
- Cartas del 2 al 9: Valen su número
- J, Q, K (representadas como 10): Valen 10 puntos
- **As (11):** Vale 11 o 1 según convenga (se ajusta automáticamente)

### Ejemplos de manos
```
Mano 1: [10, 7] = 17 puntos
Mano 2: [11, 10] = 21 puntos (¡BLACKJACK!)
Mano 3: [11, 10, 5] = 16 puntos (As cambia a 1: 1+10+5)
Mano 4: [10, 9, 5] = 24 puntos (¡Te pasaste! Pierdes)
```

---

## Explicación del Código

### 1. Importar Herramientas

```python
import random
from art import logo
```

**¿Qué hace?**
- `import random`: Importa el módulo para generar números/elecciones aleatorias
- `from art import logo`: Importa un logo decorativo (opcional - puedes omitirlo si no tienes el paquete `art`)

**Analogía:** Como sacar las herramientas de tu caja antes de empezar un proyecto.

---

### 2. Función: Dar una Carta

```python
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
```

**Desglose línea por línea:**

| Línea | Código | Explicación |
|-------|--------|-------------|
| 1 | `def deal_card():` | Define una función llamada `deal_card` que no necesita parámetros |
| 2 | `"""Returns..."""` | Docstring (comentario de documentación) que explica qué hace la función |
| 3 | `cards = [...]` | Crea una lista con todas las cartas posibles. Hay cuatro 10s (J, Q, K, 10) |
| 4 | `card = random.choice(cards)` | Elige una carta aleatoria de la lista usando `random.choice()` |
| 5 | `return card` | Devuelve la carta seleccionada para usarla fuera de la función |

**Ejemplo de uso:**
```python
mi_carta = deal_card()  # Podría devolver: 7
otra_carta = deal_card()  # Podría devolver: 10
```

**Concepto clave:** Esta función es **reutilizable** - puedes llamarla cuantas veces quieras para obtener cartas diferentes.

---

### 3. Función: Calcular Puntos (La más importante)

```python
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
```

Esta función tiene **tres secciones importantes:**

#### Sección 1: Detectar Blackjack

```python
if sum(cards) == 21 and len(cards) == 2:
    return 0
```

| Elemento | Explicación |
|----------|-------------|
| `sum(cards)` | Suma todos los números de la lista |
| `len(cards)` | Cuenta cuántos elementos hay en la lista |
| `== 21` | Verifica si la suma es exactamente 21 |
| `and` | Operador lógico - ambas condiciones deben ser verdaderas |
| `return 0` | Devuelve 0 como código especial para "Blackjack perfecto" |

**Ejemplos:**
```python
calculate_score([11, 10])  # Suma 21 con 2 cartas → return 0 (¡Blackjack!)
calculate_score([7, 7, 7])  # Suma 21 con 3 cartas → NO es blackjack, continúa
```

**¿Por qué devuelve 0?** Es una convención del código: 0 representa un Blackjack perfecto (21 con 2 cartas), que es la mejor mano posible.

#### Sección 2: Ajustar el As (11 → 1)

```python
if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
```

| Línea | Explicación |
|-------|-------------|
| `if 11 in cards` | Verifica si hay un As (11) en la lista de cartas |
| `and sum(cards) > 21` | Y además verifica si te pasaste de 21 |
| `cards.remove(11)` | Elimina el primer 11 que encuentre en la lista |
| `cards.append(1)` | Añade un 1 al final de la lista |

**Paso a paso con ejemplo:**
```python
# Estado inicial
cards = [11, 10, 7]
sum(cards) = 28  # ¡Te pasaste!

# Después del ajuste
cards.remove(11)  # cards = [10, 7]
cards.append(1)   # cards = [10, 7, 1]
sum(cards) = 18   # ¡Salvado!
```

**Concepto clave:** El As es una carta especial que puede valer 11 o 1. El código cambia automáticamente su valor cuando te conviene.

#### Sección 3: Devolver el puntaje final

```python
return sum(cards)
```

Si no se cumplieron las condiciones anteriores, simplemente suma todas las cartas y devuelve el total.

---

### 4. Función: Comparar Resultados

```python
def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"
```

**Estructura:** Esta es una **cadena de condiciones** que evalúa en orden. La primera que sea verdadera se ejecuta y sale de la función.

| Condición | Significado | Resultado |
|-----------|-------------|-----------|
| `u_score == c_score` | Ambos tienen los mismos puntos | Empate |
| `c_score == 0` | El dealer tiene Blackjack (21 con 2 cartas) | Pierdes |
| `u_score == 0` | Tú tienes Blackjack | Ganas |
| `u_score > 21` | Te pasaste de 21 | Pierdes automáticamente |
| `c_score > 21` | El dealer se pasó | Ganas automáticamente |
| `u_score > c_score` | Tienes más puntos (sin pasarte) | Ganas |
| `else` | Ninguna anterior (dealer tiene más puntos) | Pierdes |

**Ejemplo de evaluación:**
```python
compare(18, 20)
# ¿18 == 20? NO
# ¿20 == 0? NO (no es blackjack)
# ¿18 == 0? NO
# ¿18 > 21? NO
# ¿20 > 21? NO
# ¿18 > 20? NO
# else → "You lose 😤"
```

**Concepto clave:** Las condiciones se evalúan de **arriba hacia abajo**. El orden importa porque algunas son más prioritarias (como detectar Blackjack antes que comparar puntos).

---

### 5. Función Principal: El Juego Completo

```python
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
```

#### Inicialización de Variables

| Variable | Tipo | Valor Inicial | Propósito |
|----------|------|---------------|-----------|
| `user_cards` | Lista | `[]` (vacía) | Almacena las cartas del jugador |
| `computer_cards` | Lista | `[]` (vacía) | Almacena las cartas del dealer |
| `user_score` | Entero | `-1` | Puntos del jugador (aún no calculados) |
| `computer_score` | Entero | `-1` | Puntos del dealer (aún no calculados) |
| `is_game_over` | Booleano | `False` | Controla si el juego ha terminado |

**Concepto:** `is_game_over` es una **bandera (flag)** - una variable booleana que controla el flujo del programa.

---

#### Repartir Cartas Iniciales

```python
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
```

**Desglose:**

| Elemento | Explicación |
|----------|-------------|
| `for _ in range(2):` | Bucle que se repite exactamente 2 veces |
| `_` | Variable "desechable" - no la usamos, solo queremos repetir |
| `range(2)` | Genera la secuencia [0, 1] - dos iteraciones |
| `.append(deal_card())` | Llama a `deal_card()` y añade el resultado a la lista |

**Resultado después del bucle:**
```python
user_cards = [7, 10]        # Ejemplo
computer_cards = [5, 11]    # Ejemplo
```

**Concepto:** `.append()` es un método que añade elementos al final de una lista.

---

#### Bucle Principal: Turno del Jugador

```python
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
```

**Explicación del `while`:**

| Elemento | Significado |
|----------|-------------|
| `while` | Bucle que se repite mientras la condición sea verdadera |
| `not is_game_over` | "mientras el juego NO haya terminado" |
| Equivale a | `while is_game_over == False:` |

**Calcular y mostrar información:**
```python
user_score = calculate_score(user_cards)
```
- Llama a la función `calculate_score()` con las cartas del usuario
- Guarda el resultado en `user_score`

```python
print(f"Your cards: {user_cards}, current score: {user_score}")
```
- `f"..."` es un **f-string** - permite insertar variables dentro del texto usando `{}`
- Muestra: `Your cards: [7, 10], current score: 17`

```python
print(f"Computer's first card: {computer_cards[0]}")
```
- `computer_cards[0]` accede al **primer elemento** de la lista (índice 0)
- Solo muestra 1 carta del dealer (regla del Blackjack)

---

#### Condiciones para Terminar el Turno

```python
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
```

**El juego termina cuando:**

| Condición | Significado | Razón |
|-----------|-------------|-------|
| `user_score == 0` | Tienes Blackjack | Ganaste automáticamente |
| `computer_score == 0` | Dealer tiene Blackjack | Perdiste automáticamente |
| `user_score > 21` | Te pasaste de 21 | Perdiste automáticamente |
| `or` | Si CUALQUIERA es verdad | El juego debe terminar |

**Cuando `is_game_over = True`:** El bucle `while` termina y pasa al turno del dealer.

---

#### Decisión del Jugador

```python
else:
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == "y":
        user_cards.append(deal_card())
    else:
        is_game_over = True
```

**Flujo de decisión:**

1. `input()` pausa el programa y espera que el usuario escriba algo
2. La respuesta se guarda en `user_should_deal`
3. Si es `"y"`: añade una carta nueva a `user_cards`
4. Si es cualquier otra cosa: termina el juego (`is_game_over = True`)

**Ejemplo de ejecución:**
```
Tu entrada: "y"
→ user_cards.append(deal_card())  # Añade carta
→ El while vuelve a empezar

Tu entrada: "n"
→ is_game_over = True  # Termina el while
```

---

#### Turno del Dealer (Automático)

```python
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
```

**Regla del Casino:**

| Condición | Explicación |
|-----------|-------------|
| `computer_score != 0` | No tiene Blackjack |
| `and` | Y además... |
| `computer_score < 17` | Tiene menos de 17 puntos |
| **Acción** | Debe pedir carta obligatoriamente |

**Paso a paso:**
```python
# Estado inicial
computer_cards = [5, 10]  # 15 puntos
computer_score = 15

# Primera iteración
15 < 17 → TRUE → Pide carta
computer_cards = [5, 10, 8]  # 23 puntos
computer_score = 23

# Segunda iteración
23 < 17 → FALSE → Sale del bucle
```

**Concepto:** El dealer no "decide" - sigue reglas fijas del casino.

---

#### Mostrar Resultados Finales

```python
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
```

1. Muestra todas las cartas y puntos finales del jugador
2. Muestra todas las cartas y puntos finales del dealer
3. Llama a `compare()` para determinar el ganador y mostrar el mensaje

---

### 6. Bucle Principal del Programa

```python
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
```

**¿Cómo funciona?**

| Elemento | Explicación |
|----------|-------------|
| `while ... == "y"` | Mientras la respuesta sea "y", repite |
| `input("...")` | Pregunta al usuario y captura su respuesta |
| `print("\n" * 20)` | Imprime 20 saltos de línea (efecto de "limpiar pantalla") |
| `play_game()` | Llama a la función principal - inicia una partida nueva |

**Flujo completo:**
```
1. Pregunta: "¿Quieres jugar?"
   ├─ Usuario escribe "y" → Continúa
   └─ Usuario escribe "n" → Programa termina

2. Si continúa:
   ├─ Limpia pantalla visualmente
   └─ Inicia juego con play_game()

3. Cuando termina el juego, vuelve al paso 1
```

**Concepto:** Este bucle permite **jugar múltiples partidas** sin reiniciar el programa.

---

## Conclusiones del Proyecto

### ¿Qué aprendí con este proyecto?

#### 1. **Estructura de un Programa Completo**
- **Importaciones** al inicio
- **Funciones** que dividen el código en tareas específicas
- **Función principal** que coordina todo
- **Bucle de control** para repetir el programa

#### 2. **Trabajo con Funciones**
- Crear funciones con `def nombre():`
- Pasar información a funciones (parámetros)
- Devolver resultados con `return`
- Reutilizar código llamando funciones múltiples veces

#### 3. **Manipulación de Listas**
- Crear listas vacías: `lista = []`
- Añadir elementos: `lista.append(elemento)`
- Eliminar elementos: `lista.remove(elemento)`
- Acceder a elementos: `lista[0]` (primer elemento)
- Sumar todos los elementos: `sum(lista)`
- Contar elementos: `len(lista)`
- Verificar si existe un elemento: `elemento in lista`

#### 4. **Control de Flujo Avanzado**
- Bucles `while` con condiciones complejas
- Cadenas de `if/elif/else` para múltiples casos
- Uso de operadores lógicos: `and`, `or`, `not`
- Banderas (flags) para controlar bucles

#### 5. **Lógica de Juegos**
- Implementar reglas complejas en código
- Turnos de jugadores (humano vs computadora)
- Comparación de resultados
- Manejo de casos especiales (Blackjack, pasarse de 21)

#### 6. **Aleatoriedad**
- Usar `random.choice()` para selecciones aleatorias
- Simular comportamiento impredecible (cartas)

### Habilidades Transferibles

Este proyecto te prepara para:
- **Data Analysis:** Manipulación de listas es fundamental para trabajar con DataFrames en Pandas
- **Scripting:** Estructura de funciones reutilizables
- **Debugging:** Seguir el flujo lógico de un programa complejo
- **Pensamiento Algorítmico:** Traducir reglas del mundo real a código

### Lo Más Importante

**No necesitas memorizar la sintaxis** - lo importante es entender:
1. **Qué hace cada parte del código** (propósito)
2. **Por qué está organizado así** (estructura)
3. **Cómo las partes interactúan** (flujo)

Con la práctica, la sintaxis se vuelve natural. Lo difícil es la **lógica**, y eso solo se aprende **haciendo proyectos**.

---

## Guía Rápida de Conceptos

### 📚 Imports y Módulos

```python
import random
```

**¿Qué es?** Trae funcionalidades externas al programa.

**Uso común:**
```python
import random          # Aleatoridad
import datetime        # Fechas y horas
from modulo import funcion  # Importar función específica
```

---

### 🔧 Funciones

```python
def nombre_funcion(parametro1, parametro2):
    # Código aquí
    return resultado
```

**Partes:**
- `def`: Palabra clave para definir función
- `nombre_funcion`: Nombre descriptivo en snake_case
- `(parametros)`: Información que necesita (opcional)
- `return`: Lo que devuelve (opcional)

**Ejemplo:**
```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)  # resultado = 8
```

---

### 📋 Listas

```python
mi_lista = [1, 2, 3, 4, 5]
```

**Operaciones comunes:**

| Operación | Código | Resultado |
|-----------|--------|-----------|
| Crear vacía | `lista = []` | `[]` |
| Añadir al final | `lista.append(6)` | `[1, 2, 3, 4, 5, 6]` |
| Eliminar elemento | `lista.remove(3)` | `[1, 2, 4, 5, 6]` |
| Acceder por índice | `lista[0]` | `1` (primer elemento) |
| Sumar todos | `sum(lista)` | `18` |
| Contar elementos | `len(lista)` | `5` |
| Verificar existencia | `3 in lista` | `True` o `False` |

**Índices:**
```python
lista = ['a', 'b', 'c', 'd']
#        0    1    2    3    ← Índices
#       -4   -3   -2   -1    ← Índices negativos (desde el final)

lista[0]   # 'a'
lista[-1]  # 'd' (último elemento)
```

---

### 🔁 Bucle `while`

```python
while condicion:
    # Código que se repite
```

**Funcionamiento:**
1. Evalúa la condición
2. Si es `True`: ejecuta el bloque y vuelve al paso 1
3. Si es `False`: sale del bucle

**Ejemplo:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Aumenta en 1

# Imprime: 0, 1, 2, 3, 4
```

---

### 🔁 Bucle `for`

```python
for variable in secuencia:
    # Código que se repite
```

**Uso común:**
```python
for i in range(5):        # Repite 5 veces (0, 1, 2, 3, 4)
    print(i)

for carta in cartas:      # Recorre cada elemento
    print(carta)
```

---

### 🔀 Condicionales

```python
if condicion1:
    # Si condicion1 es True
elif condicion2:
    # Si condicion1 es False y condicion2 es True
else:
    # Si ninguna anterior es True
```

**Operadores de comparación:**
- `==` igual a
- `!=` diferente de
- `>` mayor que
- `<` menor que
- `>=` mayor o igual
- `<=` menor o igual

**Operadores lógicos:**
- `and` (y) - Ambas deben ser True
- `or` (o) - Al menos una debe ser True
- `not` (no) - Invierte el valor

**Ejemplos:**
```python
if edad >= 18 and tiene_licencia:
    print("Puede conducir")

if puntos > 21 or puntos < 0:
    print("Puntuación inválida")

if not es_fin_de_semana:
    print("A trabajar")
```

---

### 🎲 Aleatoriedad con `random`

```python
import random

random.choice([1, 2, 3, 4, 5])      # Elige uno al azar
random.randint(1, 10)                # Número entero entre 1 y 10
random.shuffle(lista)                # Mezcla la lista
```

---

### 📝 F-strings (Formatted Strings)

```python
nombre = "Ana"
edad = 25

# Forma antigua
print("Hola " + nombre + ", tienes " + str(edad) + " años")

# F-string (recomendado)
print(f"Hola {nombre}, tienes {edad} años")
```

**Ventajas:**
- Más legible
- Permite expresiones dentro de `{}`
- No necesitas convertir tipos

```python
print(f"2 + 2 = {2 + 2}")  # Imprime: 2 + 2 = 4
```

---

### 🚩 Variables Booleanas (Flags)

```python
is_game_over = False
has_permission = True
```

**Uso común:** Controlar bucles y condiciones

```python
while not is_game_over:
    # Jugar
    if puntos > 21:
        is_game_over = True
```

---

### 📊 Métodos de Listas más Usados

```python
lista = [3, 1, 4, 1, 5]

lista.append(9)      # Añade al final → [3, 1, 4, 1, 5, 9]
lista.remove(1)      # Elimina primer 1 → [3, 4, 1, 5, 9]
lista.pop()          # Elimina último → [3, 4, 1, 5]
lista.sort()         # Ordena → [1, 3, 4, 5]
lista.reverse()      # Invierte → [5, 4, 3, 1]
lista.clear()        # Vacía lista → []
```

---

### 🔍 Funciones Built-in Útiles

```python
sum([1, 2, 3])           # 6 - Suma elementos
len([1, 2, 3])           # 3 - Cuenta elementos
max([1, 2, 3])           # 3 - Valor máximo
min([1, 2, 3])           # 1 - Valor mínimo
sorted([3, 1, 2])        # [1, 2, 3] - Devuelve lista ordenada
range(5)                 # 0, 1, 2, 3, 4 - Secuencia de números
input("Pregunta: ")      # Pide input al usuario
print("Texto")           # Imprime en consola
```

---

