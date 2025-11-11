# Programación Orientada a Objetos en Python 🐍

## Tabla de Contenidos

- [¿Qué es la Programación Orientada a Objetos?](#qué-es-la-programación-orientada-a-objetos)
- [Los 4 Pilares Fundamentales de la POO](#los-4-pilares-fundamentales-de-la-poo)
  - [1. Encapsulación](#1-encapsulación)
  - [2. Abstracción](#2-abstracción)
  - [3. Herencia](#3-herencia)
  - [4. Polimorfismo](#4-polimorfismo)
- [Conceptos Clave en Python](#conceptos-clave-en-python)
- [Ejemplo Práctico Completo](#ejemplo-práctico-completo)
- [Ventajas de la POO](#ventajas-de-la-poo)
- [Cuándo Usar POO](#cuándo-usar-poo)
- [Consejos para Tu Aprendizaje](#consejos-para-tu-aprendizaje)

---

## ¿Qué es la Programación Orientada a Objetos?

La **Programación Orientada a Objetos (POO)** es un paradigma de programación que organiza el código en torno a "objetos" en lugar de funciones y lógica. Un objeto combina datos (atributos) y comportamientos (métodos) en una sola entidad.

**Analogía:** Imagina que estás construyendo un videojuego. En lugar de tener variables sueltas como `jugador_nombre`, `jugador_vida`, `jugador_nivel` y funciones separadas, la POO te permite crear un objeto "Jugador" que agrupa toda esta información y funcionalidad en un solo lugar.

---

## Los 4 Pilares Fundamentales de la POO

### 1. Encapsulación

La encapsulación significa agrupar datos y métodos relacionados dentro de una clase, y controlar el acceso a ellos. Es como tener una caja con compartimentos: algunos son públicos, otros privados.

**¿Por qué es importante?** Protege los datos sensibles y previene que se modifiquen de formas no previstas.

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # self.titular es un atributo público (puede accederse desde fuera)
        self.titular = titular
        
        # self.__saldo es un atributo privado (el __ lo hace privado)
        # No puede accederse directamente desde fuera de la clase
        self.__saldo = saldo_inicial
    
    def depositar(self, cantidad):
        """Método para depositar dinero de forma controlada"""
        if cantidad > 0:
            self.__saldo += cantidad  # Modificamos el saldo de forma segura
            return f"Depósito exitoso. Nuevo saldo: ${self.__saldo}"
        return "Cantidad inválida"
    
    def retirar(self, cantidad):
        """Método para retirar dinero con validación"""
        # Verificamos que haya fondos suficientes antes de retirar
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: ${self.__saldo}"
        return "Fondos insuficientes o cantidad inválida"
    
    def consultar_saldo(self):
        """Método público para ver el saldo de forma segura"""
        return f"Saldo actual: ${self.__saldo}"

# === USO ===
mi_cuenta = CuentaBancaria("Dan", 1000)
print(mi_cuenta.depositar(500))        # Depósito exitoso. Nuevo saldo: $1500
print(mi_cuenta.consultar_saldo())     # Saldo actual: $1500

# Esto NO funcionará (el saldo está protegido):
# print(mi_cuenta.__saldo)  # AttributeError

# La única forma de acceder al saldo es a través de los métodos públicos
```

---

### 2. Abstracción

La abstracción significa mostrar solo lo esencial y ocultar los detalles complejos. Es como usar un coche: no necesitas saber cómo funciona el motor internamente, solo necesitas saber acelerar y frenar.

```python
from abc import ABC, abstractmethod

# ABC = Abstract Base Class (Clase Base Abstracta)
class DispositivoElectronico(ABC):
    """
    Clase abstracta que define la interfaz básica para dispositivos.
    No puede ser instanciada directamente, solo sirve como plantilla.
    """
    
    @abstractmethod
    def encender(self):
        """Método abstracto: todas las clases hijas DEBEN implementarlo"""
        pass
    
    @abstractmethod
    def apagar(self):
        """Método abstracto: todas las clases hijas DEBEN implementarlo"""
        pass

class Telefono(DispositivoElectronico):
    """Clase concreta que implementa la abstracción"""
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    # Implementamos los métodos abstractos
    def encender(self):
        """Implementación específica de encender para teléfonos"""
        self.encendido = True
        return f"{self.marca} {self.modelo} encendido"
    
    def apagar(self):
        """Implementación específica de apagar para teléfonos"""
        self.encendido = False
        return f"{self.marca} {self.modelo} apagado"
    
    def llamar(self, numero):
        """Método específico de la clase Telefono"""
        if self.encendido:
            return f"Llamando a {numero}..."
        return "El teléfono está apagado"

# === USO ===
# Esto daría error (no podemos instanciar una clase abstracta):
# dispositivo = DispositivoElectronico()  # TypeError

# Pero podemos instanciar la clase concreta:
mi_telefono = Telefono("Samsung", "Galaxy S24")
print(mi_telefono.encender())           # Samsung Galaxy S24 encendido
print(mi_telefono.llamar("123456789"))  # Llamando a 123456789...
```

---

### 3. Herencia

La herencia permite crear nuevas clases basadas en clases existentes, reutilizando y extendiendo su funcionalidad. Es como un árbol genealógico: los hijos heredan características de los padres.

```python
class Animal:
    """Clase base o padre - define características comunes"""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        """Método genérico que será sobrescrito por las clases hijas"""
        return "Algún sonido genérico"
    
    def dormir(self):
        """Método común para todos los animales"""
        return f"{self.nombre} está durmiendo"

class Perro(Animal):
    """Clase derivada o hija que hereda de Animal"""
    
    def __init__(self, nombre, edad, raza):
        # super() llama al constructor de la clase padre (Animal)
        # Así reutilizamos el código del padre
        super().__init__(nombre, edad)
        
        # Agregamos un atributo específico de Perro
        self.raza = raza
    
    def hacer_sonido(self):
        """Sobrescribimos el método del padre con comportamiento específico"""
        return "¡Guau guau!"
    
    def traer_pelota(self):
        """Método nuevo, específico de la clase Perro"""
        return f"{self.nombre} está trayendo la pelota"

class Gato(Animal):
    """Otra clase hija con su propia implementación"""
    
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def hacer_sonido(self):
        """El gato tiene su propio sonido"""
        return "¡Miau!"
    
    def ronronear(self):
        """Método específico de los gatos"""
        return f"{self.nombre} está ronroneando"

# === USO ===
mi_perro = Perro("Max", 3, "Golden Retriever")
mi_gato = Gato("Luna", 2, "Gris")

# Cada animal hace su propio sonido (polimorfismo)
print(mi_perro.hacer_sonido())  # ¡Guau guau!
print(mi_gato.hacer_sonido())   # ¡Miau!

# Pero ambos pueden dormir (método heredado)
print(mi_perro.dormir())        # Max está durmiendo
print(mi_gato.dormir())         # Luna está durmiendo

# Métodos específicos de cada clase
print(mi_perro.traer_pelota())  # Max está trayendo la pelota
print(mi_gato.ronronear())      # Luna está ronroneando
```

---

### 4. Polimorfismo

El polimorfismo significa "muchas formas". Permite que diferentes clases respondan al mismo método de maneras diferentes. Es como pedirle a diferentes animales que "hablen": cada uno hará su propio sonido.

```python
class Forma:
    """Clase base para todas las formas geométricas"""
    
    def area(self):
        """Método que será implementado por cada forma específica"""
        pass
    
    def perimetro(self):
        """Método que será implementado por cada forma específica"""
        pass

class Rectangulo(Forma):
    """Implementación específica para rectángulos"""
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        """Cálculo del área: base × altura"""
        return self.base * self.altura
    
    def perimetro(self):
        """Cálculo del perímetro: 2 × (base + altura)"""
        return 2 * (self.base + self.altura)

class Circulo(Forma):
    """Implementación específica para círculos"""
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        """Cálculo del área: π × radio²"""
        return 3.14159 * self.radio ** 2
    
    def perimetro(self):
        """Cálculo del perímetro: 2 × π × radio"""
        return 2 * 3.14159 * self.radio

# === POLIMORFISMO EN ACCIÓN ===
def calcular_area_total(formas):
    """
    Esta función acepta cualquier objeto que tenga un método area().
    No le importa si es un Rectángulo, Círculo, Triángulo, etc.
    Esto es polimorfismo: diferentes formas, misma interfaz.
    """
    total = 0
    for forma in formas:
        # Cada forma calcula su área de manera diferente
        total += forma.area()
    return total

# === USO ===
rectangulo = Rectangulo(5, 10)
circulo = Circulo(7)

# Ambos objetos son diferentes pero tienen la misma interfaz (método area)
formas = [rectangulo, circulo]

# La función no necesita saber qué tipo de forma es cada objeto
print(f"Área total: {calcular_area_total(formas)}")  # Área total: 203.93754

# Esto es polimorfismo: diferentes objetos responden al mismo método
print(f"Área del rectángulo: {rectangulo.area()}")  # 50
print(f"Área del círculo: {circulo.area()}")        # 153.93754
```

---

## Conceptos Clave en Python

### Clases y Objetos

Una **clase** es como un plano o molde, mientras que un **objeto** es una instancia específica creada a partir de ese molde.

```python
class Estudiante:
    """
    Una clase define las características y comportamientos
    que tendrán todos los estudiantes.
    """
    
    # Atributo de clase: compartido por TODAS las instancias
    # Todos los estudiantes van a la misma institución
    institucion = "UOC"
    
    def __init__(self, nombre, carrera):
        """
        Constructor: se ejecuta automáticamente cuando creamos un estudiante.
        Define los atributos de instancia (únicos para cada objeto).
        """
        self.nombre = nombre           # Atributo de instancia
        self.carrera = carrera         # Atributo de instancia
        self.calificaciones = []       # Lista vacía para cada estudiante
    
    def agregar_calificacion(self, calificacion):
        """Método para agregar una calificación a la lista del estudiante"""
        self.calificaciones.append(calificacion)
    
    def promedio(self):
        """Método que calcula el promedio de calificaciones"""
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0
    
    def __str__(self):
        """
        Método especial que define cómo se representa el objeto como string.
        Se llama automáticamente cuando usamos print() o str().
        """
        return f"{self.nombre} - {self.carrera}"

# === CREAR OBJETOS (INSTANCIAS) ===
# Cada objeto es independiente, con sus propios datos
estudiante1 = Estudiante("Dan", "Data Science")
estudiante2 = Estudiante("Alex", "Computer Science")

# Cada estudiante tiene sus propias calificaciones
estudiante1.agregar_calificacion(8.5)
estudiante1.agregar_calificacion(9.0)
estudiante2.agregar_calificacion(7.5)

# Cada uno tiene su propio promedio
print(f"Promedio de {estudiante1.nombre}: {estudiante1.promedio()}")  # 8.75
print(f"Promedio de {estudiante2.nombre}: {estudiante2.promedio()}")  # 7.5

# Pero ambos comparten el atributo de clase
print(estudiante1.institucion)  # UOC
print(estudiante2.institucion)  # UOC
```

---

### El Constructor `__init__`

El método `__init__` es un método especial (constructor) que se ejecuta automáticamente cuando creas un nuevo objeto. Sirve para inicializar los atributos del objeto.

```python
class Libro:
    """
    Clase para representar un libro con funcionalidad de lectura.
    """
    
    def __init__(self, titulo, autor, paginas):
        """
        Constructor: se ejecuta automáticamente al crear un Libro.
        
        Parámetros:
            titulo (str): El título del libro
            autor (str): El autor del libro
            paginas (int): Número total de páginas
        """
        # Inicializamos los atributos del objeto
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0  # Empezamos en la página 0
    
    def leer(self, num_paginas):
        """
        Método para simular la lectura de páginas.
        Verifica que no excedamos el número de páginas del libro.
        """
        # Calculamos si podemos leer esas páginas
        if self.pagina_actual + num_paginas <= self.paginas:
            self.pagina_actual += num_paginas
            return f"Leíste {num_paginas} páginas. Estás en la página {self.pagina_actual}"
        return "No hay tantas páginas en el libro"

# === USO ===
# Al crear el objeto, __init__ se ejecuta automáticamente
mi_libro = Libro("Python para Data Science", "Jake VanderPlas", 500)

print(mi_libro.leer(50))   # Leíste 50 páginas. Estás en la página 50
print(mi_libro.leer(100))  # Leíste 100 páginas. Estás en la página 150
print(mi_libro.leer(500))  # No hay tantas páginas en el libro
```

---

### `self` - La Referencia al Objeto Actual

`self` es una referencia al objeto actual. Permite acceder a los atributos y métodos del objeto desde dentro de la clase.

```python
class Contador:
    """
    Clase simple para demostrar el uso de self.
    """
    
    def __init__(self):
        """
        self se refiere al objeto que estamos creando.
        self.valor crea un atributo 'valor' para este objeto específico.
        """
        self.valor = 0  # self.valor es un atributo del objeto
    
    def incrementar(self):
        """
        self nos permite acceder al atributo valor del objeto actual.
        Sin self, Python no sabría a qué 'valor' nos referimos.
        """
        self.valor += 1  # Accedemos al atributo usando self
    
    def obtener_valor(self):
        """self nos permite retornar el valor del atributo"""
        return self.valor  # Retornamos el valor del atributo

# === USO ===
# Cada contador es independiente
contador1 = Contador()
contador2 = Contador()

# Incrementamos solo contador1
contador1.incrementar()
contador1.incrementar()

# Cada uno mantiene su propio valor
print(contador1.obtener_valor())  # 2
print(contador2.obtener_valor())  # 0

# self hace que cada objeto tenga sus propios datos
```

---

### Métodos Especiales (Magic Methods)

Python tiene métodos especiales que comienzan y terminan con doble guion bajo `__`. Estos permiten que tus objetos se comporten de maneras especiales.

```python
class Vector:
    """
    Clase para representar vectores matemáticos 2D.
    Demuestra el uso de métodos especiales.
    """
    
    def __init__(self, x, y):
        """Constructor: inicializa las coordenadas del vector"""
        self.x = x
        self.y = y
    
    def __str__(self):
        """
        Se llama cuando usas print() o str() con el objeto.
        Debe retornar una representación legible para humanos.
        """
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """
        Representación oficial del objeto.
        Se usa en el intérprete y para debugging.
        """
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, otro):
        """
        Se llama cuando usas el operador +
        Permite hacer: vector1 + vector2
        """
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __eq__(self, otro):
        """
        Se llama cuando usas el operador ==
        Permite hacer: vector1 == vector2
        """
        return self.x == otro.x and self.y == otro.y
    
    def __len__(self):
        """
        Se llama cuando usas len()
        Retorna la magnitud del vector.
        """
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

# === USO ===
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# __str__ se llama automáticamente con print()
print(v1)           # Vector(3, 4)

# __add__ se llama automáticamente con el operador +
v3 = v1 + v2        # Internamente llama v1.__add__(v2)
print(v3)           # Vector(4, 6)

# __eq__ se llama automáticamente con el operador ==
print(v1 == v2)     # False (llama v1.__eq__(v2))

# __len__ se llama con len()
print(len(v1))      # 5 (magnitud del vector 3,4)
```

---

### Herencia Múltiple

Python permite que una clase herede de múltiples clases padres.

```python
class Volador:
    """Primera clase padre: define la capacidad de volar"""
    
    def volar(self):
        """Método que define cómo vuela"""
        return "Estoy volando"

class Nadador:
    """Segunda clase padre: define la capacidad de nadar"""
    
    def nadar(self):
        """Método que define cómo nada"""
        return "Estoy nadando"

class Pato(Volador, Nadador):
    """
    Clase que hereda de AMBAS clases padre.
    Un pato puede tanto volar como nadar.
    """
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        """Método propio de la clase Pato"""
        return "¡Cuac!"

# === USO ===
donald = Pato("Donald")

# El pato tiene métodos de ambas clases padre
print(donald.volar())        # Heredado de Volador
print(donald.nadar())        # Heredado de Nadador
print(donald.hacer_sonido()) # Método propio de Pato

# Esto es herencia múltiple: una clase hereda de varias clases
```

---

### Propiedades y Decoradores

Los decoradores `@property`, `@getter` y `@setter` permiten controlar el acceso a los atributos de manera elegante.

```python
class Temperatura:
    """
    Clase que demuestra el uso de propiedades para
    controlar el acceso y validación de atributos.
    """
    
    def __init__(self, celsius=0):
        """Inicializamos con celsius"""
        self._celsius = celsius  # El _ indica que es "privado por convención"
    
    @property
    def celsius(self):
        """
        Getter: se llama cuando accedemos a temperatura.celsius
        El decorador @property convierte el método en una propiedad.
        """
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        """
        Setter: se llama cuando asignamos temperatura.celsius = valor
        Nos permite validar el valor antes de asignarlo.
        """
        if valor < -273.15:
            # Validación: no permitimos temperaturas imposibles
            raise ValueError("La temperatura no puede ser menor a -273.15°C (cero absoluto)")
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        """
        Propiedad calculada automáticamente desde celsius.
        Se llama cuando accedemos a temperatura.fahrenheit
        """
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        """
        Setter para fahrenheit: convierte a celsius internamente.
        Podemos asignar en fahrenheit y se guarda en celsius.
        """
        self._celsius = (valor - 32) * 5/9

# === USO ===
temp = Temperatura(25)

# Accedemos como si fueran atributos simples, pero hay lógica detrás
print(temp.celsius)      # 25 (llama al getter)
print(temp.fahrenheit)   # 77.0 (se calcula automáticamente)

# Asignamos y la validación se ejecuta automáticamente
temp.fahrenheit = 86     # Llama al setter
print(temp.celsius)      # 30.0 (se convirtió automáticamente)

# Intento de asignar un valor inválido
try:
    temp.celsius = -300  # Esto lanzará un ValueError
except ValueError as e:
    print(e)  # La temperatura no puede ser menor a -273.15°C
```

---

### Métodos de Clase y Métodos Estáticos

```python
class Empleado:
    """
    Clase que demuestra tres tipos de métodos:
    - Métodos de instancia (usan self)
    - Métodos de clase (usan cls)
    - Métodos estáticos (no usan ni self ni cls)
    """
    
    # Atributos de clase: compartidos por todas las instancias
    aumento_salarial = 1.05  # 5% de aumento
    num_empleados = 0        # Contador de empleados
    
    def __init__(self, nombre, salario):
        """Constructor: método de instancia"""
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1  # Incrementamos el contador
    
    def aplicar_aumento(self):
        """
        Método de instancia: trabaja con datos del objeto (self).
        Aplica el aumento al salario de ESTE empleado específico.
        """
        self.salario = int(self.salario * self.aumento_salarial)
    
    @classmethod
    def establecer_aumento(cls, cantidad):
        """
        Método de clase: trabaja con la clase misma (cls), no con instancias.
        El decorador @classmethod hace que reciba cls en lugar de self.
        Cambia el aumento para TODOS los empleados.
        """
        cls.aumento_salarial = cantidad
    
    @classmethod
    def desde_string(cls, empleado_str):
        """
        Constructor alternativo: método de clase.
        Crea un empleado desde un string con formato "Nombre-Salario".
        cls() llama al constructor __init__.
        """
        nombre, salario = empleado_str.split('-')
        return cls(nombre, int(salario))  # Retorna un nuevo objeto Empleado
    
    @staticmethod
    def es_dia_laboral(dia):
        """
        Método estático: no accede ni a la instancia (self) ni a la clase (cls).
        Es como una función normal, pero está dentro de la clase por organización.
        Verifica si un día es laboral (lunes-viernes).
        """
        return dia.weekday() < 5  # 0-4 son lunes-viernes

# === USO ===

# Crear empleados de forma normal
emp1 = Empleado("Ana", 50000)

# Usar el constructor alternativo (método de clase)
emp2 = Empleado.desde_string("Luis-60000")

# Cambiar el aumento para TODA la clase
Empleado.establecer_aumento(1.10)  # 10% de aumento

# Aplicar aumento a un empleado específico
emp1.aplicar_aumento()
print(f"Nuevo salario de Ana: ${emp1.salario}")  # $55000 (50000 * 1.10)

# Usar método estático (no necesita una instancia)
from datetime import date
hoy = date.today()
print(Empleado.es_dia_laboral(hoy))  # True o False según el día

print(f"Total de empleados: {Empleado.num_empleados}")  # 2
```

---

### Composición vs Herencia

A veces es mejor usar **composición** (tener objetos como atributos) en lugar de herencia.

**Regla general:**
- **Herencia** → "es un" (un Perro ES UN Animal)
- **Composición** → "tiene un" (un Coche TIENE UN Motor)

```python
class Motor:
    """Clase independiente que representa un motor"""
    
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def encender(self):
        """Método para encender el motor"""
        return f"Motor {self.tipo} encendido"
    
    def apagar(self):
        """Método para apagar el motor"""
        return f"Motor {self.tipo} apagado"

class Rueda:
    """Clase independiente que representa una rueda"""
    
    def __init__(self, tamaño):
        self.tamaño = tamaño  # Tamaño en pulgadas

class Coche:
    """
    Clase que USA composición en lugar de herencia.
    Un Coche NO ES UN Motor, pero TIENE UN Motor.
    """
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
        # Composición: el coche "tiene" un motor
        # Creamos objetos de otras clases como atributos
        self.motor = Motor("V6", "300 HP")
        
        # Composición: el coche "tiene" 4 ruedas
        self.ruedas = [Rueda(18) for _ in range(4)]
    
    def arrancar(self):
        """
        El coche delega la funcionalidad al motor.
        No implementa cómo arrancar, usa el método del motor.
        """
        return self.motor.encender()
    
    def info_completa(self):
        """Muestra información completa del coche"""
        return f"{self.marca} {self.modelo} con motor {self.motor.tipo}"

# === USO ===
mi_coche = Coche("Toyota", "Corolla")

# El coche usa el motor internamente
print(mi_coche.arrancar())         # Motor V6 encendido
print(mi_coche.info_completa())    # Toyota Corolla con motor V6

# Podemos acceder directamente al motor si necesitamos
print(mi_coche.motor.potencia)     # 300 HP

# Ventaja: podemos cambiar el motor fácilmente
mi_coche.motor = Motor("V8", "450 HP")
print(mi_coche.arrancar())         # Motor V8 encendido
```

---

## Ejemplo Práctico Completo

Vamos a crear un **sistema de gestión de biblioteca** que integra todos los conceptos de POO que hemos visto.

```python
from datetime import datetime, timedelta
from abc import ABC, abstractmethod

# ============================================================================
# CLASE ABSTRACTA BASE
# ============================================================================

class ItemBiblioteca(ABC):
    """
    Clase abstracta base para todos los items de la biblioteca.
    Define la interfaz común que todos los items deben tener.
    """
    
    def __init__(self, titulo, codigo):
        """Constructor para atributos comunes"""
        self.titulo = titulo
        self.codigo = codigo
        self.prestado = False           # ¿Está prestado actualmente?
        self.fecha_prestamo = None      # ¿Cuándo se prestó?
    
    @abstractmethod
    def obtener_info(self):
        """
        Método abstracto: cada tipo de item debe implementar
        su propia forma de mostrar información.
        """
        pass
    
    def prestar(self):
        """
        Método común para prestar un item.
        Retorna True si se pudo prestar, False si ya estaba prestado.
        """
        if not self.prestado:
            self.prestado = True
            self.fecha_prestamo = datetime.now()
            return True
        return False
    
    def devolver(self):
        """Método común para devolver un item"""
        self.prestado = False
        self.fecha_prestamo = None

# ============================================================================
# CLASES DERIVADAS (HERENCIA)
# ============================================================================

class Libro(ItemBiblioteca):
    """Clase específica para libros - hereda de ItemBiblioteca"""
    
    def __init__(self, titulo, codigo, autor, isbn):
        # Llamamos al constructor del padre para título y código
        super().__init__(titulo, codigo)
        
        # Agregamos atributos específicos de libros
        self.autor = autor
        self.isbn = isbn
    
    def obtener_info(self):
        """Implementación específica para libros"""
        return f"📚 Libro: {self.titulo} por {self.autor} (ISBN: {self.isbn})"

class Revista(ItemBiblioteca):
    """Clase específica para revistas - hereda de ItemBiblioteca"""
    
    def __init__(self, titulo, codigo, numero_edicion):
        super().__init__(titulo, codigo)
        self.numero_edicion = numero_edicion
    
    def obtener_info(self):
        """Implementación específica para revistas"""
        return f"📰 Revista: {self.titulo} - Edición #{self.numero_edicion}"

class DVD(ItemBiblioteca):
    """Clase específica para DVDs - hereda de ItemBiblioteca"""
    
    def __init__(self, titulo, codigo, director, duracion):
        super().__init__(titulo, codigo)
        self.director = director
        self.duracion = duracion  # en minutos
    
    def obtener_info(self):
        """Implementación específica para DVDs"""
        return f"🎬 DVD: {self.titulo} dirigida por {self.director} ({self.duracion} min)"

# ============================================================================
# CLASE USUARIO (COMPOSICIÓN)
# ============================================================================

class Usuario:
    """
    Clase para representar usuarios de la biblioteca.
    Demuestra composición: tiene una lista de items.
    """
    
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Composición: el usuario "tiene" items prestados
        self.items_prestados = []
    
    def tomar_prestado(self, item):
        """
        Intenta tomar prestado un item.
        Valida el límite de préstamos (3 items máximo).
        """
        if len(self.items_prestados) < 3:  # Límite de préstamos
            if item.prestar():  # Intenta prestar el item
                self.items_prestados.append(item)
                return f"✅ {self.nombre} tomó prestado: {item.titulo}"
            return "❌ El item ya está prestado"
        return "❌ Límite de préstamos alcanzado (máximo 3)"
    
    def devolver_item(self, item):
        """Devuelve un item prestado"""
        if item in self.items_prestados:
            item.devolver()
            self.items_prestados.remove(item)
            return f"✅ {self.nombre} devolvió: {item.titulo}"
        return "❌ Este item no estaba prestado a este usuario"
    
    def listar_prestamos(self):
        """Muestra todos los items que tiene el usuario"""
        if not self.items_prestados:
            return f"{self.nombre} no tiene items prestados"
        
        # Usamos list comprehension para crear la lista
        items = "\n".join([f"  • {item.obtener_info()}" 
                          for item in self.items_prestados])
        return f"Items prestados a {self.nombre}:\n{items}"

# ============================================================================
# CLASE BIBLIOTECA (COMPOSICIÓN Y GESTIÓN)
# ============================================================================

class Biblioteca:
    """
    Clase principal que gestiona la biblioteca.
    Demuestra composición: contiene listas de items y usuarios.
    """
    
    def __init__(self, nombre):
        self.nombre = nombre
        # Composición: la biblioteca "tiene" items y usuarios
        self.catalogo = []     # Lista de todos los items
        self.usuarios = []     # Lista de todos los usuarios
    
    def agregar_item(self, item):
        """Agrega un item al catálogo"""
        self.catalogo.append(item)
        return f"✅ Item agregado: {item.titulo}"
    
    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario"""
        self.usuarios.append(usuario)
        return f"✅ Usuario registrado: {usuario.nombre}"
    
    def buscar_item(self, titulo):
        """
        Busca items por título (búsqueda parcial).
        Retorna una lista de items que coinciden.
        """
        # List comprehension con filtro de búsqueda
        resultados = [item for item in self.catalogo 
                     if titulo.lower() in item.titulo.lower()]
        return resultados
    
    def items_disponibles(self):
        """Retorna lista de items que NO están prestados"""
        return [item for item in self.catalogo if not item.prestado]
    
    def items_prestados(self):
        """Retorna lista de items que SÍ están prestados"""
        return [item for item in self.catalogo if item.prestado]
    
    def reporte(self):
        """
        Genera un reporte estadístico de la biblioteca.
        Demuestra el uso de métodos y atributos.
        """
        total = len(self.catalogo)
        prestados = len(self.items_prestados())
        disponibles = len(self.items_disponibles())
        
        return f"""
╔══════════════════════════════════════════════╗
║     REPORTE DE {self.nombre.upper()}
╠══════════════════════════════════════════════╣
║ Total de items:          {total:>3}            ║
║ Items prestados:         {prestados:>3}            ║
║ Items disponibles:       {disponibles:>3}            ║
║ Usuarios registrados:    {len(self.usuarios):>3}            ║
╚══════════════════════════════════════════════╝
        """

# ============================================================================
# USO DEL SISTEMA COMPLETO
# ============================================================================

# Crear la biblioteca
biblioteca = Biblioteca("Biblioteca Municipal de Barcelona")

# Agregar items de diferentes tipos (polimorfismo)
libro1 = Libro("Python para Data Science", "L001", "Jake VanderPlas", "978-1491912058")
libro2 = Libro("Clean Code", "L002", "Robert Martin", "978-0132350884")
revista1 = Revista("National Geographic", "R001", 245)
dvd1 = DVD("Inception", "D001", "Christopher Nolan", 148)

print(biblioteca.agregar_item(libro1))
print(biblioteca.agregar_item(libro2))
print(biblioteca.agregar_item(revista1))
print(biblioteca.agregar_item(dvd1))
print()

# Registrar usuarios
dan = Usuario("Dan", "U001")
alex = Usuario("Alex", "U002")

print(biblioteca.registrar_usuario(dan))
print(biblioteca.registrar_usuario(alex))
print()

# Realizar préstamos
print("=== PRÉSTAMOS ===")
print(dan.tomar_prestado(libro1))
print(dan.tomar_prestado(libro2))
print(dan.tomar_prestado(dvd1))
print(alex.tomar_prestado(libro1))  # Ya está prestado
print()

# Ver préstamos de un usuario
print(dan.listar_prestamos())
print()

# Buscar items
print("=== BÚSQUEDA ===")
resultados = biblioteca.buscar_item("python")
for item in resultados:
    print(item.obtener_info())
print()

# Devolver un item
print("=== DEVOLUCIÓN ===")
print(dan.devolver_item(libro1))
print()

# Ahora otro usuario puede tomarlo
print(alex.tomar_prestado(libro1))
print()

# Ver reporte final
print(biblioteca.reporte())

# Ver items disponibles
print("=== ITEMS DISPONIBLES ===")
for item in biblioteca.items_disponibles():
    print(item.obtener_info())
```

**Salida del programa:**

```
✅ Item agregado: Python para Data Science
✅ Item agregado: Clean Code
✅ Item agregado: National Geographic
✅ Item agregado: Inception

✅ Usuario registrado: Dan
✅ Usuario registrado: Alex

=== PRÉSTAMOS ===
✅ Dan tomó prestado: Python para Data Science
✅ Dan tomó prestado: Clean Code
✅ Dan tomó prestado: Inception
❌ El item ya está prestado

Items prestados a Dan:
  • 📚 Libro: Python para Data Science por Jake VanderPlas (ISBN: 978-1491912058)
  • 📚 Libro: Clean Code por Robert Martin (ISBN: 978-0132350884)
  • 🎬 DVD: Inception dirigida por Christopher Nolan (148 min)

=== BÚSQUEDA ===
📚 Libro: Python para Data Science por Jake VanderPlas (ISBN: 978-1491912058)

=== DEVOLUCIÓN ===
✅ Dan devolvió: Python para Data Science

✅ Alex tomó prestado: Python para Data Science

╔══════════════════════════════════════════════╗
║     REPORTE DE BIBLIOTECA MUNICIPAL DE BARCELONA
╠══════════════════════════════════════════════╣
║ Total de items:            4            ║
║ Items prestados:           3            ║
║ Items disponibles:         1            ║
║ Usuarios registrados:      2            ║
╚══════════════════════════════════════════════╝

=== ITEMS DISPONIBLES ===
📰 Revista: National Geographic - Edición #245
```

---

## Ventajas de la POO

### 1. **Reutilización de código**
Herencia y composición permiten reutilizar código existente sin duplicarlo.

### 2. **Modularidad**
El código está organizado en unidades lógicas y manejables (clases).

### 3. **Mantenibilidad**
Es más fácil encontrar y corregir errores cuando el código está bien organizado.

### 4. **Escalabilidad**
Facilita agregar nuevas funcionalidades sin romper el código existente.

### 5. **Abstracción**
Puedes trabajar con conceptos de alto nivel sin preocuparte por detalles de implementación.

### 6. **Encapsulación**
Protege los datos sensibles y previene modificaciones accidentales.

### 7. **Colaboración**
Múltiples desarrolladores pueden trabajar en diferentes clases simultáneamente.

---

## Cuándo Usar POO

### ✅ **La POO es ideal cuando:**

- Tu programa modela entidades del mundo real (personas, productos, vehículos)
- Necesitas reutilizar código de manera estructurada
- El proyecto es grande y necesita organización
- Trabajas en equipo y necesitas interfaces claras
- El código necesita ser mantenido a largo plazo
- Hay relaciones claras entre entidades (herencia, composición)

### ❌ **NO siempre necesitas POO:**

Para scripts simples, análisis de datos básicos, o cuando la programación funcional es más adecuada:

```python
# Esto NO necesita POO:
numeros = [1, 2, 3, 4, 5]
cuadrados = [n**2 for n in numeros]
promedio = sum(numeros) / len(numeros)
```

### 🤔 **Considera POO cuando:**

- Tienes datos que necesitan comportamientos asociados
- Hay múltiples instancias de algo con diferentes estados
- Necesitas representar relaciones complejas entre entidades

---

## Consejos para Tu Aprendizaje

### 1. **Practica con ejemplos del mundo real**
Modela cosas que conoces: mascotas, vehículos, productos de una tienda, juegos simples.

```python
# Ejercicio: Crea una clase para tu mascota
class Mascota:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.hambre = 50  # 0-100
    
    def alimentar(self):
        self.hambre = max(0, self.hambre - 20)
```

### 2. **Empieza simple**
No intentes crear jerarquías complejas al principio. Comienza con una clase simple y ve agregando funcionalidad gradualmente.

### 3. **Dibuja diagramas**
Visualiza las relaciones entre clases antes de programar:

```
Animal
  ├── Perro
  │   └── Labrador
  └── Gato
      └── Persa
```

### 4. **Refactoriza código existente**
Toma código procedural que hayas escrito y conviértelo a POO:

```python
# Antes (procedural)
jugador_nombre = "Dan"
jugador_vida = 100
jugador_nivel = 1

def atacar(daño):
    global jugador_vida
    jugador_vida -= daño

# Después (POO)
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.nivel = 1
    
    def atacar(self, daño):
        self.vida -= daño
```

### 5. **Lee código de otros**
Estudia proyectos en GitHub para ver cómo otros desarrolladores usan POO. Busca proyectos pequeños y bien documentados.

### 6. **Crea proyectos pequeños**
Algunos proyectos perfectos para practicar POO:
- Sistema de gestión de tareas (To-Do List)
- Juego de adivinanzas con diferentes niveles de dificultad
- Simulador de cajero automático
- Sistema de gestión de estudiantes y calificaciones
- Juego de cartas simple (blackjack, poker)

### 7. **No te compliques**
Si te encuentras creando jerarquías muy profundas o clases con muchos métodos, probablemente estás complicándote demasiado. Keep it simple!

### 8. **Practica los 4 pilares**
Asegúrate de practicar cada pilar por separado:
- **Encapsulación**: Crea una clase `CuentaBancaria` con saldo privado
- **Abstracción**: Crea una interfaz para diferentes formas de pago
- **Herencia**: Crea jerarquías de animales o vehículos
- **Polimorfismo**: Crea diferentes clases que respondan al mismo método

---

## Recursos Adicionales

### 📚 **Para profundizar:**
- Documentación oficial de Python sobre clases: [docs.python.org](https://docs.python.org/3/tutorial/classes.html)
- Real Python - OOP in Python: Tutoriales detallados y prácticos
- Design Patterns: Estudia patrones de diseño como Singleton, Factory, Observer

### 🎯 **Siguiente paso:**
Una vez domines POO básico, aprende sobre:
- **Patrones de diseño** (Design Patterns)
- **SOLID principles** (principios para código limpio)
- **Testing** con unittest y pytest
- **Type hints** para código más robusto

---

## Conclusión

La POO es un cambio de mentalidad. Al principio puede sentirse extraño pensar en "objetos" en lugar de solo funciones y variables, pero con práctica verás cómo hace tu código:

- ✨ Más limpio y organizado
- 🔧 Más fácil de mantener
- 🚀 Más escalable
- 💼 Más profesional

**¡Es una habilidad fundamental para tu carrera en data science!** Muchas bibliotecas que usarás (pandas, scikit-learn, TensorFlow) están construidas usando POO, así que entender estos conceptos te ayudará a usarlas mejor.

Recuerda: la práctica hace al maestro. No te desanimes si al principio parece complicado. Cada desarrollador pasó por lo mismo. ¡Sigue practicando y verás resultados! 💪

---

**Creado por:** Dan  
**Fecha:** Noviembre 2025  
**GitHub:** [Tu perfil de GitHub]  
**Recursos:** Python 3.x

---

*"La programación orientada a objetos no es solo una técnica de programación, es una forma de pensar sobre cómo organizar y estructurar soluciones a problemas complejos."*
