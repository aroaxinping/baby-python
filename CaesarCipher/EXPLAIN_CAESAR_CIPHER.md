# 🔐 EXPLICACIÓN DEL CIFRADO CÉSAR

## ÍNDICE

1. [Código Completo Final](#-código-completo-final)
2. [Importaciones y Configuración Inicial](#-parte-1-importaciones-y-configuración-inicial)
3. [La Función Caesar - El Corazón del Programa](#-parte-2-la-función-caesar---el-corazón-del-programa)
4. [El Bucle de Reinicio](#-parte-3-el-bucle-de-reinicio)
5. [Comparación: Dos Funciones vs Una Función](#-comparación-dos-funciones-vs-una-función)
6. [Manejo de Caracteres Especiales](#-parte-4-manejo-de-caracteres-especiales)
7. [Visualización Completa de Ejecución](#-visualización-completa-de-ejecución)
8. [Errores Comunes que Cometí](#-errores-comunes-que-cometí)
9. [Conceptos Clave Aprendidos](#-conceptos-clave-aprendidos)
10. [Ejercicios para Practicar](#-ejercicios-para-practicar)

---

## CÓDIGO COMPLETO FINAL
```python
# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
            
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
```

---

## 📦 PARTE 1: IMPORTACIONES Y CONFIGURACIÓN INICIAL

### **Línea 1-2: Importar y mostrar el logo**
```python
from art import logo
print(logo)
```

#### **🔍 Análisis detallado:**

**¿Qué hace `from art import logo`?**
- Busca un archivo llamado `art.py` en la misma carpeta
- Importa SOLO la variable `logo` de ese archivo
- No importa todo el archivo, solo lo que necesitamos

**Estructura del archivo `art.py`:**
```python
# art.py
logo = """
 _____                              
|  __ \                             
| |  \/ __ _  ___  ___  __ _ _ __  
| | __ / _` |/ _ \/ __|/ _` | '__| 
| |_\ \ (_| |  __/\__ \ (_| | |    
 \____/\__,_|\___||___/\__,_|_|    
"""
```

**❓ ¿Por qué importar en lugar de copiar el logo aquí?**

| Opción | Ventajas | Desventajas |
|--------|----------|-------------|
| **Importar** (nuestra opción) | ✅ Código organizado<br>✅ Fácil de cambiar el logo<br>✅ Reutilizable en otros programas | Necesitas otro archivo |
| **Copiar aquí** | ✅ Todo en un archivo | ❌ Código largo y desordenado<br>❌ Difícil de leer<br>❌ Mezcla lógica con arte |

**✅ Importar es la práctica profesional.**

---

### **Línea 4: El alfabeto**
```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

#### **¿Por qué una lista y NO un string?**

**Comparación:**
```python
# Opción 1: Lista (nuestra opción)
alphabet = ['a', 'b', 'c', ..., 'z']
alphabet.index('a')  # Devuelve 0 (posición)
alphabet[3]          # Devuelve 'd'
# ✅ Fácil de buscar posiciones
# ✅ Fácil de acceder por índice

# Opción 2: String
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.index('a')  # Devuelve 0 (también funciona)
alphabet[3]          # Devuelve 'd' (también funciona)
# ✅ También funciona igual
# ❌ Menos visual (todo junto)
```

**Nota:** En este caso, ¡ambas opciones funcionan igual! Es más cuestión de preferencia visual. La profe eligió lista porque es más fácil de ver cada letra separada.

---

## 🧠 PARTE 2: LA FUNCIÓN CAESAR - EL CORAZÓN DEL PROGRAMA
```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
            
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")
```

### **🎯 LA PREGUNTA CLAVE: ¿Por qué `encode_or_decode` como parámetro?**

Aquí está **el concepto MÁS IMPORTANTE** que debes entender:

#### **Lo que YO pensaba (y es lógico pensar):**
```python
# Mi idea: usar las FUNCIONES como parámetros
def caesar(encrypt, decrypt):  # ❌ Esto NO tiene sentido aquí
    if direction == "encode":
        encrypt(...)  # ¿Cuál encrypt? ¿La que pasas como parámetro?
    else:
        decrypt(...)  # ¿Cuál decrypt? ¿La que pasas como parámetro?
```

**Problema:** Las funciones `encrypt` y `decrypt` ya las definiste antes. No necesitas que te las "pasen" como parámetros. Ya las tienes disponibles.

#### **Lo que LA PROFE pensó (brillante):**
```python
# Su idea: NO necesito dos funciones separadas
# Solo necesito SABER qué quiere hacer el usuario
def caesar(original_text, shift_amount, encode_or_decode):
    # encode_or_decode me DICE qué hacer
    # Es un STRING: "encode" o "decode"
```

---

### **🔑 CONCEPTO CRUCIAL: Parámetros = Datos que CAMBIAN**

**Pregunta:** ¿Qué datos cambian cada vez que usas el programa?

| Dato | ¿Cambia cada vez? | ¿Debe ser parámetro? |
|------|-------------------|----------------------|
| El texto que el usuario escribe | ✅ SÍ | ✅ SÍ → `original_text` |
| El número de shift | ✅ SÍ | ✅ SÍ → `shift_amount` |
| Si quiere encode o decode | ✅ SÍ | ✅ SÍ → `encode_or_decode` |
| El alfabeto | ❌ NO (siempre es el mismo) | ❌ NO (variable global) |
| Las funciones encrypt/decrypt | ❌ NO existen más (combinadas en caesar) | ❌ NO |

---

### **Línea por línea de la función `caesar`:**

#### **Línea 1: Definición**
```python
def caesar(original_text, shift_amount, encode_or_decode):
```

**Análisis de los parámetros:**

1. **`original_text`**: El mensaje del usuario
   - Ejemplo: `"hola"`
   - Tipo: `string`

2. **`shift_amount`**: Cuántas posiciones desplazar
   - Ejemplo: `3`
   - Tipo: `int`

3. **`encode_or_decode`**: La dirección de la operación
   - Ejemplo: `"encode"` o `"decode"`
   - Tipo: `string`
   - **¡ESTE ES EL TRUCO!** 🎩✨

**❓ ¿Por qué NO llamar al parámetro `direction`?**

Ambos nombres funcionan igual:
```python
# Opción 1: encode_or_decode (más descriptivo)
def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        # Es claro qué contiene

# Opción 2: direction (más corto)
def caesar(original_text, shift_amount, direction):
    if direction == "decode":
        # También es claro

# ✅ Ambos están bien, es preferencia personal
```

La profe eligió `encode_or_decode` porque es **MÁS EXPLÍCITO** sobre qué valores puede tener.

---

#### **Línea 2: Inicializar output**
```python
output_text = ""
```

**¿Qué hace?**
- Crea un string vacío donde construiremos el resultado

**¿Por qué vacío?**
- Iremos **agregando** letras una por una
- Es como empezar con una hoja en blanco

**Ejemplo de construcción:**
```python
output_text = ""
output_text += "h"  # output_text = "h"
output_text += "o"  # output_text = "ho"
output_text += "l"  # output_text = "hol"
output_text += "a"  # output_text = "hola"
```

---

#### **Línea 4: El loop principal**
```python
for letter in original_text:
```

**¿Qué hace?**
- Recorre CADA letra del texto original

**Ejemplo:**
```python
original_text = "hola"

# Iteración 1: letter = "h"
# Iteración 2: letter = "o"
# Iteración 3: letter = "l"
# Iteración 4: letter = "a"
```

---

#### **Línea 5-6: Manejar caracteres especiales (TODO-2)**
```python
if letter not in alphabet:
    output_text += letter
```

**¿Qué hace?**
- Si la letra NO está en el alfabeto (espacio, número, símbolo)
- La añade TAL CUAL al resultado (sin cifrar)

**Ejemplos:**

| Input | ¿Está en alphabet? | Acción |
|-------|--------------------|--------|
| `"a"` | ✅ SÍ | Cifrar |
| `" "` (espacio) | ❌ NO | Copiar tal cual |
| `"3"` | ❌ NO | Copiar tal cual |
| `"!"` | ❌ NO | Copiar tal cual |
| `"z"` | ✅ SÍ | Cifrar |

**Ejemplo completo:**
```python
# Input: "hola mundo!"
# Proceso:
# "h" → en alphabet → cifrar
# "o" → en alphabet → cifrar
# "l" → en alphabet → cifrar
# "a" → en alphabet → cifrar
# " " → NO en alphabet → copiar " "
# "m" → en alphabet → cifrar
# "u" → en alphabet → cifrar
# "n" → en alphabet → cifrar
# "d" → en alphabet → cifrar
# "o" → en alphabet → cifrar
# "!" → NO en alphabet → copiar "!"

# Output (con shift 3): "krod pxqgr!"
```

**❓ ¿Por qué NO cifrar espacios y símbolos?**
```python
# Si cifráramos TODO:
"hola mundo!" → cifrar espacio → ¿qué letra poner?
# ❌ Los espacios no tienen "posición" en el alfabeto
# ❌ Perdemos la separación entre palabras
# ❌ Los símbolos se volverían ilegibles

# ✅ Mejor: dejar espacios y símbolos tal cual
"hola mundo!" → "krod pxqgr!"
# Las palabras siguen separadas
# La puntuación se mantiene
```

---

#### **Línea 7-9: EL TRUCO MÁGICO 🎩✨**
```python
else:
    if encode_or_decode == "decode":
        shift_amount *= -1
```

**¡AQUÍ ESTÁ LA GENIALIDAD DE LA PROFE!**

### **🔍 ANÁLISIS PROFUNDO DEL TRUCO:**

**Pregunta:** ¿Cómo funciona encode vs decode?

**Encode (cifrar):**
```
a → (posición 0 + shift 3) → d
b → (posición 1 + shift 3) → e
c → (posición 2 + shift 3) → f
```

**Decode (descifrar):**
```
d → (posición 3 - shift 3) → a
e → (posición 4 - shift 3) → b
f → (posición 5 - shift 3) → c
```

**Observación:** 
- Encode: **suma** el shift
- Decode: **resta** el shift

**El truco:**
```python
# Sumar un número positivo = encode
posicion + 3

# Sumar un número negativo = decode (es como restar)
posicion + (-3)  # ¡Es lo mismo que: posicion - 3!
```

**Tabla de verdad:**

| `encode_or_decode` | `shift_amount` original | Después del `if` | Operación resultante |
|-------------------|-------------------------|------------------|---------------------|
| `"encode"` | `3` | `3` (sin cambios) | `posicion + 3` ✅ |
| `"decode"` | `3` | `-3` (multiplicado por -1) | `posicion + (-3)` = `posicion - 3` ✅ |

---

### **🎬 DEMOSTRACIÓN PASO A PASO:**

#### **Escenario 1: Encode**
```python
original_text = "abc"
shift_amount = 3
encode_or_decode = "encode"

# Iteración 1: letter = "a"
if "a" not in alphabet:  # False
else:
    if "encode" == "decode":  # False
        # NO se ejecuta, shift_amount sigue siendo 3
    
    shifted_position = alphabet.index("a") + 3
    # = 0 + 3 = 3
    shifted_position %= 26  # 3 % 26 = 3
    output_text += alphabet[3]  # output_text = "d"

# Iteración 2: letter = "b"
# ... similar ...
# output_text = "de"

# Iteración 3: letter = "c"
# ... similar ...
# output_text = "def"

# Resultado: "abc" → "def" ✅
```

---

#### **Escenario 2: Decode**
```python
original_text = "def"
shift_amount = 3
encode_or_decode = "decode"

# Iteración 1: letter = "d"
if "d" not in alphabet:  # False
else:
    if "decode" == "decode":  # True ✅
        shift_amount *= -1  # shift_amount = -3 🎯
    
    shifted_position = alphabet.index("d") + (-3)
    # = 3 + (-3) = 0
    shifted_position %= 26  # 0 % 26 = 0
    output_text += alphabet[0]  # output_text = "a"

# Iteración 2: letter = "e"
# ⚠️ IMPORTANTE: shift_amount YA es -3
    shifted_position = alphabet.index("e") + (-3)
    # = 4 + (-3) = 1
    output_text += alphabet[1]  # output_text = "ab"

# Iteración 3: letter = "f"
    shifted_position = alphabet.index("f") + (-3)
    # = 5 + (-3) = 2
    output_text += alphabet[2]  # output_text = "abc"

# Resultado: "def" → "abc" ✅
```

---

### **⚠️ ADVERTENCIA IMPORTANTE:**

**Pregunta:** ¿Por qué el `if encode_or_decode == "decode"` está DENTRO del loop `for`?
```python
for letter in original_text:
    # ...
    if encode_or_decode == "decode":  # ← ¿Se ejecuta muchas veces?
        shift_amount *= -1
```

**Respuesta:** Parece ineficiente, ¿verdad? Veamos:

**Ejecución real:**
```python
# Primera iteración:
if "decode" == "decode":  # True
    shift_amount *= -1  # shift_amount pasa de 3 a -3

# Segunda iteración:
if "decode" == "decode":  # True
    shift_amount *= -1  # shift_amount pasa de -3 a 3 ❌❌❌
    # ¡Se vuelve positivo otra vez!

# Tercera iteración:
if "decode" == "decode":  # True
    shift_amount *= -1  # shift_amount pasa de 3 a -3
    # ¡Alterna entre positivo y negativo!
```

**🐛 ¡ESTO ES UN BUG POTENCIAL!**

#### **¿Por qué funciona en el código de la profe?**

**Truco:** Mira el código completo otra vez:
```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:  # ← SOLO entra aquí si letter ESTÁ en alphabet
            if encode_or_decode == "decode":
                shift_amount *= -1
            
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
```

**Si el texto es `"hola mundo!"`:**
- `"h"` → en alphabet → entra al else → multiplica shift
- `"o"` → en alphabet → entra al else → multiplica shift OTRA VEZ ❌
- `"l"` → en alphabet → entra al else → multiplica shift OTRA VEZ ❌
- ...

**¡ESTO ESTÁ MAL! 🐛**

---

### **✅ CÓDIGO CORREGIDO:**
```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    # ✅ Convertir shift ANTES del loop
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")
```

**¿Por qué es mejor?**
- El `if` se ejecuta **UNA SOLA VEZ** antes del loop
- Más eficiente
- Más claro conceptualmente

---

### **📊 COMPARACIÓN: Código original vs Código corregido**

| Aspecto | Código de la profe | Código corregido |
|---------|-------------------|------------------|
| **Ejecuciones del if** | N veces (N = letras en alphabet) | 1 vez |
| **¿Funciona?** | ✅ SÍ (por accidente) | ✅ SÍ |
| **Eficiencia** | ❌ Ineficiente | ✅ Eficiente |
| **Claridad** | ❌ Confuso | ✅ Claro |
| **¿Es un bug?** | ⚠️ Bug técnico que "funciona" | ✅ Sin bugs |

**Nota:** El código de la profe "funciona" porque multiplicar por -1 dos veces vuelve al número original:
```python
3 * -1 = -3
-3 * -1 = 3  # Vuelve a ser positivo
3 * -1 = -3  # Vuelve a ser negativo
# Alterna, pero como solo sumamos UNA VEZ por letra, funciona
```

**Pero es mejor moverlo fuera del loop.**

---

#### **Líneas 11-13: Calcular la nueva posición**
```python
shifted_position = alphabet.index(letter) + shift_amount
shifted_position %= len(alphabet)
output_text += alphabet[shifted_position]
```

### **Línea 11: Calcular posición desplazada**
```python
shifted_position = alphabet.index(letter) + shift_amount
```

**Desglose:**
1. `alphabet.index(letter)`: Encuentra la posición de la letra
2. `+ shift_amount`: Le suma (o resta si es negativo) el shift
3. `shifted_position`: Guarda el resultado

**Ejemplos:**

**Encode (shift = 3):**
| Letra | `.index()` | `+ shift_amount` | `shifted_position` |
|-------|-----------|------------------|-------------------|
| `"a"` | `0` | `0 + 3` | `3` |
| `"x"` | `23` | `23 + 3` | `26` ⚠️ |
| `"z"` | `25` | `25 + 3` | `28` ⚠️ |

**Decode (shift = -3):**
| Letra | `.index()` | `+ shift_amount` | `shifted_position` |
|-------|-----------|------------------|-------------------|
| `"d"` | `3` | `3 + (-3)` | `0` |
| `"a"` | `0` | `0 + (-3)` | `-3` ⚠️ |
| `"b"` | `1` | `1 + (-3)` | `-2` ⚠️ |

**Problema:** ¡Tenemos índices fuera de rango! (26, 28, -3, -2)

---

### **Línea 12: El operador módulo (%) al rescate**
```python
shifted_position %= len(alphabet)
```

**¿Qué hace `%`?**
- Es el operador **módulo** (resto de una división)
- Hace que los números "den la vuelta" cuando se pasan

**Explicación visual:**

Imagina el alfabeto como un círculo:
```
        a  b  c  d
     z              e
    y                f
     x              g
        w  v  u  t
          ...
```

**Ejemplos de módulo:**
```python
# Módulo básico
5 % 26 = 5     # 5 cabe 0 veces en 26, resto 5
26 % 26 = 0    # 26 cabe 1 vez en 26, resto 0
27 % 26 = 1    # 27 cabe 1 vez en 26, resto 1
28 % 26 = 2    # 28 cabe 1 vez en 26, resto 2

# Con números negativos
-1 % 26 = 25   # Da la vuelta al final
-2 % 26 = 24
-3 % 26 = 23
```

**Tabla completa de casos:**

| `shifted_position` antes | `% 26` después | Letra resultante | Explicación |
|-------------------------|----------------|------------------|-------------|
| `3` | `3` | `"d"` | Dentro del rango ✅ |
| `26` | `0` | `"a"` | Dio la vuelta: z → a |
| `27` | `1` | `"b"` | Dio la vuelta: z → a → b |
| `28` | `2` | `"c"` | Dio la vuelta: z → a → b → c |
| `-1` | `25` | `"z"` | Dio la vuelta hacia atrás: a → z |
| `-2` | `24` | `"y"` | a → z → y |
| `-3` | `23` | `"x"` | a → z → y → x |

---

### **🎬 DEMOSTRACIÓN COMPLETA: Encode "xyz" con shift 3**
```python
original_text = "xyz"
shift_amount = 3
encode_or_decode = "encode"

# ====== LETRA "x" ======
letter = "x"

# Paso 1: ¿Está en alphabet?
if "x" not in alphabet:  # False
else:  # ✅ Entra aquí

# Paso 2: ¿Es decode?
    if "encode" == "decode":  # False
        # No se ejecuta

# Paso 3: Calcular posición
    shifted_position = alphabet.index("x") + 3
    # alphabet.index("x") = 23
    # 23 + 3 = 26

# Paso 4: Aplicar módulo
    shifted_position %= 26
    # 26 % 26 = 0

# Paso 5: Obtener letra
    output_text += alphabet[0]
    # alphabet[0] = "a"
    # output_text = "a"

# ====== LETRA "y" ======
letter = "y"

    shifted_position = alphabet.index("y") + 3
    # 24 + 3 = 27
    shifted_position %= 26
    # 27 % 26 = 1
    output_text += alphabet[1]
    # output_text = "ab"

# ====== LETRA "z" ======
letter = "z"

    shifted_position = alphabet.index("z") + 3
    # 25 + 3 = 28
    shifted_position %= 26
    # 28 % 26 = 2
    output_text += alphabet[2]
    # output_text = "abc"

# ====== RESULTADO FINAL ======
print(f"Here is the encoded result: abc")
```

**Resultado:** `"xyz"` con shift 3 → `"abc"` ✅

---

### **🎬 DEMOSTRACIÓN COMPLETA: Decode "abc" con shift 3**
```python
original_text = "abc"
shift_amount = 3
encode_or_decode = "decode"

# ANTES DEL LOOP (si movemos el if fuera):
if "decode" == "decode":
    shift_amount *= -1  # shift_amount = -3

# ====== LETRA "a" ======
letter = "a"

    shifted_position = alphabet.index("a") + (-3)
    # 0 + (-3) = -3
    
    shifted_position %= 26
    # -3 % 26 = 23 🎯
    
    output_text += alphabet[23]
    # alphabet[23] = "x"
    # output_text = "x"

# ====== LETRA "b" ======
letter = "b"

    shifted_position = alphabet.index("b") + (-3)
    # 1 + (-3) = -2
    shifted_position %= 26
    # -2 % 26 = 24
    output_text += alphabet[24]
    # output_text = "xy"

# ====== LETRA "c" ======
letter = "c"

    shifted_position = alphabet.index("c") + (-3)
    # 2 + (-3) = -1
    shifted_position %= 26
    # -1 % 26 = 25
    output_text += alphabet[25]
    # output_text = "xyz"

# ====== RESULTADO FINAL ======
print(f"Here is the decoded result: xyz")
```

**Resultado:** `"abc"` con shift 3 decode → `"xyz"` ✅

**¡Perfecto! Es simétrico con el encode.**

---

#### **Línea 15: Imprimir resultado**
```python
print(f"Here is the {encode_or_decode}d result: {output_text}")
```

**F-string con variable:**
```python
encode_or_decode = "encode"
print(f"Here is the {encode_or_decode}d result: ...")
# Output: "Here is the encoded result: ..."

encode_or_decode = "decode"
print(f"Here is the {encode_or_decode}d result: ...")
# Output: "Here is the decoded result: ..."
```

**Truco:** La `d` después de `{encode_or_decode}d` forma:
- `"encode" + "d"` = `"encoded"`
- `"decode" + "d"` = `"decoded"`

---

## 🔄 PARTE 3: EL BUCLE DE REINICIO
```python
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
```

### **Línea 1: La bandera (flag)**
```python
should_continue = True
```

**¿Qué es una "bandera"?**
- Una variable booleana que controla un loop
- Como un interruptor: True = encendido, False = apagado

---

### **Línea 3: El loop principal**
```python
while should_continue:
```

**Tabla de ejecución:**

| Iteración | `should_continue` | ¿Entra al loop? | ¿Qué pasa? |
|-----------|-------------------|-----------------|------------|
| 1 | `True` | ✅ SÍ | Pide input, ejecuta caesar, pregunta si continuar |
| 2 | `True` (usuario dijo "yes") | ✅ SÍ | Pide input, ejecuta caesar, pregunta si continuar |
| 3 | `False` (usuario dijo "no") | ❌ NO | Sale del loop |

---

### **Líneas 4-6: Pedir datos al usuario**
```python
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
```

**Nota:** Esto pasa **dentro** del loop, por lo que se repite cada vez.

**Flujo:**
```
Usuario entra al programa
↓
Pregunta 1: ¿encode o decode?
Pregunta 2: ¿qué mensaje?
Pregunta 3: ¿qué shift?
↓
Ejecuta caesar
↓
Pregunta 4: ¿continuar?
↓
Si "yes": vuelve a Pregunta 1
Si "no": termina
```

---

### **Línea 8: Llamar a la función**
```python
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
```

**Matching de argumentos con parámetros:**

| Argumento | Valor del usuario | Parámetro de la función | Valor recibido |
|-----------|-------------------|-------------------------|----------------|
| `original_text=text` | `"hola"` | `original_text` | `"hola"` |
| `shift_amount=shift` | `3` | `shift_amount` | `3` |
| `encode_or_decode=direction` | `"encode"` | `encode_or_decode` | `"encode"` |

**Visualización:**
```python
# Lo que el usuario ve:
direction = "encode"  # Usuario escribió "encode"
text = "hola"         # Usuario escribió "hola"
shift = 3             # Usuario escribió 3

# La llamada:
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

# Lo que la función recibe:
def caesar(original_text, shift_amount, encode_or_decode):
    # original_text = "hola"
    # shift_amount = 3
    # encode_or_decode = "encode"
```

---

### **Líneas 10-13: Preguntar si continuar**
```python
restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
if restart == "no":
    should_continue = False
    print("Goodbye!")
```

**Flujo de decisión:**
```
¿Usuario dice "no"?
    │
    ├─ SÍ → should_continue = False → Loop termina
    │
    └─ NO → should_continue sigue True → Loop continúa
```

**Tabla de casos:**

| Input del usuario | `.lower()` | `restart == "no"` | `should_continue` | ¿Continúa el loop? |
|-------------------|-----------|-------------------|-------------------|-------------------|
| `"yes"` | `"yes"` | `False` | `True` | ✅ SÍ |
| `"YES"` | `"yes"` | `False` | `True` | ✅ SÍ |
| `"y"` | `"y"` | `False` | `True` | ✅ SÍ (cualquier cosa que no sea "no") |
| `"no"` | `"no"` | `True` | `False` | ❌ NO |
| `"NO"` | `"no"` | `True` | `False` | ❌ NO |
| `"nope"` | `"nope"` | `False` | `True` | ✅ SÍ (no es exactamente "no") |

---

## 🆚 COMPARACIÓN: DOS FUNCIONES VS UNA FUNCIÓN

### **❌ ENFOQUE 1: Dos funciones separadas (mi idea original)**
```python
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    decipher_text = ""
    for letter in original_text:
        deshifted_position = alphabet.index(letter) - shift_amount  # ← RESTA
        deshifted_position %= len(alphabet)
        decipher_text += alphabet[deshifted_position]
    print(f"Here's the decoded result: {decipher_text}")

# Uso:
if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(original_text=text, shift_amount=shift)
```

**Análisis:**

| Aspecto | Evaluación |
|---------|------------|
| **Líneas de código** | ~20 líneas |
| **Duplicación** | ❌ Mucha (95% del código es idéntico) |
| **Mantenimiento** | ❌ Difícil (cambiar algo = cambiar en 2 lugares) |
| **Claridad** | ✅ Muy claro qué hace cada función |
| **Flexibilidad** | ❌ Agregar features = modificar 2 funciones |

---

### **✅ ENFOQUE 2: Una función con parámetro (enfoque de la profe)**
```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1  # ← EL TRUCO
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Uso:
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
```

**Análisis:**

| Aspecto | Evaluación |
|---------|------------|
| **Líneas de código** | ~10 líneas |
| **Duplicación** | ✅ Cero |
| **Mantenimiento** | ✅ Fácil (un solo lugar para cambios) |
| **Claridad** | ⚠️ Requiere entender el truco del -1 |
| **Flexibilidad** | ✅ Fácil agregar features |

---

### **📊 TABLA COMPARATIVA DETALLADA:**

| Criterio | Dos funciones | Una función |
|----------|---------------|-------------|
| **Líneas de código** | 20+ | 10-12 |
| **DRY (Don't Repeat Yourself)** | ❌ Viola el principio | ✅ Cumple el principio |
| **Bugs potenciales** | ⚠️ Mayor (doble código = doble bugs) | ✅ Menor (un lugar = menos bugs) |
| **Testing** | ⚠️ Necesitas testear 2 funciones | ✅ Solo testeas 1 función |
| **Legibilidad para principiantes** | ✅ Muy claro | ⚠️ Requiere entender el truco |
| **Legibilidad para expertos** | ⚠️ Verboso | ✅ Elegante |
| **Escalabilidad** | ❌ Agregar "rotate" = 3ra función | ✅ Agregar "rotate" = 1 línea más |

---

### **🎓 LECCIÓN DE DISEÑO:**

**Principio DRY (Don't Repeat Yourself):**
> "Si copias código, estás haciendo algo mal. Busca cómo reutilizar."

**La profe aplicó este principio preguntándose:**
1. ¿Qué tienen en común `encrypt` y `decrypt`?
   - Respuesta: TODO excepto el signo del shift
2. ¿Puedo parametrizar esa diferencia?
   - Respuesta: SÍ, con una variable `encode_or_decode`
3. ¿Cómo unifico la lógica?
   - Respuesta: Multiplicar shift por -1 cuando sea decode

---

## 🔧 PARTE 4: MANEJO DE CARACTERES ESPECIALES

### **El problema original:**
```python
# Sin manejo de caracteres especiales:
"hola mundo!" con shift 3
# ❌ Error: ' ' no está en alphabet
# ❌ Error: '!' no está en alphabet
```

### **La solución:**
```python
if letter not in alphabet:
    output_text += letter  # Copiar tal cual
else:
    # Cifrar normalmente
```

**Ejemplos de casos:**

| Input | Contiene | Output (shift 3) | Explicación |
|-------|----------|------------------|-------------|
| `"abc"` | Solo letras | `"def"` | Todo cifrado |
| `"a b c"` | Letras + espacios | `"d e f"` | Espacios copiados |
| `"a1b2"` | Letras + números | `"d1e2"` | Números copiados |
| `"hola!"` | Letras + puntuación | `"krod!"` | Puntuación copiada |
| `"123"` | Solo números | `"123"` | Todo copiado (nada cifrado) |

---

## 🎬 VISUALIZACIÓN COMPLETA DE EJECUCIÓN

### **📋 Escenario: Usuario cifra "hola 3" con shift 5, luego descifra**

#### **🔵 Primera iteración del while (Encode)**
```
┌─────────────────────────────────────────┐
│ should_continue = True                  │
│ while should_continue: ← ENTRA          │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│ Input 1: direction = "encode"           │
│ Input 2: text = "hola 3"                │
│ Input 3: shift = 5                      │
└─────────────────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────────────────────────┐
│ Llamada: caesar("hola 3", 5, "encode")                   │
│                                                           │
│   ┌─ output_text = ""                                    │
│   │                                                       │
│   ├─ if "encode" == "decode": NO                         │
│   │   shift_amount sigue siendo 5                        │
│   │                                                       │
│   ├─ for letter in "hola 3":                             │
│   │                                                       │
│   │   [h] → en alphabet → 7 + 5 = 12 → 'm'               │
│   │   output_text = "m"                                  │
│   │                                                       │
│   │   [o] → en alphabet → 14 + 5 = 19 → 't'              │
│   │   output_text = "mt"                                 │
│   │                                                       │
│   │   [l] → en alphabet → 11 + 5 = 16 → 'q'              │
│   │   output_text = "mtq"                                │
│   │                                                       │
│   │   [a] → en alphabet → 0 + 5 = 5 → 'f'                │
│   │   output_text = "mtqf"                               │
│   │                                                       │
│   │   [ ] → NO en alphabet → copiar ' '                  │
│   │   output_text = "mtqf "                              │
│   │                                                       │
│   │   [3] → NO en alphabet → copiar '3'                  │
│   │   output_text = "mtqf 3"                             │
│   │                                                       │
│   └─ print("Here is the encoded result: mtqf 3")         │
└──────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│ restart = "yes"                         │
│ if "yes" == "no": NO                    │
│ should_continue sigue True              │
└─────────────────────────────────────────┘
         │
         ▼ Vuelve al inicio del while
```

---

#### **🔵 Segunda iteración del while (Decode)**
```
┌─────────────────────────────────────────┐
│ should_continue = True                  │
│ while should_continue: ← ENTRA          │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│ Input 1: direction = "decode"           │
│ Input 2: text = "mtqf 3"                │
│ Input 3: shift = 5                      │
└─────────────────────────────────────────┘
         │
         ▼
┌──────────────────────────────────────────────────────────┐
│ Llamada: caesar("mtqf 3", 5, "decode")                   │
│                                                           │
│   ┌─ output_text = ""                                    │
│   │                                                       │
│   ├─ if "decode" == "decode": SÍ                         │
│   │   shift_amount *= -1 → shift_amount = -5             │
│   │                                                       │
│   ├─ for letter in "mtqf 3":                             │
│   │                                                       │
│   │   [m] → en alphabet → 12 + (-5) = 7 → 'h'            │
│   │   output_text = "h"                                  │
│   │                                                       │
│   │   [t] → en alphabet → 19 + (-5) = 14 → 'o'           │
│   │   output_text = "ho"                                 │
│   │                                                       │
│   │   [q] → en alphabet → 16 + (-5) = 11 → 'l'           │
│   │   output_text = "hol"                                │
│   │                                                       │
│   │   [f] → en alphabet → 5 + (-5) = 0 → 'a'             │
│   │   output_text = "hola"                               │
│   │                                                       │
│   │   [ ] → NO en alphabet → copiar ' '                  │
│   │   output_text = "hola "                              │
│   │                                                       │
│   │   [3] → NO en alphabet → copiar '3'                  │
│   │   output_text = "hola 3"                             │
│   │                                                       │
│   └─ print("Here is the decoded result: hola 3")         │
└──────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│ restart = "no"                          │
│ if "no" == "no": SÍ                     │
│ should_continue = False                 │
│ print("Goodbye!")                       │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│ while should_continue: ← NO ENTRA       │
│ (False = termina)                       │
└─────────────────────────────────────────┘
         │
         ▼
    PROGRAMA TERMINA
```

---

## 🐛 ERRORES COMUNES QUE COMETÍ

### **❌ ERROR 1: Confundir parámetros con argumentos**

**Mi error:**
```python
def caesar(encrypt, decrypt):  # ❌ Pensé que necesitaba pasar funciones
    if direction == "encode":
        encrypt()
```

**Por qué estaba mal:**
- Los parámetros deben ser **datos** que cambian, no las funciones en sí
- Las funciones ya están definidas, no necesito recibirlas como parámetros

**Corrección:**
```python
def caesar(original_text, shift_amount, encode_or_decode):  # ✅ Datos que cambian
    if encode_or_decode == "encode":
        # Usar la lógica directamente
```

**Lección aprendida:**
> Los parámetros son para datos que **varían entre llamadas**, no para cosas que ya existen en el código.

---

### **❌ ERROR 2: Iterando sobre la variable equivocada en decrypt**

**Mi error:**
```python
def decrypt(original_text, shift_amount):
    decipher_text = " "  # ❌ Con espacio en lugar de vacío
    for letter in decipher_text:  # ❌❌❌ Iterando sobre la variable DESTINO
        deshifted_position = alphabet.index(letter) - shift_amount
        decipher_text += alphabet[deshifted_position]
```

**Por qué estaba mal:**
1. `decipher_text = " "` tiene un espacio, no está vacío
2. `for letter in decipher_text` itera sobre el string DESTINO (vacío/espacio), no sobre el texto original
3. Nunca procesa el texto del usuario

**Corrección:**
```python
def decrypt(original_text, shift_amount):
    decipher_text = ""  # ✅ Vacío sin espacios
    for letter in original_text:  # ✅ Itera sobre el INPUT del usuario
        deshifted_position = alphabet.index(letter) - shift_amount
        decipher_text += alphabet[deshifted_position]
```

**Lección aprendida:**
> Siempre itera sobre los **datos de entrada** (input), no sobre los datos de salida (output).

---

### **❌ ERROR 3: No entender por qué usar `encode_or_decode` como parámetro**

**Mi confusión:**
```python
# Pregunta que tenía: ¿Por qué encode_or_decode es un parámetro
# si las funciones encrypt y decrypt ya existen?

def caesar(original_text, shift_amount, encode_or_decode):  # ← ¿Por qué esto?
```

**Por qué estaba confundido:**
- Pensaba que los parámetros solo podían ser "datos puros" como números o texto
- No entendía que un string puede **controlar el comportamiento** de una función

**Lo que entendí después:**
```python
# encode_or_decode es un STRING que dice QUÉ hacer
def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":  # ← Decide qué hacer basado en el string
        shift_amount *= -1  # Cambia el comportamiento
```

**Lección aprendida:**
> Los parámetros pueden ser "datos de control" que determinan cómo funciona tu código, no solo "datos para procesar".

---

### **❌ ERROR 4: No usar `.lower()` consistentemente**

**Mi error:**
```python
# A veces usaba .lower() y a veces no
direction = input("Type 'encode' to encrypt:\n")  # ❌ Sin .lower()
text = input("Type your message:\n").lower()      # ✅ Con .lower()
```

**Por qué estaba mal:**
- Si el usuario escribe "ENCODE", no funciona porque no matchea con "encode"
- Inconsistente: unas variables con `.lower()` y otras sin

**Corrección:**
```python
# Siempre usar .lower() en TODOS los inputs de strings
direction = input("Type 'encode' to encrypt:\n").lower()  # ✅
text = input("Type your message:\n").lower()              # ✅
```

**Lección aprendida:**
> Siempre normaliza inputs de texto con `.lower()` para evitar problemas de case-sensitivity.

---

### **❌ ERROR 5: No entender la ubicación del `if encode_or_decode == "decode"`**

**Mi confusión:**
```python
# Veía esto en el código de la profe:
for letter in original_text:
    if encode_or_decode == "decode":  # ← ¿Por qué DENTRO del loop?
        shift_amount *= -1
```

**Por qué estaba confundido:**
- Pensaba que se ejecutaba una vez por cada letra
- No entendía por qué no estaba ANTES del loop

**Lo que descubrí:**
```python
# Esto es un BUG técnico que "funciona" por accidente
# Primera iteración: 3 * -1 = -3
# Segunda iteración: -3 * -1 = 3  ← ¡Vuelve a ser positivo!
# Tercera iteración: 3 * -1 = -3  ← Alterna

# Pero como solo usamos shift_amount una vez por iteración,
# el bug no afecta el resultado final
```

**Corrección (mejor práctica):**
```python
def caesar(original_text, shift_amount, encode_or_decode):
    # ✅ Mover ANTES del loop
    if encode_or_decode == "decode":
        shift_amount *= -1
    
    for letter in original_text:
        # Ya no necesitas el if aquí
        shifted_position = alphabet.index(letter) + shift_amount
```

**Lección aprendida:**
> Si algo solo necesita ejecutarse UNA VEZ, ponlo FUERA del loop, no dentro.

---

### **❌ ERROR 6: No entender el operador módulo `%`**

**Mi confusión:**
```python
shifted_position = 28
shifted_position %= 26  # ← ¿Qué hace esto exactamente?
# Resultado: 2
```

**Por qué estaba confundido:**
- No entendía cómo 28 se convierte en 2
- No veía la conexión con "dar la vuelta" en el alfabeto

**Lo que entendí después:**
```python
# Módulo = resto de una división
28 ÷ 26 = 1 con resto 2
# 28 % 26 = 2

# Visual:
# z (25) + 3 = 28
# 28 % 26 = 2
# alphabet[2] = 'c'
# z → a → b → c ✅ Da la vuelta correctamente
```

**Casos especiales que me confundían:**
```python
# Con números negativos
-3 % 26 = 23  # ← ¿Por qué no -3?

# Explicación:
# Python siempre devuelve un número positivo
# -3 % 26 busca: ¿qué número entre 0-25 es equivalente a -3?
# Respuesta: 23 (porque 23 + 3 = 26 = 0 en módulo)
```

**Lección aprendida:**
> El operador `%` es perfecto para hacer que los índices "den la vuelta" en estructuras cíclicas como el alfabeto.

---

### **❌ ERROR 7: No validar el tipo de dato del shift**

**Mi error:**
```python
shift = input("Type the shift number:\n")  # ❌ Devuelve un string
shifted_position = alphabet.index(letter) + shift  # ❌ TypeError!
```

**Por qué estaba mal:**
- `input()` SIEMPRE devuelve un string
- No puedes sumar un string con un número

**Corrección:**
```python
shift = int(input("Type the shift number:\n"))  # ✅ Convertir a int
shifted_position = alphabet.index(letter) + shift  # ✅ Funciona
```

**Lección aprendida:**
> Siempre convierte los inputs numéricos con `int()` o `float()`.

---

### **❌ ERROR 8: No manejar caracteres que no están en el alfabeto**

**Mi error original:**
```python
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        # ❌ No verificaba si letter está en alphabet
        shifted_position = alphabet.index(letter) + shift_amount
        # Si letter = " " (espacio) → ValueError: ' ' is not in list
```

**Por qué estaba mal:**
- `.index()` lanza un error si el elemento no existe en la lista
- Espacios, números, símbolos no están en `alphabet`

**Corrección:**
```python
for letter in original_text:
    if letter not in alphabet:  # ✅ Verificar primero
        output_text += letter  # Copiar sin cambios
    else:
        # Solo cifrar si está en alphabet
        shifted_position = alphabet.index(letter) + shift_amount
```

**Lección aprendida:**
> Siempre valida que un elemento existe antes de buscarlo con `.index()`.

---

### **❌ ERROR 9: Crear dos funciones casi idénticas**

**Mi error:**
```python
def encrypt(original_text, shift_amount):
    # ... 10 líneas de código
    shifted_position = alphabet.index(letter) + shift_amount  # ← SUMA

def decrypt(original_text, shift_amount):
    # ... 10 líneas de código (IGUALES)
    deshifted_position = alphabet.index(letter) - shift_amount  # ← RESTA

# ❌ 20 líneas con 95% de duplicación
```

**Por qué estaba mal:**
- Violaba el principio DRY (Don't Repeat Yourself)
- Más código = más bugs potenciales
- Cambiar algo = cambiar en dos lugares

**Corrección (lo que hizo la profe):**
```python
def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        shift_amount *= -1  # ← Convierte suma en resta
    
    # Una sola lógica para ambos casos
    shifted_position = alphabet.index(letter) + shift_amount
    # Si decode: + (-3) = - 3 ✅
```

**Lección aprendida:**
> Si dos funciones son 90% iguales, probablemente deberían ser una sola función con parámetros.

---

### **❌ ERROR 10: No reiniciar el programa correctamente**

**Mi intento fallido:**
```python
# Intenté llamar al programa de nuevo
def main():
    # ... todo el código ...
    if restart == "yes":
        main()  # ❌ Recursión infinita potencial

main()
```

**Por qué estaba mal:**
- La recursión puede causar stack overflow si el usuario juega muchas veces
- No es la forma "Pythonica" de hacer loops

**Corrección:**
```python
should_continue = True
while should_continue:  # ✅ Loop controlado con bandera
    # ... código del juego ...
    if restart == "no":
        should_continue = False  # Termina el loop
```

**Lección aprendida:**
> Para repetir código, usa loops (`while`), no recursión.

---

## 📊 RESUMEN DE ERRORES Y CORRECCIONES

| Error | Problema | Solución |
|-------|----------|----------|
| **Parámetros equivocados** | Usar funciones como parámetros | Usar datos que cambian |
| **Iterar variable equivocada** | `for letter in decipher_text` | `for letter in original_text` |
| **String con espacio** | `decipher_text = " "` | `decipher_text = ""` |
| **Sin `.lower()`** | Case-sensitive | Usar `.lower()` en todos los inputs |
| **`if` dentro del loop** | Ineficiente | Mover antes del loop |
| **No entender `%`** | Confusión con módulo | Estudiar casos de ejemplo |
| **Sin `int()`** | TypeError al sumar | `int(input())` |
| **No validar caracteres** | ValueError con espacios | Usar `if letter not in alphabet` |
| **Código duplicado** | Dos funciones iguales | Una función parametrizada |
| **Recursión para repetir** | Stack overflow | Usar `while` loop |

---

## 🎓 CONCEPTOS CLAVE APRENDIDOS

### **1. Parametrización de comportamiento**
```python
# En lugar de dos funciones, un parámetro controla el comportamiento
def caesar(original_text, shift_amount, encode_or_decode):
```
**Principio:** Un parámetro puede cambiar cómo funciona toda una función.

---

### **2. Números negativos como "operación inversa"**
```python
# Encode: suma
posicion + shift

# Decode: resta (suma negativo)
posicion + (-shift)
```
**Principio:** Sumar un negativo = restar. Esto permite unificar operaciones opuestas.

---

### **3. Operador módulo para "dar la vuelta"**
```python
28 % 26 = 2   # z + 3 → a, b, c → índice 2
-3 % 26 = 23  # a - 3 → z, y, x → índice 23
```
**Principio:** El módulo hace que los índices "den la vuelta" en los límites.

---

### **4. Banderas (flags) para controlar loops**
```python
should_continue = True
while should_continue:
    # ...
    if condicion:
        should_continue = False  # Termina el loop
```
**Principio:** Una variable booleana controla cuándo termina un loop indefinido.

---

### **5. Filtrado de caracteres**
```python
if letter not in alphabet:
    output_text += letter  # Copiar sin procesar
else:
    # Procesar
```
**Principio:** No todos los elementos necesitan procesarse. Algunos pueden copiarse tal cual.

---

### **6. Principio DRY (Don't Repeat Yourself)**
```python
# ❌ MAL: Dos funciones casi idénticas
def encrypt(): ...
def decrypt(): ...

# ✅ BIEN: Una función parametrizada
def caesar(encode_or_decode): ...
```
**Principio:** Si dos piezas de código son 90% iguales, probablemente deberían ser una sola con parámetros.

---

### **7. Operadores de asignación compuestos**
```python
shift_amount *= -1  # Mismo que: shift_amount = shift_amount * -1
output_text += letter  # Mismo que: output_text = output_text + letter
```

---

### **8. Conversión de tipos con `.lower()` e `int()`**
```python
direction = input("...").lower()  # String a minúsculas
shift = int(input("..."))  # String a entero
```

---

- [Python Official Docs - String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Real Python - Modulo Operator](https://realpython.com/python-modulo-operator/)
- [Wikipedia - Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Cryptography - Basic Concepts](https://www.khanacademy.org/computing/computer-science/cryptography)
- [Python Official Docs - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)

---

## 📌 RESUMEN EJECUTIVO

### **3 cosas más importantes que aprendí:**

1. **Usar parámetros para cambiar comportamiento**
   - En lugar de dos funciones, una función con un parámetro puede hacer ambas cosas

2. **Números negativos como inversión**
   - Multiplicar por -1 convierte suma en resta (encode → decode)

3. **Módulo para límites cíclicos**
   - El operador `%` hace que los índices "den la vuelta"

---

### **El "truco mágico" en una frase:**
> "Sumar un número negativo es restar, así que multiplicar el shift por -1 convierte encode en decode."

---

### **Flujo del programa en 5 pasos:**
1. Mostrar logo
2. Pedir datos (encode/decode, texto, shift)
3. Llamar función `caesar` que procesa letra por letra
4. Preguntar si quiere continuar
5. Repetir o terminar

---

### **Los 3 errores más importantes que cometí:**
1. **Confundir qué debe ser un parámetro** (funciones vs datos)
2. **Iterar sobre la variable equivocada** (output en lugar de input)
3. **No validar inputs** (sin `.lower()`, sin `int()`, sin verificar si letra está en alphabet)

---

## REFLEXIÓN FINAL

- **La simplicidad es mejor que la duplicación**: Una función bien diseñada es mejor que dos funciones casi iguales
- **Los bugs pueden "funcionar"**: El código de la profe técnicamente tiene un bug (multiplicar por -1 dentro del loop) pero funciona por accidente
- **Validar inputs es crucial**: Sin `.lower()`, `int()`, y verificaciones, el programa falla fácilmente
- **El módulo `%` es mágico**: Perfecto para estructuras cíclicas
- **DRY es importante**: Don't Repeat Yourself - si copias código, algo está mal

**Lo más importante:** Entender el **por qué** detrás de cada decisión de diseño, no solo el **cómo** funciona el código.

---
