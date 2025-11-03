# 🎮 Number Guessing Game

## 📝 Descripción del Proyecto

Un juego interactivo de adivinanza de números donde el jugador debe adivinar un número aleatorio entre 1 y 100. El juego ofrece dos niveles de dificultad y proporciona pistas al jugador después de cada intento.

---

## 🎯 Objetivos de Aprendizaje

Este proyecto fue diseñado para practicar:
- Variables globales y constantes
- Funciones y retorno de valores
- Condicionales (`if`, `elif`, `else`)
- Bucles (`while`)
- Manejo de input del usuario
- Generación de números aleatorios con `random`
- Lógica de flujo de programa

---

## 🎲 Lógica del Juego

### Flujo Principal

```
INICIO
  ↓
1. Mostrar bienvenida
  ↓
2. Pedir nivel de dificultad (easy/hard)
  ↓
3. Asignar número de intentos según nivel
   - Easy: 10 intentos
   - Hard: 5 intentos
  ↓
4. Generar número secreto aleatorio (1-100)
  ↓
5. BUCLE DE JUEGO (mientras haya intentos Y no haya ganado):
   │
   ├─ Pedir al jugador que adivine
   ├─ Comparar con número secreto
   ├─ Dar pista (too high / too low / correcto)
   ├─ Restar 1 intento
   └─ Volver al inicio del bucle
  ↓
6. FIN DEL JUEGO
   - Si ganó: Felicitar
   - Si perdió: Mostrar el número correcto
  ↓
FIN
```

### Diagrama de Decisión

```
¿El jugador adivinó?
    ├─ SÍ → ¡Victoria! �
    └─ NO → ¿Su número es mayor que el secreto?
            ├─ SÍ → "Too high" 📉
            └─ NO → "Too low" 📈
```

---

## 🐛 Errores y Sus Soluciones

### Error #1: `random.choice in range()`

#### ❌ Código Incorrecto
```python
number = random.choice in range(1, 101)
```

#### ❓ Problema
- Falta paréntesis en `choice()`
- `choice()` no funciona directamente con `range()`
- Sintaxis incorrecta con `in`

#### ✅ Solución
```python
number = random.randint(1, 100)
```

#### 💡 Explicación
`random.randint(a, b)` genera un número entero aleatorio entre `a` y `b` (inclusive). Es la forma más directa para este caso.

**Alternativa válida:**
```python
number = random.choice(list(range(1, 101)))
```
Pero es innecesariamente complejo.

---

### Error #2: Input sin convertir

#### ❌ Código Incorrecto
```python
guess = input("Make a guess: ")
if guess == number:  # Compara string con int
```

#### ❓ Problema
`input()` siempre devuelve un **string** (texto). Comparar `"42"` con `42` siempre será `False`.

#### ✅ Solución
```python
guess = int(input("Make a guess: "))
```

#### 💡 Mejor práctica con manejo de errores
```python
try:
    guess = int(input("Make a guess: "))
except ValueError:
    print("Please enter a valid number!")
```

---

### Error #3: Comparaciones invertidas

#### ❌ Código Incorrecto
```python
if guess < number:
    print("too high")  # ¡Al revés!
elif guess > number:
    print("too low")   # ¡Confuso!
```

#### ❓ Problema
Si el jugador adivina **20** y el número secreto es **50**:
- Su número (20) es MENOR que el secreto (50)
- Debería decir "too low" (sube tu número)
- Pero el código dice "too high" ❌

#### ✅ Solución
```python
if guess > number:
    print("Too high.")   # Tu número es demasiado grande
else:
    print("Too low.")    # Tu número es demasiado pequeño
```
---

### Error #4: Orden lógico del código

#### ❌ Código Incorrecto
```python
def guess(number):
    guess = input("Make a guess: ")
    # hacer comparación...
    
    level = input("What level?")  # ¡Después de jugar!
    if level == "easy":
        attempts = 10
```

#### ❓ Problema
- Se pide el nivel **DESPUÉS** de intentar adivinar
- No tiene sentido lógico
- El flujo está desordenado

#### ✅ Orden correcto
```python
# 1. Configuración (nivel, intentos)
level = input("Choose difficulty: ")
attempts = 10 if level == "easy" else 5

# 2. Generar número
secret_number = choose_number()

# 3. Jugar (bucle de intentos)
while attempts > 0:
    guess = int(input("Make a guess: "))
    # comparar...
```

#### 💡 Regla de oro
**Configuración → Acción → Resultado**

---

### Error #5: Sin bucle de repetición

#### ❌ Código Incorrecto
```python
def guess(number):
    guess = input("Make a guess: ")
    if guess == number:
        print("You guessed it!")
    # ...solo un intento
```

#### ❓ Problema
- El código solo permite **UN** intento
- No hay forma de repetir hasta agotar los intentos

#### ✅ Solución
```python
won = False
while attempts > 0 and not won:
    guess = int(input("Make a guess: "))
    
    if guess == number:
        print("You got it!")
        won = True  # Sale del bucle
    else:
        # dar pistas...
        attempts -= 1
```

#### 💡 Explicación del bucle
- **Condición**: `attempts > 0 and not won`
  - Continúa SI hay intentos disponibles
  - Y SI aún no ha ganado
- **`won = True`**: Bandera para salir del bucle cuando adivine

---

## 🔑 Conceptos Clave para el Futuro

### 1. Variables Globales vs Locales
```python
# Global (disponible en todo el programa)
EASY_LEVEL_ATTEMPTS = 10

def play_game():
    # Local (solo existe dentro de esta función)
    attempts = EASY_LEVEL_ATTEMPTS
```

### 2. Funciones deben hacer UNA cosa
```python
# ✅ BIEN: Función específica
def choose_number():
    return random.randint(1, 100)

# ❌ MAL: Función que hace demasiado
def guess_and_check_and_set_level():
    # ...demasiado complejo
```

### 3. Flujo lógico del programa
```
Entrada → Procesamiento → Salida
```

### 4. Bucles necesitan condición de salida
```python
while condition:  # ¿Cuándo debe parar?
    # código
    # cambiar algo para que eventualmente condition sea False
```

### 5. Siempre validar input del usuario
```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("That's not a number!")
```

---

## 📚 Recursos Útiles

- **`random` module**: https://docs.python.org/3/library/random.html
- **Bucles while**: Continúan mientras la condición sea True
- **Try/Except**: Manejo de errores cuando el usuario escribe cosas inesperadas
- **Operadores de comparación**: `>`, `<`, `==`, `!=`, `>=`, `<=`

---

## 🎓 Checklist de Buenas Prácticas

Antes de dar tu código por terminado, pregúntate:

- [ ] ¿Las funciones tienen nombres descriptivos?
- [ ] ¿Cada función hace solo UNA cosa?
- [ ] ¿El flujo del programa tiene sentido lógico?
- [ ] ¿Hay un bucle para repetir acciones?
- [ ] ¿Validé el input del usuario?
- [ ] ¿Probé el programa con diferentes casos?
- [ ] ¿El código es fácil de leer para otra persona?

---

## 💭 Reflexión Final

### "El código es como hacer una tortilla "

Cuando empiezas a cocinar, es fácil hacer esto:

1. Batir los huevos ✓
2. Freír las patatas ✓
3. ¡Espera! Olvidé pelar las patatas ❌
4. Ah, no tengo sal ❌
5. Ups, la sartén está fría ❌

**El resultado**: Una tortilla extraña con patatas con piel, sin sal, medio cruda.

Lo mismo pasa con el código. Tenía todos los ingredientes correctos:
- ✓ Variables globales (la sal y el aceite)
- ✓ Funciones (los pasos de la receta)
- ✓ Condicionales (saber cuándo darle la vuelta)

Pero lo hcie en el orden equivocado: puse los huevos antes que las patatas, pregunté cuánta sal DESPUÉS de cocinar, y olvidé el fuego del bucle.

### La lección

**Programar no es saber todas las funciones de Python; es saber en qué ORDEN usarlas.**

Es como una receta: no importa si tienes los mejores ingredientes del mundo, si los mezclas en desorden, la tortilla saldrá mal.

> "Un programa es una historia que le cuentas al ordenador. Si empiezas por el final, nadie entenderá nada."

---

**Proyecto completado con ☕️ y muchos `attempts -= 1`**
