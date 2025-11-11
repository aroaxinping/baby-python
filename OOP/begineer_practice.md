# Ejercicios de POO para Empezar desde CERO 🌱

## 📌 ¿Cómo usar este archivo?

Este archivo está diseñado para que **nunca hayas visto POO antes**. Cada ejercicio construye sobre el anterior, y los primeros vienen con **ejemplos resueltos** para que veas el patrón.

**⚠️ IMPORTANTE:** No te saltes ejercicios. Cada uno enseña un concepto nuevo que necesitarás para el siguiente.

---

## Fase 1: Tu Primera Clase (Entendiendo lo básico)

### 🔰 Ejercicio 0: Observa este ejemplo (NO lo escribas todavía)

```python
# Esto es una clase - es como un molde para crear objetos
class Perro:
    pass  # pass significa "no hagas nada todavía"

# Esto es crear un objeto (una instancia) de la clase Perro
mi_perro = Perro()

print(mi_perro)  # Imprime algo como: <__main__.Perro object at 0x...>
```

**¿Qué acabas de ver?**
- `class Perro:` crea una clase llamada Perro
- `mi_perro = Perro()` crea un perro específico (un objeto)
- Es como tener el molde (clase) y crear galletas (objetos) con ese molde

**Ahora sí, ¡tu turno!** 👇

---

### ✏️ Ejercicio 1: Crea tu primera clase

Crea una clase llamada `Gato` (vacía, con `pass`), luego crea un objeto llamado `mi_gato`.

```python
# Tu código aquí


# Imprime mi_gato para ver qué pasa
print(mi_gato)
```

**Objetivo:** Entender que `class` crea el molde y `NombreClase()` crea un objeto.

---

### ✏️ Ejercicio 2: Crea varios objetos de la misma clase

Crea una clase llamada `Coche` (vacía), luego crea **tres coches diferentes**: `coche1`, `coche2`, `coche3`.

```python
# Tu código aquí


# Imprime los tres coches
print(coche1)
print(coche2)
print(coche3)
```

**¿Qué notarás?** Cada objeto tiene una dirección de memoria diferente. Son objetos distintos del mismo tipo.

---

## Fase 2: Agregando Datos a las Clases (Atributos)

### 🔰 Ejercicio 3: Observa cómo agregamos datos (EJEMPLO RESUELTO)

```python
class Persona:
    # __init__ es un método especial que se ejecuta cuando creas un objeto
    # Es el "constructor" - construye el objeto
    def __init__(self):  # self se refiere al objeto que estamos creando
        # Creamos atributos (datos) del objeto
        self.nombre = "Ana"
        self.edad = 25

# Creamos una persona
persona1 = Persona()

# Accedemos a sus atributos
print(persona1.nombre)  # Ana
print(persona1.edad)    # 25
```

**¿Qué acabas de ver?**
- `__init__` es como el "nacimiento" del objeto - se ejecuta automáticamente
- `self` es la forma en que el objeto se refiere a sí mismo
- `self.nombre` crea un atributo llamado `nombre` para este objeto
- Usamos `objeto.atributo` para acceder a los datos

**¡Ahora te toca!** 👇

---

### ✏️ Ejercicio 4: Crea una clase con atributos fijos

Crea una clase `Libro` que tenga:
- Un atributo `titulo` con el valor "Python para Todos"
- Un atributo `autor` con el valor "Charles Severance"
- Un atributo `paginas` con el valor 250

Luego crea un objeto `mi_libro` e imprime sus tres atributos.

```python
class Libro:
    def __init__(self):
        # Completa aquí con los tres atributos
        pass

# Crea el objeto
mi_libro = Libro()

# Imprime los atributos
print(mi_libro.titulo)
print(mi_libro.autor)
print(mi_libro.paginas)
```

---

### ✏️ Ejercicio 5: Crea tu tarjeta de presentación

Crea una clase `TarjetaPresentacion` con estos atributos (usa TUS datos):
- `nombre`
- `profesion`
- `ciudad`
- `email`

Crea un objeto e imprime todos los atributos.

```python
# Tu código aquí
```

---

## Fase 3: Atributos Personalizables (Parámetros)

### 🔰 Ejercicio 6: Observa cómo personalizar objetos (EJEMPLO RESUELTO)

```python
class Mascota:
    # Ahora __init__ recibe parámetros además de self
    def __init__(self, nombre_mascota, tipo_mascota):
        # Asignamos los parámetros a los atributos
        self.nombre = nombre_mascota
        self.tipo = tipo_mascota

# Ahora podemos crear mascotas con diferentes datos
mascota1 = Mascota("Firulais", "perro")
mascota2 = Mascota("Michi", "gato")

print(mascota1.nombre)  # Firulais
print(mascota2.nombre)  # Michi
```

**¿Qué cambió?**
- `__init__` ahora recibe parámetros: `nombre_mascota`, `tipo_mascota`
- Al crear el objeto, le pasamos los valores: `Mascota("Firulais", "perro")`
- Cada objeto puede tener datos diferentes

**⚠️ Nota importante:** El primer parámetro SIEMPRE es `self`. Los siguientes son los que tú defines.

---

### ✏️ Ejercicio 7: Crea estudiantes personalizados

Crea una clase `Estudiante` que reciba:
- `nombre`
- `carrera`
- `semestre` (número)

Crea tres estudiantes diferentes y muestra los datos de cada uno.

```python
class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        # Asigna los parámetros a los atributos
        pass

# Crea tres estudiantes con datos diferentes
estudiante1 = Estudiante("Dan", "Data Science", 1)
# Crea estudiante2 y estudiante3 aquí


# Imprime los datos de cada estudiante
print(f"{estudiante1.nombre} estudia {estudiante1.carrera}")
# Imprime los otros dos estudiantes
```

---

### ✏️ Ejercicio 8: Tu lista de reproducción

Crea una clase `Cancion` que reciba:
- `titulo`
- `artista`
- `duracion` (en minutos, puede ser decimal como 3.5)

Crea 3 canciones que te gusten e imprime su información.

```python
# Tu código aquí
```

---

### ✏️ Ejercicio 9: Productos de una tienda

Crea una clase `Producto` que reciba:
- `nombre`
- `precio`
- `cantidad`

Crea 3 productos de una tienda (por ejemplo: manzanas, leche, pan) e imprime su información.

```python
# Tu código aquí
```

---

## Fase 4: Tu Primer Método (Funciones dentro de clases)

### 🔰 Ejercicio 10: Observa cómo agregamos comportamiento (EJEMPLO RESUELTO)

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Esto es un método - una función que pertenece a la clase
    def ladrar(self):  # Los métodos también reciben self
        print(f"{self.nombre} dice: ¡Guau guau!")
    
    def comer(self):
        print(f"{self.nombre} está comiendo...")

# Creamos un perro
mi_perro = Perro("Max")

# Llamamos a sus métodos
mi_perro.ladrar()  # Max dice: ¡Guau guau!
mi_perro.comer()   # Max está comiendo...
```

**¿Qué son los métodos?**
- Son funciones que pertenecen a una clase
- Se definen con `def` dentro de la clase
- Siempre reciben `self` como primer parámetro
- Se llaman con `objeto.metodo()`
- Pueden usar los atributos del objeto con `self.atributo`

---

### ✏️ Ejercicio 11: Gato que maúlla

Crea una clase `Gato` que:
- Reciba `nombre` en el constructor
- Tenga un método `maullar()` que imprima "[nombre] dice: ¡Miau!"
- Tenga un método `dormir()` que imprima "[nombre] está durmiendo... zzz"

Crea un gato y haz que maúlle y duerma.

```python
class Gato:
    def __init__(self, nombre):
        # Tu código aquí
        pass
    
    def maullar(self):
        # Tu código aquí
        pass
    
    def dormir(self):
        # Tu código aquí
        pass

# Crea un gato
mi_gato = Gato("Luna")

# Llama a los métodos
mi_gato.maullar()
mi_gato.dormir()
```

---

### ✏️ Ejercicio 12: Persona que se presenta

Crea una clase `Persona` que:
- Reciba `nombre` y `edad` en el constructor
- Tenga un método `saludar()` que imprima "Hola, soy [nombre]"
- Tenga un método `decir_edad()` que imprima "Tengo [edad] años"

```python
# Tu código aquí
```

---

### ✏️ Ejercicio 13: Coche que acelera

Crea una clase `Coche` que:
- Reciba `marca` y `modelo` en el constructor
- Tenga un método `arrancar()` que imprima "El [marca] [modelo] está arrancando..."
- Tenga un método `tocar_bocina()` que imprima "¡Beep beep!"

```python
# Tu código aquí
```

---

## Fase 5: Métodos que Modifican Atributos

### 🔰 Ejercicio 14: Observa cómo los métodos cambian datos (EJEMPLO RESUELTO)

```python
class Contador:
    def __init__(self):
        self.valor = 0  # Empieza en 0
    
    def incrementar(self):
        # self.valor accede al atributo
        self.valor = self.valor + 1
        # También puedes escribir: self.valor += 1
    
    def mostrar(self):
        print(f"Valor actual: {self.valor}")

# Creamos un contador
mi_contador = Contador()
mi_contador.mostrar()  # Valor actual: 0

# Incrementamos
mi_contador.incrementar()
mi_contador.mostrar()  # Valor actual: 1

mi_contador.incrementar()
mi_contador.incrementar()
mi_contador.mostrar()  # Valor actual: 3
```

**¿Qué pasó?**
- Los métodos pueden leer atributos con `self.atributo`
- Los métodos pueden modificar atributos con `self.atributo = nuevo_valor`
- Los cambios se mantienen en el objeto

---

### ✏️ Ejercicio 15: Lámpara que se enciende y apaga

Crea una clase `Lampara` que:
- Tenga un atributo `encendida` que empiece en `False`
- Tenga un método `encender()` que cambie `encendida` a `True` y muestre "Lámpara encendida"
- Tenga un método `apagar()` que cambie `encendida` a `False` y muestre "Lámpara apagada"
- Tenga un método `estado()` que muestre si está encendida o apagada

```python
class Lampara:
    def __init__(self):
        # Empieza apagada
        self.encendida = False
    
    def encender(self):
        # Completa aquí
        pass
    
    def apagar(self):
        # Completa aquí
        pass
    
    def estado(self):
        if self.encendida:
            print("La lámpara está encendida")
        else:
            print("La lámpara está apagada")

# Prueba tu clase
mi_lampara = Lampara()
mi_lampara.estado()
mi_lampara.encender()
mi_lampara.estado()
mi_lampara.apagar()
mi_lampara.estado()
```

---

### ✏️ Ejercicio 16: Termómetro

Crea una clase `Termometro` que:
- Tenga un atributo `temperatura` que empiece en 20
- Tenga un método `subir(grados)` que aumente la temperatura
- Tenga un método `bajar(grados)` que disminuya la temperatura
- Tenga un método `mostrar()` que imprima la temperatura actual

```python
# Tu código aquí
```

---

### ✏️ Ejercicio 17: Cuenta bancaria simple

Crea una clase `Cuenta` que:
- Tenga un atributo `saldo` que empiece en 0
- Tenga un método `depositar(cantidad)` que aumente el saldo
- Tenga un método `retirar(cantidad)` que disminuya el saldo
- Tenga un método `consultar()` que muestre el saldo actual

```python
# Tu código aquí
```

---

## Fase 6: Métodos que Retornan Valores

### 🔰 Ejercicio 18: Observa métodos que devuelven valores (EJEMPLO RESUELTO)

```python
class Calculadora:
    def sumar(self, a, b):
        # return devuelve un valor que podemos guardar o usar
        return a + b
    
    def restar(self, a, b):
        return a - b

# Creamos la calculadora
calc = Calculadora()

# Llamamos a los métodos y guardamos los resultados
resultado1 = calc.sumar(5, 3)
resultado2 = calc.restar(10, 4)

print(resultado1)  # 8
print(resultado2)  # 6

# También podemos usar el resultado directamente
print(calc.sumar(2, 2))  # 4
```

**Diferencia importante:**
- `print()` solo muestra en pantalla
- `return` devuelve un valor que puedes guardar o usar
- Métodos con `return` son más flexibles

---

### ✏️ Ejercicio 19: Rectángulo con cálculos

Crea una clase `Rectangulo` que:
- Reciba `base` y `altura` en el constructor
- Tenga un método `calcular_area()` que **retorne** el área (base × altura)
- Tenga un método `calcular_perimetro()` que **retorne** el perímetro (2 × (base + altura))

```python
class Rectangulo:
    def __init__(self, base, altura):
        # Tu código aquí
        pass
    
    def calcular_area(self):
        # Tu código aquí
        pass
    
    def calcular_perimetro(self):
        # Tu código aquí
        pass

# Prueba tu clase
rect = Rectangulo(5, 3)
print(f"Área: {rect.calcular_area()}")
print(f"Perímetro: {rect.calcular_perimetro()}")
```

---

### ✏️ Ejercicio 20: Círculo

Crea una clase `Circulo` que:
- Reciba `radio` en el constructor
- Tenga un método `calcular_area()` que retorne π × radio² (usa 3.14159 para π)
- Tenga un método `calcular_circunferencia()` que retorne 2 × π × radio

```python
# Tu código aquí
```

---

### ✏️ Ejercicio 21: Conversión de temperatura

Crea una clase `ConversorTemperatura` que:
- Tenga un método `celsius_a_fahrenheit(celsius)` que retorne la conversión
  - Fórmula: (celsius × 9/5) + 32
- Tenga un método `fahrenheit_a_celsius(fahrenheit)` que retorne la conversión
  - Fórmula: (fahrenheit - 32) × 5/9

```python
# Tu código aquí
```

---

## Fase 7: Validaciones y Lógica en Métodos

### 🔰 Ejercicio 22: Métodos con validación (EJEMPLO RESUELTO)

```python
class CuentaBanco:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    
    def retirar(self, cantidad):
        # Validamos antes de hacer el retiro
        if cantidad > self.saldo:
            print("⚠️ No tienes suficiente dinero")
            return False  # Retornamos False si no se pudo
        else:
            self.saldo = self.saldo - cantidad
            print(f"✅ Retiraste ${cantidad}. Saldo: ${self.saldo}")
            return True  # Retornamos True si sí se pudo
    
    def depositar(self, cantidad):
        if cantidad <= 0:
            print("⚠️ La cantidad debe ser positiva")
            return False
        else:
            self.saldo = self.saldo + cantidad
            print(f"✅ Depositaste ${cantidad}. Saldo: ${self.saldo}")
            return True

# Probamos
cuenta = CuentaBanco(100)
cuenta.retirar(30)   # ✅ Retiraste $30. Saldo: $70
cuenta.retirar(100)  # ⚠️ No tienes suficiente dinero
cuenta.depositar(-10)  # ⚠️ La cantidad debe ser positiva
```

**Concepto clave:** Validar antes de modificar datos.

---

### ✏️ Ejercicio 23: Edad válida

Crea una clase `Persona` que:
- Reciba `nombre` y `edad` en el constructor
- En el constructor, valida que la edad esté entre 0 y 120
- Si la edad no es válida, establécela en 0 y muestra un mensaje de error
- Tenga un método `cumplir_años()` que aumente la edad en 1
- Tenga un método `mostrar_info()` que muestre nombre y edad

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        # Valida la edad aquí
        if edad < 0 or edad > 120:
            print("⚠️ Edad inválida, establecida en 0")
            self.edad = 0
        else:
            self.edad = edad
    
    def cumplir_años(self):
        # Tu código aquí
        pass
    
    def mostrar_info(self):
        # Tu código aquí
        pass

# Prueba con diferentes edades
persona1 = Persona("Dan", 25)
persona2 = Persona("Ana", 150)  # Edad inválida
persona1.mostrar_info()
persona2.mostrar_info()
```

---

### ✏️ Ejercicio 24: Stock de producto

Crea una clase `Producto` que:
- Reciba `nombre`, `precio` y `stock` en el constructor
- Tenga un método `vender(cantidad)` que:
  - Verifique si hay suficiente stock
  - Si hay, reduzca el stock y retorne el total de la venta (precio × cantidad)
  - Si no hay, muestre un mensaje y retorne 0
- Tenga un método `agregar_stock(cantidad)` que aumente el stock

```python
# Tu código aquí
```

---

### ✏️ Ejercicio 25: Calificación de estudiante

Crea una clase `Estudiante` que:
- Reciba `nombre` en el constructor
- Tenga un atributo `calificacion` que empiece en 0
- Tenga un método `establecer_calificacion(nota)` que:
  - Solo acepte notas entre 0 y 10
  - Si es válida, la guarde
  - Si no es válida, muestre un error
- Tenga un método `aprobo()` que retorne `True` si la nota es >= 6, `False` si no
- Tenga un método `letra_calificacion()` que retorne:
  - "Excelente" si es >= 9
  - "Bueno" si es >= 7
  - "Suficiente" si es >= 6
  - "Reprobado" si es < 6

```python
# Tu código aquí
```

---

## Fase 8: Combinando Todo lo Aprendido

### ✏️ Ejercicio 26: Lista de tareas completa

Crea una clase `ListaTareas` que:
- Tenga un atributo `tareas` que sea una lista vacía
- Tenga un método `agregar(tarea)` que agregue una tarea a la lista
- Tenga un método `completar(indice)` que elimine la tarea en ese índice
  - Valida que el índice exista
- Tenga un método `mostrar_todas()` que imprima todas las tareas numeradas
- Tenga un método `total()` que retorne cuántas tareas hay

```python
class ListaTareas:
    def __init__(self):
        # Tu código aquí
        pass
    
    def agregar(self, tarea):
        # Tu código aquí
        pass
    
    def completar(self, indice):
        # Tu código aquí (recuerda validar)
        pass
    
    def mostrar_todas(self):
        # Tu código aquí
        pass
    
    def total(self):
        # Tu código aquí
        pass

# Prueba tu clase
mis_tareas = ListaTareas()
mis_tareas.agregar("Estudiar Python")
mis_tareas.agregar("Hacer ejercicio")
mis_tareas.agregar("Cocinar")
mis_tareas.mostrar_todas()
print(f"Total de tareas: {mis_tareas.total()}")
mis_tareas.completar(1)  # Completa "Hacer ejercicio"
mis_tareas.mostrar_todas()
```

---

### ✏️ Ejercicio 27: Juego de dado

Crea una clase `Dado` que:
- Tenga un atributo `caras` (por defecto 6)
- Tenga un atributo `ultimo_valor` que guarde el último número que salió
- Tenga un método `lanzar()` que:
  - Genere un número aleatorio entre 1 y el número de caras (usa `import random`)
  - Guarde ese número en `ultimo_valor`
  - Retorne el número
- Tenga un método `lanzar_varias(veces)` que lance el dado varias veces y retorne la suma

```python
import random

class Dado:
    def __init__(self, caras=6):
        # Tu código aquí
        pass
    
    def lanzar(self):
        # Tu código aquí
        # Pista: random.randint(1, self.caras)
        pass
    
    def lanzar_varias(self, veces):
        # Tu código aquí
        pass

# Prueba
dado = Dado()
print(f"Lanzamiento: {dado.lanzar()}")
print(f"Último valor: {dado.ultimo_valor}")
print(f"Suma de 3 lanzamientos: {dado.lanzar_varias(3)}")
```

---

### ✏️ Ejercicio 28: Carrito de compras

Crea una clase `Carrito` que:
- Tenga un atributo `productos` (lista vacía) para guardar nombres de productos
- Tenga un atributo `precios` (lista vacía) para guardar los precios correspondientes
- Tenga un método `agregar(producto, precio)` que agregue a ambas listas
- Tenga un método `eliminar(producto)` que elimine el producto y su precio
- Tenga un método `calcular_total()` que retorne la suma de todos los precios
- Tenga un método `mostrar()` que muestre todos los productos con sus precios

```python
# Tu código aquí
```

---

### ✏️ Ejercicio 29: Mascota virtual (Tamagotchi)

Crea una clase `MascotaVirtual` que:
- Reciba `nombre` en el constructor
- Tenga atributos: `hambre` (0-100, empieza en 50), `felicidad` (0-100, empieza en 50), `energia` (0-100, empieza en 100)
- Tenga un método `alimentar()` que:
  - Reduzca hambre en 20 (mínimo 0)
  - Aumente energía en 10 (máximo 100)
- Tenga un método `jugar()` que:
  - Aumente felicidad en 20 (máximo 100)
  - Aumente hambre en 15
  - Reduzca energía en 20
  - No permita jugar si energía < 20
- Tenga un método `dormir()` que ponga energía en 100
- Tenga un método `estado()` que muestre todos los atributos
- Tenga un método `necesita_atencion()` que retorne `True` si hambre > 80 o felicidad < 30 o energía < 30

```python
# Tu código aquí
```

---

### ✏️ Ejercicio 30: Cuenta bancaria completa

Crea una clase `CuentaBancaria` que:
- Reciba `titular` y `saldo_inicial` en el constructor
- Tenga un método `depositar(cantidad)` con validación
- Tenga un método `retirar(cantidad)` con validación de fondos
- Tenga un método `transferir(cuenta_destino, cantidad)` que:
  - Retire de esta cuenta
  - Deposite en la cuenta destino
  - Solo funcione si hay fondos suficientes
- Tenga un método `resumen()` que muestre titular y saldo
- Tenga un atributo `historial` (lista) que guarde todas las operaciones

```python
# Tu código aquí
```

---

## 🎯 ¿Qué has aprendido hasta aquí?

Después de completar estos 30 ejercicios, ya sabes:

✅ **Qué es una clase** y cómo crearla  
✅ **Qué es un objeto** y cómo instanciarlo  
✅ **Qué es `self`** y por qué lo usamos  
✅ **Qué es `__init__`** y cómo funciona el constructor  
✅ **Qué son los atributos** y cómo crearlos  
✅ **Qué son los métodos** y cómo definirlos  
✅ **Cómo los métodos modifican atributos**  
✅ **Cómo los métodos retornan valores**  
✅ **Cómo validar datos** en los métodos  
✅ **Cómo combinar todo** en clases más complejas  

---

## 🚀 Próximos Pasos

Ahora que dominas los fundamentos, estás lista para:

1. **Practicar más** con el archivo de ejercicios intermedios
2. **Aprender sobre herencia** (clases que heredan de otras)
3. **Entender encapsulación** (atributos privados)
4. **Explorar polimorfismo** (diferentes clases con los mismos métodos)
5. **Crear tus propios proyectos** desde cero

---

## 💡 Consejos para Practicar

### ✨ Mientras resuelves ejercicios:

1. **Escribe el código TÚ MISMA** - no copies y pegues
2. **Prueba cada método** que crees
3. **Experimenta** - cambia valores, rompe cosas, aprende
4. **Si te atascas**, vuelve al ejemplo resuelto anterior
5. **Celebra cada ejercicio completado** 🎉

### 🧠 Para memorizar conceptos:

- `class NombreClase:` → Define el molde
- `__init__(self, parametros):` → Constructor, "nace" el objeto
- `self.atributo = valor` → Crear o modificar atributo
- `def metodo(self):` → Definir comportamiento
- `objeto.metodo()` → Llamar al comportamiento
- `return valor` → Devolver resultado

### 📝 Práctica adicional:

Después de cada 5 ejercicios, crea TU PROPIA clase relacionada con algo que te guste:
- Si te gusta la música → clase `Playlist` o `Instrumento`
- Si te gusta cocinar → clase `Receta` o `Ingrediente`
- Si te gusta viajar → clase `Destino` o `Viaje`
- Si te gustan las plantas → clase `Planta` o `Jardin`

---

## ❤️ Mensaje Final

Dan, estos ejercicios están diseñados específicamente para que no te sientas perdida. Cada uno construye sobre el anterior, y los conceptos se introducen de uno en uno.

**No tengas prisa.** Es mejor entender bien 5 ejercicios que hacer 30 sin entender.

**Recuerda:** Todos los programadores expertos empezaron exactamente donde estás tú ahora. La diferencia es que ellos siguieron practicando.

**¡Tú puedes hacerlo!** 💪✨

---

**Creado especialmente para:** Dan  
**Fecha:** Noviembre 2025  
**Tiempo estimado:** 2-3 semanas (tomándote tu tiempo)  

**¡A practicar! 🚀**
