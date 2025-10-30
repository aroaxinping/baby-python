# 💕 Love Calculator - Calculadora de Compatibilidad

## 📋 ¿En qué consiste el proyecto?

El **Love Calculator** es un programa de Python que calcula un "puntaje de amor" entre dos personas basándose en sus nombres. Es un ejercicio divertido del curso "100 Days of Code: The Complete Python Pro Bootcamp" de Udemy.

### 🎯 Objetivo del ejercicio:
Practicar:
- Funciones en Python
- Manipulación de strings
- Bucles `for`
- Métodos de strings como `.count()` y `.lower()`
- Conversión de tipos de datos
- Concatenación de strings y números

---

## 🧮 Lógica del Algoritmo

El algoritmo funciona en 4 pasos:

### **Paso 1: Combinar los nombres**
- Toma los dos nombres y los junta en un solo string
- Convierte todo a minúsculas para que no importe si las letras son mayúsculas o minúsculas

**Ejemplo:**
```
"Angela Yu" + "Jack Bauer" = "Angela YuJack Bauer"
→ .lower() →
"angela yujack bauer"
```

---

### **Paso 2: Contar letras de "TRUE"**
- Cuenta cuántas veces aparecen las letras T, R, U, E en los nombres combinados
- Suma todos estos conteos

**Ejemplo con "angela yujack bauer":**
- T = 0
- R = 1 (en "bauer")
- U = 2 (en "yu" y "bauer")
- E = 2 (en "angela" y "bauer")
- **Total TRUE = 0 + 1 + 2 + 2 = 5**

---

### **Paso 3: Contar letras de "LOVE"**
- Cuenta cuántas veces aparecen las letras L, O, V, E en los nombres combinados
- Suma todos estos conteos

**Ejemplo con "angela yujack bauer":**
- L = 1 (en "angela")
- O = 0
- V = 0
- E = 2 (en "angela" y "bauer")
- **Total LOVE = 1 + 0 + 0 + 2 = 3**

---

### **Paso 4: Combinar en número de 2 dígitos**
- El primer dígito es el total de TRUE
- El segundo dígito es el total de LOVE
- Se concatenan como strings y luego se convierten a entero

**Ejemplo:**
```
TRUE = 5, LOVE = 3
→ "5" + "3" = "53"
→ int("53") = 53
```

**Resultado final: 53** 💕

---

## 💻 Las Tres Versiones del Código

### **Versión 1: Sin Loop (Básica)**

```python
def calculate_love_score(name1, name2):
    # Combinar y convertir a minúsculas
    combined = (name1 + name2).lower()
    
    # Contar cada letra de TRUE individualmente
    t = combined.count("t")
    r = combined.count("r")
    u = combined.count("u")
    e = combined.count("e")
    true_total = t + r + u + e
    
    # Contar cada letra de LOVE individualmente
    l = combined.count("l")
    o = combined.count("o")
    v = combined.count("v")
    e2 = combined.count("e")
    love_total = l + o + v + e2
    
    # Combinar y mostrar
    love_score = int(str(true_total) + str(love_total))
    print(love_score)


calculate_love_score("Angela Yu", "Jack Bauer")
```

**✅ Ventajas:**
- Muy fácil de entender
- Cada paso es explícito
- Perfecto para principiantes

**❌ Desventajas:**
- Mucho código repetitivo
- Si quisieras cambiar "TRUE" por otra palabra, tendrías que modificar muchas líneas

---

### **Versión 2: Con For Loop (Recomendada)**

```python
def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    # Loop para contar TRUE
    true_total = 0
    for letter in "true":
        true_total += combined.count(letter)
    
    # Loop para contar LOVE
    love_total = 0
    for letter in "love":
        love_total += combined.count(letter)
    
    # Combinar y mostrar
    love_score = int(str(true_total) + str(love_total))
    print(love_score)


calculate_love_score("Angela Yu", "Jack Bauer")
```

**✅ Ventajas:**
- Código más corto y elegante
- Usa loops (concepto importante en programación)
- Más fácil de modificar
- Menos repetición

**❌ Desventajas:**
- Requiere entender cómo funcionan los loops

**🔍 Explicación del loop:**
```python
for letter in "true":
    true_total += combined.count(letter)
```

Esto hace:
1. **Vuelta 1:** `letter = "t"` → cuenta "t" en combined → suma al total
2. **Vuelta 2:** `letter = "r"` → cuenta "r" en combined → suma al total
3. **Vuelta 3:** `letter = "u"` → cuenta "u" en combined → suma al total
4. **Vuelta 4:** `letter = "e"` → cuenta "e" en combined → suma al total

---

### **Versión 3: Con Sum y List Comprehension (Avanzada)**

```python
def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    true_total = sum(combined.count(letter) for letter in "true")
    love_total = sum(combined.count(letter) for letter in "love")
    
    love_score = int(str(true_total) + str(love_total))
    print(love_score)


calculate_love_score("Angela Yu", "Jack Bauer")
```

**✅ Ventajas:**
- Código muy compacto (solo una línea por palabra)
- Estilo "pythónico" profesional
- Muy eficiente

**❌ Desventajas:**
- Puede ser difícil de entender para principiantes
- Combina varios conceptos avanzados

**🔍 Explicación:**
```python
sum(combined.count(letter) for letter in "true")
```

Esto es una **list comprehension** dentro de `sum()`:
- `for letter in "true"` → itera sobre cada letra
- `combined.count(letter)` → cuenta cada letra
- `sum(...)` → suma todos los resultados

Es equivalente a:
```python
combined.count("t") + combined.count("r") + combined.count("u") + combined.count("e")
```

---

## 🎮 Hardcoded Values vs Input Dinámico

### ⚠️ ¿Por qué hay valores hardcoded?

En el ejercicio de Udemy, las instrucciones dicen:

> "Udemy coding exercises do not have a console, so you cannot use `input()`. You will need to call your function with hard-coded values."

**Valor hardcoded** = Valor fijo escrito directamente en el código

```python
calculate_love_score("Angela Yu", "Jack Bauer")  # ← Valores hardcoded
```

Esto significa:
- No puedes pedirle al usuario que escriba los nombres
- Debes poner los nombres directamente en el código
- Es una limitación de la plataforma de Udemy

---

### 🔄 ¿Cómo implementarlo con Input Dinámico?

Si quisieras usar este programa **fuera de Udemy** (en tu computadora, PyCharm, etc.), puedes hacerlo con `input()`:

#### **Opción 1: Input Simple**
```python
def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    true_total = 0
    for letter in "true":
        true_total += combined.count(letter)
    
    love_total = 0
    for letter in "love":
        love_total += combined.count(letter)
    
    love_score = int(str(true_total) + str(love_total))
    print(f"Your love score is: {love_score}")


# Pedir nombres al usuario
nombre1 = input("Enter the first name: ")
nombre2 = input("Enter the second name: ")

# Llamar la función con los inputs
calculate_love_score(nombre1, nombre2)
```

**Ejecución:**
```
Enter the first name: Angela Yu
Enter the second name: Jack Bauer
Your love score is: 53
```

---

#### **Opción 2: Todo en la Función**
```python
def calculate_love_score():
    # Pedir nombres dentro de la función
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    combined = (name1 + name2).lower()
    
    true_total = 0
    for letter in "true":
        true_total += combined.count(letter)
    
    love_total = 0
    for letter in "love":
        love_total += combined.count(letter)
    
    love_score = int(str(true_total) + str(love_total))
    print(f"Your love score is: {love_score}")


# Llamar la función (ya no necesita parámetros)
calculate_love_score()
```

---

#### **Opción 3: Modo Interactivo con Validación**
```python
def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    true_total = sum(combined.count(letter) for letter in "true")
    love_total = sum(combined.count(letter) for letter in "love")
    
    love_score = int(str(true_total) + str(love_total))
    
    print(f"\n💕 Love Calculator 💕")
    print(f"{name1} + {name2}")
    print(f"TRUE score: {true_total}")
    print(f"LOVE score: {love_total}")
    print(f"Your love score is: {love_score}!")
    
    # Interpretación del score
    if love_score < 10 or love_score > 90:
        print("You go together like Coke and Mentos! 💥")
    elif love_score >= 40 and love_score <= 50:
        print("You are alright together. 👍")
    else:
        print("Not bad! 😊")


# Programa principal
print("Welcome to the Love Calculator! 💘")
nombre1 = input("Enter the first name: ")
nombre2 = input("Enter the second name: ")

calculate_love_score(nombre1, nombre2)
```

**Ejecución:**
```
Welcome to the Love Calculator! 💘
Enter the first name: Kanye West
Enter the second name: Kim Kardashian

💕 Love Calculator 💕
Kanye West + Kim Kardashian
TRUE score: 4
LOVE score: 2
Your love score is: 42!
You are alright together. 👍
```

---

## 📊 Comparación: Hardcoded vs Input

| Aspecto | Hardcoded | Input Dinámico |
|---------|-----------|----------------|
| **Flexibilidad** | ❌ Siempre los mismos nombres | ✅ Cualquier nombre |
| **En Udemy** | ✅ Funciona | ❌ No funciona |
| **En PyCharm/VS Code** | ✅ Funciona | ✅ Funciona |
| **Interactividad** | ❌ No es interactivo | ✅ Usuario puede participar |
| **Para testing** | ✅ Perfecto para pruebas | ⚠️ Requiere input manual |

---

## 🚀 Ejemplos de Uso

### **Ejemplo 1: Angela Yu y Jack Bauer**
```python
calculate_love_score("Angela Yu", "Jack Bauer")
# Resultado: 53
```

**Cálculo:**
- Combined: "angela yujack bauer"
- TRUE: t(0) + r(1) + u(2) + e(2) = 5
- LOVE: l(1) + o(0) + v(0) + e(2) = 3
- Score: 53

---

### **Ejemplo 2: Kanye West y Kim Kardashian**
```python
calculate_love_score("Kanye West", "Kim Kardashian")
# Resultado: 42
```

**Cálculo:**
- Combined: "kanye westkim kardashian"
- TRUE: t(1) + r(1) + u(0) + e(2) = 4
- LOVE: l(0) + o(0) + v(0) + e(2) = 2
- Score: 42

---

### **Ejemplo 3: Romeo y Juliet**
```python
calculate_love_score("Romeo", "Juliet")
# Resultado: ** (¡pruébalo tú!)
```

---

## 🎓 Conceptos de Python Aprendidos

### 1. **Funciones**
```python
def calculate_love_score(name1, name2):
    # código aquí
```
- Reutilización de código
- Parámetros y argumentos

### 2. **Métodos de Strings**
```python
.lower()   # Convierte a minúsculas
.count()   # Cuenta ocurrencias
```

### 3. **Bucles For**
```python
for letter in "true":
    # procesar cada letra
```

### 4. **Conversión de Tipos**
```python
str(5)      # 5 → "5"
int("53")   # "53" → 53
```

### 5. **Concatenación**
```python
"5" + "3"           # Strings → "53"
"name1" + "name2"   # Concatenar texto
```

### 6. **Operador +=**
```python
total += 1  # Equivalente a: total = total + 1
```

### 7. **F-strings (opcional)**
```python
print(f"Score: {love_score}")
```

---

## 💡 Consejos y Mejores Prácticas

### ✅ DO (Hacer):
- Usa `.lower()` para que las mayúsculas no importen
- Usa loops para evitar código repetitivo
- Nombra tus variables de forma descriptiva
- Prueba tu código con diferentes nombres

### ❌ DON'T (No hacer):
- No usar `input()` en Udemy (no funciona)
- No olvidar convertir a `int()` al final
- No contar la letra "e" dos veces por error
- No asumir que todos los nombres tienen las mismas letras

---

## 🐛 Problemas Comunes y Soluciones

### **Problema 1: El score es un string en lugar de un número**
```python
# ❌ Incorrecto
love_score = str(true_total) + str(love_total)
print(love_score)  # Resultado: "53" (string)

# ✅ Correcto
love_score = int(str(true_total) + str(love_total))
print(love_score)  # Resultado: 53 (número)
```

---

### **Problema 2: Las mayúsculas afectan el conteo**
```python
# ❌ Incorrecto
combined = name1 + name2
# "Angela" tiene "A" pero .count("a") no lo encuentra

# ✅ Correcto
combined = (name1 + name2).lower()
# Ahora todo está en minúsculas
```

---

### **Problema 3: Olvidar el `print()`**
```python
# ❌ No verás ningún resultado
def calculate_love_score(name1, name2):
    love_score = int(str(true_total) + str(love_total))
    # Falta el print

# ✅ Ahora sí se muestra
def calculate_love_score(name1, name2):
    love_score = int(str(true_total) + str(love_total))
    print(love_score)
```
---

## 📚 Recursos Adicionales

- [Python String Methods Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python For Loops Tutorial](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Functions Guide](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

---

## 🏆 Conclusión

Este ejercicio es excelente para:
- Practicar funciones y loops
- Entender manipulación de strings
- Aprender a resolver problemas paso a paso
- Divertirse mientras aprendes Python 😄

**La versión recomendada es la Versión 2 (con for loop)** porque combina claridad, eficiencia y buenas prácticas de programación.

**¡Happy Coding! 💻💕**
