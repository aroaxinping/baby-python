# Ejercicios de POO en Python - Empezando desde CERO 🌱

## Introducción 💡

Este archivo está diseñado para que empieces con **Programación Orientada a Objetos (POO) desde CERO ABSOLUTO**. No asumimos que sabes nada sobre clases u objetos.

Iremos paso a paso, construyendo el conocimiento desde lo más básico. Cada ejercicio incluye:
- 📖 **Explicación del concepto nuevo**
- 🎯 **Objetivo del ejercicio**
- ✅ **Ejemplo resuelto** (en los primeros ejercicios)
- 💪 **Tu turno** para practicar

---

## Fase 1: ¿Qué es una Clase? (Teoría Práctica)

### 🤔 Antes de empezar: Recordemos las variables

Ya sabes hacer esto:

```python
nombre = "Dan"
edad = 25
ciudad = "Barcelona"

print(f"Hola, soy {nombre}, tengo {edad} años y vivo en {ciudad}")
```

**Problema:** Si quieres representar a otra persona, necesitas más variables:

```python
nombre1 = "Dan"
edad1 = 25
ciudad1 = "Barcelona"

nombre2 = "Alex"
edad2 = 30
ciudad2 = "Madrid"

# Esto se vuelve un desastre rápidamente 😰
```

**Solución:** ¡Las clases! Una clase es como una "plantilla" para crear objetos relacionados.

---

## Ejercicio 1: Tu Primera Clase 🎯

### 📖 Concepto: Crear una clase vacía

```python
# La palabra 'class' indica que vamos a crear una clase
# 'Persona' es el nombre (siempre con mayúscula inicial)
class Persona:
    pass  # 'pass' significa "no hagas nada, está vacía"
```

### ✅ Ejemplo Resuelto: Crear un objeto

```python
class Persona:
    pass

# Crear objetos usando la clase
persona1 = Persona()  # Los () crean el objeto
persona2 = Persona()

print(persona1)  # <__main__.Persona object at 0x...>
```

### 💪 Tu Turno:

Crea una clase llamada `Perro` vacía (con `pass`) y luego crea 2 objetos: `mi_perro` y `tu_perro`.

```python
# Escribe tu código aquí


```

---

## Ejercicio 2: Añadiendo Atributos 📦

### 📖 Concepto: Atributos (datos dentro de un objeto)

```python
class Persona:
    pass

persona1 = Persona()

# Añadir atributos DESPUÉS de crear el objeto
persona1.nombre = "Dan"
persona1.edad = 25

print(persona1.nombre)   # Dan
```

### ✅ Ejemplo Resuelto:

```python
class Perro:
    pass

mi_perro = Perro()
mi_perro.nombre = "Max"
mi_perro.raza = "Golden Retriever"
mi_perro.edad = 3

print(f"Mi perro se llama {mi_perro.nombre}")
```

### 💪 Tu Turno:

1. Crea una clase `Libro` vacía
2. Crea un objeto `mi_libro`
3. Añádele: `titulo`, `autor`, `paginas`
4. Imprime la información

```python
# Escribe tu código aquí


```

---

## Ejercicio 3: El Constructor `__init__` 🏗️

### 📖 Concepto: Inicializar objetos automáticamente

```python
class Persona:
    def __init__(self):
        # 'self' representa el objeto que creamos
        self.nombre = "Dan"
        self.edad = 25

# __init__ se ejecuta automáticamente
persona1 = Persona()
print(persona1.nombre)  # Dan
```

### ✅ Ejemplo con Parámetros:

```python
class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

# Pasamos los valores al crear el objeto
perro1 = Perro("Max", "Golden Retriever", 3)
perro2 = Perro("Luna", "Bulldog", 2)

print(perro1.nombre)  # Max
print(perro2.nombre)  # Luna
```

### 💪 Tu Turno:

Crea una clase `Cancion` con constructor que reciba:
- `titulo`, `artista`, `duracion`

Crea 3 canciones diferentes.

```python
# Escribe tu código aquí


```

---

## Ejercicio 4: Tu Primer Método 🎬

### 📖 Concepto: Métodos (funciones dentro de la clase)

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Método: siempre lleva 'self' como primer parámetro
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

mi_perro = Perro("Max")
mi_perro.ladrar()  # Max dice: ¡Guau!
```

### ✅ Ejemplo con Varios Métodos:

```python
class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 50
    
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")
    
    def comer(self):
        self.hambre -= 20
        print(f"{self.nombre} comiendo. Hambre: {self.hambre}")

mi_gato = Gato("Luna")
mi_gato.maullar()  # Luna dice: ¡Miau!
mi_gato.comer()    # Luna comiendo. Hambre: 30
```

### 💪 Tu Turno:

Crea clase `Coche` con:
- Constructor: `marca`, `modelo`, `velocidad` (=0)
- Método `acelerar()` que sume 10 a velocidad
- Método `frenar()` que reste 10 a velocidad
- Método `mostrar_velocidad()` que imprima la velocidad

```python
# Escribe tu código aquí


```

---

## Ejercicio 5: Métodos con Parámetros 📥

### 📖 Concepto: Métodos que reciben valores

```python
class Calculadora:
    def sumar(self, a, b):
        resultado = a + b
        return resultado

calc = Calculadora()
resultado = calc.sumar(5, 3)
print(resultado)  # 8
```

### ✅ Ejemplo Resuelto:

```python
class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Nuevo saldo: ${self.saldo}")
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Nuevo saldo: ${self.saldo}")
        else:
            print("¡Fondos insuficientes!")

cuenta = CuentaBancaria("Dan")
cuenta.depositar(1000)  # Nuevo saldo: $1000
cuenta.retirar(300)     # Nuevo saldo: $700
```

### 💪 Tu Turno:

Crea clase `Mascota` con:
- Constructor: `nombre`, `energia` (=100)
- `jugar(minutos)` que reste `minutos * 2`
- `dormir(horas)` que sume `horas * 10`
- `mostrar_estado()` que muestre nombre y energía

```python
# Escribe tu código aquí


```

---

## Ejercicio 6: Retornar Valores 🔄

### 📖 Concepto: Usar `return` en métodos

```python
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

rect = Rectangulo(5, 10)
area = rect.calcular_area()
print(f"Área: {area}")  # Área: 50
```

### 💪 Tu Turno:

Crea clase `Estudiante` con:
- Constructor: `nombre`, `calificaciones` (lista vacía)
- `agregar_calificacion(nota)` añade a lista
- `obtener_promedio()` retorna el promedio
- `esta_aprobado()` retorna True si promedio >= 6
- `mejor_nota()` retorna la nota más alta

```python
# Escribe tu código aquí


```

---

## Ejercicio 7: Objetos Interactuando 🤝

### 📖 Concepto: Objetos que se relacionan

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self, otra_persona):
        print(f"{self.nombre} saluda a {otra_persona.nombre}")

dan = Persona("Dan")
alex = Persona("Alex")
dan.saludar(alex)  # Dan saluda a Alex
```

### 💪 Tu Turno:

Crea clase `CuentaBancaria` con:
- Constructor: `titular`, `saldo` (=0)
- `depositar(cantidad)`
- `retirar(cantidad)`
- `transferir(cuenta_destino, cantidad)` que retire de esta cuenta y deposite en la otra

Crea dos cuentas y haz una transferencia.

```python
# Escribe tu código aquí


```

---

## Ejercicio 8: Atributos de Clase 📊

### 📖 Concepto: Atributos compartidos por todos los objetos

```python
class Perro:
    # Atributo de clase (fuera de __init__)
    total_perros = 0
    
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia
        Perro.total_perros += 1

perro1 = Perro("Max")
perro2 = Perro("Luna")
print(Perro.total_perros)  # 2
```

### 💪 Tu Turno:

Crea clase `Producto` con:
- Atributo de clase: `total_productos`
- Constructor: `nombre`, `precio`, `codigo` (auto-generado: "PROD-001", "PROD-002"...)
- Método de clase: `obtener_total()` que retorne cuántos productos hay

```python
# Escribe tu código aquí


```

---

## Ejercicio 9: El Método `__str__` 📝

### 📖 Concepto: Controlar cómo se imprime un objeto

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años"

persona = Persona("Dan", 25)
print(persona)  # Persona: Dan, 25 años
```

### 💪 Tu Turno:

Crea clase `Pokemon` con:
- Constructor: `nombre`, `tipo`, `nivel`, `hp`
- `__str__()` que retorne: "Pikachu (Tipo: Eléctrico) - Nivel 25 - HP: 100"

Crea 3 pokémon e imprímelos.

```python
# Escribe tu código aquí


```

---

## Ejercicio 10: Lista de Objetos 📚

### 📖 Concepto: Guardar objetos en listas

```python
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
    
    def completar(self):
        self.completada = True

tareas = []
tareas.append(Tarea("Estudiar Python"))
tareas.append(Tarea("Hacer ejercicios"))

tareas[0].completar()

for tarea in tareas:
    estado = "✅" if tarea.completada else "⏳"
    print(f"{estado} {tarea.descripcion}")
```

### 💪 Tu Turno:

Crea clase `Contacto` con: `nombre`, `telefono`, `email`

Luego crea lista `agenda` y:
1. Añade 5 contactos
2. Imprime todos
3. Busca uno por nombre
4. Elimina uno

```python
# Escribe tu código aquí


```

---

## Ejercicio 11: Composición 🎁

### 📖 Concepto: Objetos dentro de objetos

```python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def encender(self):
        print(f"Motor {self.tipo} encendido")

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor("V6")  # Objeto dentro de objeto
    
    def arrancar(self):
        self.motor.encender()

coche = Coche("Toyota")
coche.arrancar()  # Motor V6 encendido
```

### 💪 Tu Turno:

Crea:

**Clase `Cancion`:**
- Constructor: `titulo`, `duracion_segundos`

**Clase `Playlist`:**
- Constructor: `nombre`
- Atributo: `canciones` (lista)
- Método: `agregar_cancion(cancion)`
- Método: `duracion_total()` suma todas las duraciones
- Método: `mostrar()` imprime todas las canciones

```python
# Escribe tu código aquí


```

---

## Ejercicio 12: Mini Proyecto Integrador 📚

### 🎯 Combina TODO lo aprendido

**Clase `Libro`:**
- Atributos: `titulo`, `autor`, `isbn`, `disponible` (True)
- Métodos: `prestar()`, `devolver()`, `__str__()`

**Clase `Usuario`:**
- Atributos: `nombre`, `id`, `libros_prestados` (lista)
- Métodos: `tomar_prestado(libro)`, `devolver_libro(libro)`, `mostrar_libros()`

**Clase `Biblioteca`:**
- Atributos: `nombre`, `libros` (lista), `usuarios` (lista)
- Métodos: `agregar_libro()`, `registrar_usuario()`, `buscar_libro(titulo)`, `mostrar_disponibles()`

### Tu Turno:

Implementa las tres clases y:
1. Crea una biblioteca
2. Agrega 5 libros
3. Registra 2 usuarios
4. Haz préstamos
5. Muestra disponibles

```python
# Escribe tu código aquí


```

---

## 🎉 ¡Felicidades!

Si completaste estos ejercicios, ya entiendes:

✅ Clases y objetos  
✅ Constructor `__init__`  
✅ Qué es `self`  
✅ Métodos  
✅ Atributos de clase vs instancia  
✅ `__str__`  
✅ Composición  

---

## 🚀 Próximos Pasos

Ahora estás lista para:
1. Ver el README completo de POO
2. Hacer los ejercicios del archivo de 35 ejercicios
3. Aprender sobre Herencia
4. Estudiar Polimorfismo

---

## 💡 Consejos

- Repite ejercicios que no entiendas
- Escribe en papel cómo fluye el código
- Experimenta: cambia valores, añade prints
- POO es un cambio de mentalidad, toma tiempo

---


**"El experto en algo fue una vez un principiante."**

---

**Creado por:** Dan  
**Fecha:** Noviembre 2025  
**Tiempo estimado:** 6-8 horas
