# 🧮 Calculadora Recursiva con Acumulación

Un programa de calculadora en Python que permite realizar operaciones matemáticas básicas y continuar calculando con el resultado anterior.

## 📋 Descripción

Este proyecto implementa una calculadora que:
- Realiza operaciones básicas: suma, resta, multiplicación y división
- Permite continuar calculando con el resultado anterior
- Se puede reiniciar completamente para nuevos cálculos
- Usa recursión para reiniciar el programa limpiamente

## 🚀 Características

- ✅ Cuatro operaciones matemáticas básicas
- ✅ Acumulación de resultados
- ✅ Reinicio limpio del programa
- ✅ Interfaz de consola clara
- ✅ Uso de funciones y diccionarios

## 💻 Ejemplo de uso

```
What is the first number?: 10
+
-
*
/
Pick an operation: *
What is the next number?: 5
10.0 * 5.0 = 50.0
Type 'y' to continue calculating with 50.0, or type 'n' to start a new calculation: y

+
-
*
/
Pick an operation: +
What is the next number?: 15
50.0 + 15.0 = 65.0
Type 'y' to continue calculating with 65.0, or type 'n' to start a new calculation: n

[Pantalla limpia y programa reinicia]
```

## 🧠 Explicación del código paso a paso

### 1. Definir las funciones de operación

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
```

**¿Por qué funciones separadas?**
- **Modularidad:** Cada operación es independiente
- **Reutilizabilidad:** Puedes usar estas funciones en otros proyectos
- **Claridad:** Es más fácil de leer y mantener
- **Testeo:** Puedes probar cada función por separado

**Concepto clave:** Una función debe hacer UNA cosa y hacerla bien.

### 2. Crear el diccionario de operaciones

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
```

**¿Qué está pasando aquí? 🤔**

Este es el concepto MÁS importante del programa. Estás guardando **funciones** como valores en un diccionario.

- **Clave:** El símbolo de la operación (`"+"`, `"-"`, etc.)
- **Valor:** La función misma (NO el resultado de la función)

**Nota importante:** Escribes `add` sin paréntesis porque quieres guardar la función, no ejecutarla.

```python
# ❌ MAL - Esto ejecutaría la función inmediatamente
operations = {"+": add()}

# ✅ BIEN - Esto guarda la función para ejecutarla después
operations = {"+": add}
```

**¿Cómo se usa?**

```python
# Llamar a la función del diccionario
operations["+"](4, 8)  # Esto ejecuta add(4, 8)
operations["*"](4, 8)  # Esto ejecuta multiply(4, 8)
```

Es como tener un control remoto donde cada botón ejecuta una función diferente.

### 3. La función principal: `calculator()`

```python
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
```

**Desglose:**
1. **`def calculator():`** → Define la función que contiene todo el programa
2. **`print(art.logo)`** → Muestra el logo (archivo art.py)
3. **`should_accumulate = True`** → Variable de control del bucle (bandera/flag)
4. **`num1 = float(input(...))`** → Pide el primer número

**¿Por qué `float()` en lugar de `int()`?**
- `int()` → Solo números enteros (1, 2, 3, 100)
- `float()` → Números decimales (1.5, 3.14, 100.99)

Como queremos que la calculadora sea más flexible, usamos `float()`.

### 4. El bucle principal

```python
while should_accumulate:
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
```

**Paso a paso:**

#### 4.1 Mostrar las operaciones disponibles
```python
for symbol in operations:
    print(symbol)
```
Esto itera sobre las **claves** del diccionario (`+`, `-`, `*`, `/`) y las imprime.

**Resultado en pantalla:**
```
+
-
*
/
```

#### 4.2 Obtener inputs del usuario
```python
operation_symbol = input("Pick an operation: ")
num2 = float(input("What is the next number?: "))
```
- Pide qué operación quiere hacer
- Pide el segundo número

#### 4.3 Realizar el cálculo (¡LA MAGIA! ✨)
```python
answer = operations[operation_symbol](num1, num2)
```

**¿Qué está pasando aquí?**

Vamos a desglosarlo con un ejemplo:
- Usuario escribe: `*`
- `operation_symbol` es ahora `"*"`
- `operations["*"]` busca en el diccionario y encuentra la función `multiply`
- Luego `(num1, num2)` ejecuta esa función con los dos números

Es equivalente a escribir:
```python
answer = multiply(num1, num2)
```

**¡Pero es dinámico!** La función que se ejecuta depende de lo que el usuario escriba.

#### 4.4 Mostrar el resultado
```python
print(f"{num1} {operation_symbol} {num2} = {answer}")
```
Usa un f-string para formatear e imprimir el resultado: `10.0 * 5.0 = 50.0`

### 5. El sistema de acumulación (continuar o reiniciar)

```python
choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

if choice == "y":
    num1 = answer
else:
    should_accumulate = False
    print("\n" * 20)
    calculator()
```

**Esto es el corazón de la funcionalidad de acumulación:**

#### Si el usuario escribe 'y':
```python
num1 = answer
```
- **Reasigna** `num1` con el resultado anterior
- El bucle `while` continúa
- La siguiente iteración usará el resultado como el nuevo primer número

**Ejemplo:**
```
Primera operación: 10 * 5 = 50
Usuario escribe 'y'
num1 = 50  ← Ahora 50 es el nuevo primer número
Segunda operación: 50 + 15 = 65
```

#### Si el usuario escribe 'n':
```python
should_accumulate = False
print("\n" * 20)
calculator()
```

**¿Qué pasa aquí?**

1. **`should_accumulate = False`** → Rompe el bucle `while`
2. **`print("\n" * 20)`** → "Limpia" la pantalla imprimiendo 20 líneas vacías
3. **`calculator()`** → ¡RECURSIÓN! Llama a la función calculadora de nuevo

**¿Qué es recursión?**
Una función que se llama a sí misma. Es como reiniciar el programa desde cero.

```
calculator()
  └─ usuario termina cálculo
      └─ calculator()  ← Nueva instancia
          └─ usuario termina cálculo
              └─ calculator()  ← Otra nueva instancia
                  └─ ...
```

### 6. Iniciar el programa

```python
calculator()
```

Esta línea al final del archivo ejecuta la función `calculator()` por primera vez.

## 🐛 ERRORES QUE COMETÍ

### ❌Error #1: Confusión con `input()` e `int()`

**Mi código original:**
```python
firstnumber = input(int("Type a number: "))
```

**¿Qué está mal?**
- `int()` necesita convertir un STRING a número
- `input()` ya devuelve un string
- Estás intentando convertir el MENSAJE, no el resultado

**✅ Correcto:**
```python
num1 = int(input("Type a number: "))
# O mejor aún:
num1 = float(input("Type a number: "))
```

**El orden importa:**
1. `input()` ejecuta primero → devuelve un string
2. `int()` o `float()` convierte ese string a número

### ❌Error #2: Operación hardcodeada

**Mi código original:**
```python
result = operations["*"](n1=firstnumber, n2=secondnumber)
```

**Problema:** Siempre multiplicas, sin importar lo que el usuario escriba en `do`.

**✅ Correcto:**
```python
result = operations[do](firstnumber, secondnumber)
```

Usas la variable `do` para seleccionar dinámicamente la operación.

### ❌Error #3: Lógica del bucle defectuosa

**Mi código original:**
```python
while keepgoing == "Yes":
    result = firstnumber  # ¿Qué? Esto no tiene sentido
    # ... código ...
    # No calculas ni imprimes el nuevo resultado

if keepgoing == "no":  # Este if nunca se ejecutará lógicamente
    # código duplicado...
```

**Problemas:**
1. Asignas `result = firstnumber` pero nunca usas `result` como el primer número
2. No calculas ni imprimes el nuevo resultado dentro del while
3. El `if` después del `while` solo se ejecuta cuando sales del bucle
4. Comparas con `"Yes"` (mayúscula) pero preguntas `"yes or no"` (minúscula)

**✅ Solución:**
```python
while should_accumulate:
    # ... código de cálculo ...
    
    if choice == "y":
        num1 = answer  # Reasigna el primer número con el resultado
    else:
        should_accumulate = False  # Sale del bucle
        calculator()  # Reinicia completamente
```

**Diferencias clave:**
- Usa una variable booleana (`should_accumulate`) para controlar el bucle
- Reasigna `num1 = answer` para usar el resultado en la siguiente iteración
- Usa recursión para reiniciar limpiamente

### ❌ERROR #4: No reasignar el primer número

**El concepto clave que te faltaba:**

Para que la acumulación funcione, necesitas hacer:
```python
num1 = answer
```

Esto hace que el resultado anterior se convierta en el nuevo primer número.

**Ejemplo visual:**

```
Iteración 1:
num1 = 10
num2 = 5
answer = 50

Usuario dice 'y' → num1 = 50  ← REASIGNACIÓN

Iteración 2:
num1 = 50  ← ¡Ahora es el resultado anterior!
num2 = 15
answer = 65
```

Sin la reasignación, `num1` siempre sería 10 y no acumularías.

## 🎯 Conceptos clave a asentar

### 1. Funciones como valores en diccionarios

```python
# Guardar la función (sin paréntesis)
mi_dict = {"sumar": add}

# Ejecutar la función desde el diccionario (con paréntesis y argumentos)
resultado = mi_dict["sumar"](5, 3)
```

**Analogía:** Es como tener una caja de herramientas. El diccionario es la caja, cada herramienta es una función, y tú eliges cuál usar según la necesitas.

### 2. Variables de control de bucles (flags)

```python
should_continue = True
while should_continue:
    # código...
    if condicion:
        should_continue = False
```

**¿Por qué es mejor que otras opciones?**

❌ Opción confusa:
```python
while respuesta == "y":
    # código...
    respuesta = input("¿Continuar? ")
```

✅ Con flag:
```python
should_continue = True
while should_continue:
    # código...
    if respuesta == "n":
        should_continue = False
```

**Ventajas:**
- Más legible: "mientras debo continuar"
- Múltiples condiciones pueden cambiar el flag
- Separación clara entre lógica y control

### 3. Recursión para reiniciar

```python
def mi_programa():
    # ... código ...
    if reiniciar:
        mi_programa()  # Se llama a sí misma
```

**¿Cuándo usar recursión vs loop?**

- **Loop:** Para repetir con el mismo contexto
- **Recursión:** Para empezar de cero con un estado limpio

En este caso, la recursión es perfecta porque queremos borrar todo y empezar fresh.

### 4. Reasignación de variables

```python
x = 10
x = 20  # x ya no es 10, ahora es 20
```

**En el contexto de la calculadora:**
```python
num1 = 10           # Valor inicial
num1 = answer       # Reasignación con el resultado
```

Cada vez que reasignas, la variable "olvida" su valor anterior.

### 5. `float()` vs `int()`

```python
int(input())    # "10" → 10 (solo enteros)
float(input())  # "10.5" → 10.5 (permite decimales)
```

**Regla general:** Si puede tener decimales, usar `float()`.

### 6. Iteración sobre diccionarios

```python
for key in dictionary:
    print(key)  # Imprime las claves
    print(dictionary[key])  # Imprime los valores
```

**En la calculadora:**
```python
for symbol in operations:
    print(symbol)  # Imprime +, -, *, /
```

## 📊 Comparación: Mi código vs. Código de la profesora

| Aspecto | Mi código | Código de la profesora | ¿Por qué es mejor? |
|---------|-----------|------------------------|-------------------|
| **Estructura** | Todo en el nivel principal | Todo dentro de `calculator()` | Encapsulación y reutilización |
| **Control de bucle** | `while keepgoing == "Yes"` | `while should_accumulate:` | Más claro y mantenible |
| **Acumulación** | `result = firstnumber` (sin usar) | `num1 = answer` | Reasignación correcta |
| **Reinicio** | Código duplicado en `if` | Recursión con `calculator()` | Sin duplicación, más limpio |
| **Comparación** | `"Yes"` vs `"yes or no"` | Consistente con `'y'` y `'n'` | Sin bugs por mayúsculas |
| **Mostrar resultado** | Una vez al inicio | Dentro del bucle | Se ve cada operación |
| **Tipo de número** | `int()` | `float()` | Más flexible (permite decimales) |

## 📚 Patrones para replicar en futuros proyectos

### Patrón: Funciones en diccionario para menú dinámico

```python
def opcion_1():
    print("Opción 1 ejecutada")

def opcion_2():
    print("Opción 2 ejecutada")

menu = {
    "1": opcion_1,
    "2": opcion_2,
}

eleccion = input("Elige 1 o 2: ")
menu[eleccion]()  # Ejecuta la función elegida
```

**Cuándo usar:** Cuando tienes un menú de opciones y quieres evitar un montón de `if/elif/else`.

### Patrón: Flag para controlar bucles

```python
continuar = True
while continuar:
    # hacer cosas...
    
    respuesta = input("¿Continuar? (y/n): ")
    if respuesta == "n":
        continuar = False
```

**Cuándo usar:** Cuando la condición de salida del bucle puede depender de múltiples factores.

### Patrón: Acumulación de valores

```python
valor_acumulado = inicial
while debe_acumular:
    nuevo_valor = hacer_operacion(valor_acumulado, otro_valor)
    print(nuevo_valor)
    
    if continuar:
        valor_acumulado = nuevo_valor  # ← La clave está aquí
```

**Cuándo usar:** Calculadoras, contadores, sumadores, cualquier cosa que acumule resultados.

### Patrón: Recursión para reiniciar programa

```python
def programa():
    # ... todo el código del programa ...
    
    if usuario_quiere_reiniciar:
        print("\n" * 20)  # Limpia pantalla
        programa()  # Reinicia

programa()  # Inicia
```

**Cuándo usar:** Cuando quieres que el usuario pueda reiniciar completamente sin salir del programa.

## 🎓 Lecciones filosóficas de programación

### 1. DRY (Don't Repeat Yourself)
Usar funciones o bucles. 

### 2. Variables descriptivas
`should_accumulate` es mejor que `sa` o `flag1`. Tu yo futuro te lo agradecerá.

### 3. Una función, una responsabilidad
`calculator()` hace TODO el trabajo de la calculadora. `add()` solo suma. Cada una tiene su rol.

### 4. La importancia del flujo
Antes de escribir código, dibuja el flujo:
```
Inicio → Pedir número → Loop → Calcular → ¿Continuar? → Sí: Reasignar | No: Reiniciar
```

---

### Reflexiones finales 💭
### Lo que aprendií (después de sufrir un poco):

1. **Los diccionarios pueden guardar funciones**, y eso es como tener superpoderes, pero también como tener un arma que no sabías que existía hasta que casi te disparas en el pie.

2. **`input(int("mensaje"))` es como poner los zapatos antes de los calcetines**: técnicamente posible de escribir, pero no tiene sentido y todo el mundo se da cuenta de que algo anda mal.

3. **La reasignación de variables es tu amiga**, no tu enemiga. `num1 = answer` es la diferencia entre una calculadora que funciona y una calculadora que hace lo mismo 50 veces pensando que está progresando (como tu vida en general, pero eso es otro tema).

4. **La recursión es magia negra hasta que lo entiendes**, y luego es magia blanca. Es como reiniciar tu computadora: borra todo y empiezas de nuevo. Solo que en este caso, el programa se reinicia a sí mismo como un fénix digital.

5. **Los bucles con flags son como las relaciones**: necesitas una señal clara de cuándo seguir y cuándo es hora de parar. `should_accumulate` es más claro que `keepgoing == "Yes"` que comparas con un input en minúsculas (clásico bug de principiante que todos hemos cometido y nadie admite en público).


### La dura verdad:

Empecé este ejercicio con la inocente ilusión de "bueno, es una calculadora básica, yo creo que sabré hacerla". Terminé con un README de 500+ líneas explicándome a mí misma lcómo hacerla *bien*.

**El orgullo:** ligeramente abollado.  
**La confianza:** recalibrada.  
**El conocimiento:** expandido.

Mi código funcionaba. Hacía sumas, restas, multiplicaciones y divisiones como un campeón. El problema es que era el equivalente digital de una calculadora de bolsillo de los 90: hacía UNA operación y listo. Nada de "quiero seguir calculando con este resultado". Nada de loops elegantes. Nada de acumulación. Solo: calcula, muestra resultado, adiós.

Ahora sí entiendo:
- Por qué guardar **funciones en un diccionario** es brillante (y no brujería)
- Que **`return`** no es decorativo, es esencial para que las funciones devuelvan valores
- Cómo **reasignar variables** (`num1 = answer`) crea la magia de acumulación
- Que los **loops con flags** son más elegantes que mi código lineal

---

### Epitafio para mi código original: 🪦

*Aquí yace la calculadora básica*  
*Funcionaba una vez y se despedía*  
*Su intento de while loop vivía en negación constante*
*Descanse en paz en el cementerio de errores de sintaxis*

*Sin loops, sin acumulación, sin gloria*  
*R.I.P. 2025* 🕊️

---

### Lección de hoy:

A veces la solución es tan simple que tu cerebro se niega a aceptarla. `num1 = answer`. Eso era todo. Eso. Era. Todo.

La diferencia entre código funcional y código útil es: ¿puede el usuario seguir trabajando sin empezar de cero cada vez?

Mi código: "Hice tu suma. Ahora vete y vuelve si necesitas otra cosa."  
Código de la profesora: "¿Quieres seguir? Perfecto, usa este resultado."

---
🏆 **Título obtenido:** Desarrollador de calculadoras con síndrome de amnesia (olvida el resultado anterior)  


*Nos vemos en el próximo proyecto, donde mi código funcionará... pero le faltará algo que la profesora agregará en 3 líneas y me hará cuestionar mis decisiones de vida. El ciclo continúa.*

