# Ejercicios de Programación Orientada a Objetos en Python 🎯

## Tabla de Contenidos

- [Nivel 1: Básico - Clases y Objetos](#nivel-1-básico---clases-y-objetos)
- [Nivel 2: Intermedio - Encapsulación y Métodos](#nivel-2-intermedio---encapsulación-y-métodos)
- [Nivel 3: Intermedio-Avanzado - Herencia](#nivel-3-intermedio-avanzado---herencia)
- [Nivel 4: Avanzado - Polimorfismo y Abstracción](#nivel-4-avanzado---polimorfismo-y-abstracción)
- [Nivel 5: Experto - Proyectos Integradores](#nivel-5-experto---proyectos-integradores)
- [Soluciones](#soluciones)

---

## Nivel 1: Básico - Clases y Objetos

### Ejercicio 1: Tu Primera Clase 🌟
**Dificultad:** ⭐☆☆☆☆

Crea una clase `Persona` con los siguientes atributos:
- `nombre` (string)
- `edad` (int)
- `ciudad` (string)

Crea un método `presentarse()` que imprima: "Hola, soy [nombre], tengo [edad] años y vivo en [ciudad]"

```python
# Tu código aquí
class Persona:
    pass

# Prueba tu código
persona1 = Persona("Dan", 25, "Barcelona")
persona1.presentarse()
```

**Resultado esperado:**
```
Hola, soy Dan, tengo 25 años y vivo en Barcelona
```

---

### Ejercicio 2: Contador Simple 🔢
**Dificultad:** ⭐☆☆☆☆

Crea una clase `Contador` que:
- Inicie con un valor de 0
- Tenga un método `incrementar()` que aumente el contador en 1
- Tenga un método `decrementar()` que disminuya el contador en 1
- Tenga un método `obtener_valor()` que retorne el valor actual
- Tenga un método `resetear()` que ponga el contador en 0

```python
# Tu código aquí
```

---

### Ejercicio 3: Clase Rectángulo 📐
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `Rectangulo` que:
- Reciba `base` y `altura` en el constructor
- Tenga un método `calcular_area()` que retorne el área
- Tenga un método `calcular_perimetro()` que retorne el perímetro
- Tenga un método `es_cuadrado()` que retorne `True` si es un cuadrado, `False` si no

```python
# Tu código aquí
```

---

### Ejercicio 4: Lista de Tareas 📝
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `ListaTareas` que:
- Mantenga una lista de tareas (strings)
- Tenga un método `agregar_tarea(tarea)` para agregar una tarea
- Tenga un método `completar_tarea(indice)` para eliminar una tarea por su índice
- Tenga un método `mostrar_tareas()` que imprima todas las tareas numeradas
- Tenga un método `total_tareas()` que retorne el número de tareas pendientes

```python
# Tu código aquí
```

---

### Ejercicio 5: Clase Producto 🛒
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `Producto` que:
- Tenga atributos: `nombre`, `precio`, `cantidad_stock`
- Tenga un método `vender(cantidad)` que reduzca el stock y retorne el total de la venta
- Tenga un método `reabastecer(cantidad)` que aumente el stock
- Tenga un método `hay_stock()` que retorne `True` si hay stock disponible
- Tenga un método `__str__()` que retorne información del producto

```python
# Tu código aquí
```

---

### Ejercicio 6: Calculadora Simple 🔢
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `Calculadora` que tenga métodos para:
- `sumar(a, b)`
- `restar(a, b)`
- `multiplicar(a, b)`
- `dividir(a, b)` (maneja la división por cero)
- `potencia(base, exponente)`
- `raiz_cuadrada(numero)` (solo para números positivos)

```python
# Tu código aquí
```

---

### Ejercicio 7: Mascota Virtual 🐶
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `Mascota` que simule una mascota virtual:
- Atributos: `nombre`, `tipo` (perro, gato, etc.), `hambre` (0-100), `felicidad` (0-100)
- Método `alimentar()` que reduzca el hambre en 20
- Método `jugar()` que aumente la felicidad en 15 pero aumente el hambre en 10
- Método `estado()` que imprima el estado actual de la mascota
- El hambre y felicidad no deben salirse del rango 0-100

```python
# Tu código aquí
```

---

### Ejercicio 8: Círculo 🔵
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `Circulo` que:
- Reciba el radio en el constructor
- Tenga un método `calcular_area()` (π × r²)
- Tenga un método `calcular_circunferencia()` (2 × π × r)
- Tenga un método `calcular_diametro()` (2 × r)
- Use `import math` para obtener el valor de π

```python
# Tu código aquí
```

---

### Ejercicio 9: Clase Libro 📚
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `Libro` que:
- Tenga atributos: `titulo`, `autor`, `paginas`, `pagina_actual` (empieza en 0)
- Método `leer(num_paginas)` que avance páginas
- Método `retroceder(num_paginas)` que retroceda páginas
- Método `progreso()` que retorne el porcentaje leído
- Método `terminar_libro()` que vaya a la última página
- Valida que no se salga del rango de páginas

```python
# Tu código aquí
```

---

### Ejercicio 10: Clase Fecha 📅
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `Fecha` que:
- Reciba día, mes y año
- Tenga un método `es_bisiesto()` que determine si el año es bisiesto
- Tenga un método `dias_del_mes()` que retorne cuántos días tiene el mes
- Tenga un método `__str__()` que retorne la fecha en formato "DD/MM/AAAA"
- Tenga un método `es_valida()` que valide si la fecha es correcta

```python
# Tu código aquí
```

---

## Nivel 2: Intermedio - Encapsulación y Métodos

### Ejercicio 11: Cuenta Bancaria con Encapsulación 💰
**Dificultad:** ⭐⭐⭐☆☆

Crea una clase `CuentaBancaria` que:
- Tenga un atributo **privado** `__saldo` (empieza en 0)
- Tenga un método `depositar(cantidad)` (solo cantidades positivas)
- Tenga un método `retirar(cantidad)` (verifica fondos suficientes)
- Tenga un método `transferir(cuenta_destino, cantidad)`
- Tenga un método `obtener_saldo()` (property)
- Mantenga un historial de transacciones

```python
# Tu código aquí
```

---

### Ejercicio 12: Usuario con Contraseña 🔐
**Dificultad:** ⭐⭐⭐☆☆

Crea una clase `Usuario` que:
- Tenga atributos: `nombre_usuario`, `__contraseña` (privada)
- Método `establecer_contraseña(nueva_contraseña)` que valide:
  - Mínimo 8 caracteres
  - Al menos una mayúscula
  - Al menos un número
- Método `verificar_contraseña(contraseña)` que retorne True/False
- Método `cambiar_contraseña(contraseña_actual, contraseña_nueva)`
- NO debe ser posible ver la contraseña directamente

```python
# Tu código aquí
```

---

### Ejercicio 13: Carrito de Compras 🛒
**Dificultad:** ⭐⭐⭐☆☆

Crea dos clases:

**Clase `ItemCarrito`:**
- Atributos: `producto`, `precio`, `cantidad`
- Método `subtotal()` que retorne precio × cantidad

**Clase `CarritoCompras`:**
- Lista de items
- Método `agregar_item(producto, precio, cantidad)`
- Método `eliminar_item(producto)`
- Método `calcular_total()`
- Método `aplicar_descuento(porcentaje)` (0-100)
- Método `mostrar_carrito()` con todos los items y el total

```python
# Tu código aquí
```

---

### Ejercicio 14: Sistema de Notas de Estudiante 📊
**Dificultad:** ⭐⭐⭐☆☆

Crea una clase `Estudiante` que:
- Tenga atributos: `nombre`, `id_estudiante`, `__calificaciones` (diccionario privado)
- Método `agregar_calificacion(materia, nota)` (valida nota entre 0-10)
- Método `obtener_calificacion(materia)`
- Método `promedio_general()`
- Método `materias_aprobadas()` (nota >= 6)
- Método `materias_reprobadas()` (nota < 6)
- Método `mejor_materia()` que retorne la materia con mejor nota
- Método `peor_materia()` que retorne la materia con peor nota

```python
# Tu código aquí
```

---

### Ejercicio 15: Temporizador ⏱️
**Dificultad:** ⭐⭐⭐☆☆

Crea una clase `Temporizador` que:
- Tenga atributos: `horas`, `minutos`, `segundos`
- Método `establecer_tiempo(horas, minutos, segundos)`
- Método `tick()` que reduzca el tiempo en 1 segundo
- Método `reiniciar()`
- Método `ha_terminado()` que retorne True si llegó a 00:00:00
- Método `__str__()` que retorne el tiempo en formato "HH:MM:SS"
- Método `tiempo_restante_segundos()` que retorne el total en segundos

```python
# Tu código aquí
```

---

### Ejercicio 16: Punto 2D con Properties 📍
**Dificultad:** ⭐⭐⭐☆☆

Crea una clase `Punto` que:
- Tenga coordenadas `x` e `y` como properties
- Método `distancia_origen()` que calcule la distancia al origen (0,0)
- Método `distancia_punto(otro_punto)` que calcule la distancia a otro punto
- Método `mover(dx, dy)` que mueva el punto
- Método `cuadrante()` que retorne en qué cuadrante está (I, II, III, IV o "Origen")
- Método `__str__()` que retorne "(x, y)"

Fórmula de distancia: √((x2-x1)² + (y2-y1)²)

```python
# Tu código aquí
```

---

### Ejercicio 17: Playlist Musical 🎵
**Dificultad:** ⭐⭐⭐☆☆

Crea dos clases:

**Clase `Cancion`:**
- Atributos: `titulo`, `artista`, `duracion_segundos`
- Método `duracion_formato()` que retorne "MM:SS"

**Clase `Playlist`:**
- Atributos: `nombre`, lista de canciones, `cancion_actual` (índice)
- Método `agregar_cancion(cancion)`
- Método `eliminar_cancion(titulo)`
- Método `reproducir_siguiente()`
- Método `reproducir_anterior()`
- Método `duracion_total()` en formato "HH:MM:SS"
- Método `buscar_por_artista(artista)` que retorne lista de canciones
- Método `mezclar()` que aleatorice el orden (usa `import random`)

```python
# Tu código aquí
```

---

### Ejercicio 18: Inventario con Stock Mínimo 📦
**Dificultad:** ⭐⭐⭐☆☆

Crea una clase `ProductoInventario` que:
- Atributos: `codigo`, `nombre`, `precio`, `stock_actual`, `stock_minimo`
- Método `vender(cantidad)` que reduzca stock
- Método `reabastecer(cantidad)` que aumente stock
- Método `necesita_reabastecimiento()` que retorne True si stock < stock_minimo
- Método `alerta_stock()` que imprima una alerta si necesita reabastecimiento
- Método `valor_inventario()` que retorne precio × stock_actual
- Método `aplicar_descuento(porcentaje)` que reduzca el precio

```python
# Tu código aquí
```

---

### Ejercicio 19: Clase Email 📧
**Dificultad:** ⭐⭐⭐☆☆

Crea una clase `Email` que:
- Atributos: `remitente`, `destinatario`, `asunto`, `cuerpo`, `leido` (bool)
- Método `marcar_como_leido()`
- Método `marcar_como_no_leido()`
- Método `responder(cuerpo_respuesta)` que cree un nuevo Email
- Método `reenviar(nuevo_destinatario)` que cree un nuevo Email
- Método `es_valido_email(email)` que valide el formato (debe tener @ y .)
- Método `__str__()` que muestre la información del email

```python
# Tu código aquí
```

---

### Ejercicio 20: Clase Dado 🎲
**Dificultad:** ⭐⭐☆☆☆

Crea una clase `Dado` que:
- Tenga un atributo `caras` (por defecto 6)
- Método `lanzar()` que retorne un número aleatorio entre 1 y el número de caras
- Atributo `ultimo_lanzamiento` que guarde el último resultado
- Método `lanzar_multiple(cantidad)` que lance el dado varias veces y retorne la suma
- Método `probabilidad_cara(cara)` que retorne la probabilidad teórica de esa cara
- Método estático `lanzar_dos_dados()` que simule el lanzamiento de 2 dados

```python
# Tu código aquí
```

---

## Nivel 3: Intermedio-Avanzado - Herencia

### Ejercicio 21: Jerarquía de Vehículos 🚗
**Dificultad:** ⭐⭐⭐⭐☆

Crea una jerarquía de clases:

**Clase base `Vehiculo`:**
- Atributos: `marca`, `modelo`, `año`, `velocidad_actual`
- Métodos: `acelerar(incremento)`, `frenar(decremento)`, `obtener_info()`

**Clase `Coche` (hereda de Vehiculo):**
- Atributo adicional: `num_puertas`
- Método: `abrir_maletero()`

**Clase `Moto` (hereda de Vehiculo):**
- Atributo adicional: `tipo` (deportiva, cruiser, etc.)
- Método: `hacer_caballito()`

**Clase `Camion` (hereda de Vehiculo):**
- Atributo adicional: `capacidad_carga` (en kg)
- Método: `cargar(peso)` y `descargar(peso)`

```python
# Tu código aquí
```

---

### Ejercicio 22: Sistema de Empleados 👔
**Dificultad:** ⭐⭐⭐⭐☆

Crea una jerarquía de empleados:

**Clase base `Empleado`:**
- Atributos: `nombre`, `id_empleado`, `salario_base`
- Método: `calcular_salario()` (retorna salario_base)
- Método: `obtener_info()`

**Clase `EmpleadoPorHora` (hereda de Empleado):**
- Atributos adicionales: `horas_trabajadas`, `tarifa_hora`
- Sobrescribe `calcular_salario()` → horas × tarifa

**Clase `EmpleadoAsalariado` (hereda de Empleado):**
- Método `aplicar_bono(porcentaje)` que aumente el salario

**Clase `Gerente` (hereda de EmpleadoAsalariado):**
- Atributo: `equipo` (lista de empleados)
- Método: `agregar_miembro(empleado)`
- Método: `tamaño_equipo()`
- Método: `costo_total_equipo()` que sume los salarios del equipo

```python
# Tu código aquí
```

---

### Ejercicio 23: Figuras Geométricas 📐
**Dificultad:** ⭐⭐⭐⭐☆

Crea una jerarquía de formas:

**Clase base `Forma`:**
- Métodos abstractos: `calcular_area()`, `calcular_perimetro()`

**Clases derivadas:**
- `Cuadrado(lado)`
- `Rectangulo(base, altura)`
- `Triangulo(base, altura, lado1, lado2, lado3)`
- `Circulo(radio)`
- `Trapecio(base_mayor, base_menor, altura, lado1, lado2)`

Todas deben implementar ambos métodos. Crea una función que reciba una lista de formas y calcule el área total.

```python
# Tu código aquí
```

---

### Ejercicio 24: Sistema de Cuentas Bancarias 🏦
**Dificultad:** ⭐⭐⭐⭐☆

**Clase base `CuentaBancaria`:**
- Atributos: `numero_cuenta`, `titular`, `__saldo`
- Métodos: `depositar()`, `retirar()`, `obtener_saldo()`

**Clase `CuentaAhorro` (hereda de CuentaBancaria):**
- Atributo: `tasa_interes`
- Método: `aplicar_interes_mensual()` que aumente el saldo

**Clase `CuentaCorriente` (hereda de CuentaBancaria):**
- Atributo: `limite_sobregiro`
- Sobrescribe `retirar()` para permitir sobregiro hasta el límite
- Método: `esta_en_sobregiro()`

**Clase `CuentaInversion` (hereda de CuentaBancaria):**
- No permite retiros antes de 30 días
- Atributo: `fecha_apertura`
- Método: `puede_retirar()` que verifique si pasaron 30 días

```python
# Tu código aquí
```

---

### Ejercicio 25: Personajes de Videojuego 🎮
**Dificultad:** ⭐⭐⭐⭐☆

**Clase base `Personaje`:**
- Atributos: `nombre`, `nivel`, `vida_maxima`, `vida_actual`
- Métodos: `recibir_daño(cantidad)`, `curar(cantidad)`, `esta_vivo()`, `subir_nivel()`

**Clase `Guerrero` (hereda de Personaje):**
- Atributo: `fuerza`
- Método: `ataque_poderoso(enemigo)` causa daño × fuerza
- Método: `defender()` reduce el próximo daño recibido a la mitad

**Clase `Mago` (hereda de Personaje):**
- Atributo: `mana_actual`, `mana_maximo`
- Método: `lanzar_hechizo(enemigo, costo_mana)` 
- Método: `recuperar_mana(cantidad)`

**Clase `Arquero` (hereda de Personaje):**
- Atributo: `flechas`
- Método: `disparar_flecha(enemigo)` (consume 1 flecha)
- Método: `recargar_flechas(cantidad)`

```python
# Tu código aquí
```

---

### Ejercicio 26: Instrumentos Musicales 🎸
**Dificultad:** ⭐⭐⭐☆☆

**Clase base `Instrumento`:**
- Atributos: `nombre`, `tipo`, `marca`
- Método: `tocar()` (debe ser implementado por las clases hijas)
- Método: `afinar()`

**Clases derivadas:**
- `Guitarra(num_cuerdas)` → método `tocar()` imprime "Rasgueo de guitarra..."
- `Piano(num_teclas)` → método `tocar()` imprime "Melodía de piano..."
- `Bateria(num_tambores)` → método `tocar()` imprime "Ritmo de batería..."
- `Violin(tipo_arco)` → método `tocar()` imprime "Sonido de violín..."

Crea una función `concierto(instrumentos)` que haga tocar a todos los instrumentos de la lista.

```python
# Tu código aquí
```

---

### Ejercicio 27: Dispositivos Electrónicos 📱
**Dificultad:** ⭐⭐⭐⭐☆

**Clase base `DispositivoElectronico`:**
- Atributos: `marca`, `modelo`, `bateria_actual`, `bateria_maxima`, `encendido`
- Métodos: `encender()`, `apagar()`, `cargar(cantidad)`, `usar(consumo)`

**Clase `Smartphone` (hereda de DispositivoElectronico):**
- Atributos: `almacenamiento_usado`, `almacenamiento_total`, `apps_instaladas`
- Métodos: `instalar_app(nombre, tamaño)`, `desinstalar_app(nombre)`, `hacer_llamada()`

**Clase `Laptop` (hereda de DispositivoElectronico):**
- Atributos: `ram`, `procesador`
- Métodos: `ejecutar_programa(nombre)`, `modo_ahorro_energia()`

**Clase `Tablet` (hereda de DispositivoElectronico):**
- Atributos: `tiene_lapiz`, `tamaño_pantalla`
- Métodos: `dibujar()`, `tomar_notas()`

```python
# Tu código aquí
```

---

## Nivel 4: Avanzado - Polimorfismo y Abstracción

### Ejercicio 28: Sistema de Pagos 💳
**Dificultad:** ⭐⭐⭐⭐⭐

**Clase abstracta `MetodoPago`:**
- Método abstracto: `procesar_pago(monto)`
- Método abstracto: `validar()`

**Clases concretas:**
- `TarjetaCredito(numero, cvv, fecha_vencimiento)`
- `PayPal(email, contraseña)`
- `Bitcoin(direccion_wallet)`
- `Efectivo(monto_recibido)`

**Clase `Carrito`:**
- Método: `pagar(metodo_pago)` que use polimorfismo

Cada método debe validar de forma diferente y procesar el pago mostrando información específica.

```python
# Tu código aquí
```

---

### Ejercicio 29: Sistema de Notificaciones 📬
**Dificultad:** ⭐⭐⭐⭐⭐

**Clase abstracta `Notificacion`:**
- Atributos: `destinatario`, `mensaje`, `fecha_hora`
- Método abstracto: `enviar()`
- Método: `formato_fecha()`

**Clases concretas:**
- `NotificacionEmail(destinatario, mensaje, asunto)`
- `NotificacionSMS(destinatario, mensaje, numero_telefono)`
- `NotificacionPush(destinatario, mensaje, app)`
- `NotificacionSlack(destinatario, mensaje, canal)`

**Clase `SistemaNotificaciones`:**
- Método: `enviar_notificacion(notificacion)` (polimorfismo)
- Método: `enviar_multiple(lista_notificaciones)`
- Método: `programar_notificacion(notificacion, minutos_espera)`

```python
# Tu código aquí
```

---

### Ejercicio 30: Zoológico Virtual 🦁
**Dificultad:** ⭐⭐⭐⭐⭐

**Clase abstracta `Animal`:**
- Atributos: `nombre`, `edad`, `especie`, `habitat`
- Métodos abstractos: `hacer_sonido()`, `alimentarse()`
- Método concreto: `cumplir_años()`

**Clases concretas (mínimo 5 animales diferentes):**
- `Leon`, `Elefante`, `Pinguino`, `Serpiente`, `Aguila`
- Cada uno implementa `hacer_sonido()` y `alimentarse()` de forma única

**Clase `Zoologico`:**
- Atributo: `animales` (lista)
- Método: `agregar_animal(animal)`
- Método: `hora_alimentacion()` → alimenta a todos los animales
- Método: `concierto_animal()` → hace que todos los animales hagan su sonido
- Método: `animales_por_habitat(habitat)` → retorna lista filtrada
- Método: `animal_mas_viejo()` → retorna el animal con mayor edad

```python
# Tu código aquí
```

---

## Nivel 5: Experto - Proyectos Integradores

### Ejercicio 31: Sistema de Gestión de Hotel 🏨
**Dificultad:** ⭐⭐⭐⭐⭐

Crea un sistema completo con las siguientes clases:

**Clase `Habitacion`:**
- Atributos: `numero`, `tipo` (simple, doble, suite), `precio_noche`, `ocupada`
- Métodos: `ocupar()`, `liberar()`, `calcular_costo(num_noches)`

**Clase `Huesped`:**
- Atributos: `nombre`, `dni`, `email`, `telefono`

**Clase `Reserva`:**
- Atributos: `huesped`, `habitacion`, `fecha_entrada`, `fecha_salida`, `confirmada`
- Métodos: `confirmar()`, `cancelar()`, `calcular_total()`, `num_noches()`

**Clase `Hotel`:**
- Atributos: `nombre`, `habitaciones`, `reservas`, `historial`
- Métodos:
  - `buscar_habitaciones_disponibles(fecha_entrada, fecha_salida, tipo)`
  - `crear_reserva(huesped, habitacion, fecha_entrada, fecha_salida)`
  - `check_in(reserva)`
  - `check_out(reserva)`
  - `ingresos_periodo(fecha_inicio, fecha_fin)`
  - `ocupacion_promedio()`
  - `habitacion_mas_reservada()`

```python
# Tu código aquí
```

---

### Ejercicio 32: Red Social Simplificada 📱
**Dificultad:** ⭐⭐⭐⭐⭐

**Clase `Usuario`:**
- Atributos: `username`, `nombre`, `bio`, `seguidores`, `siguiendo`, `posts`
- Métodos: `publicar(contenido)`, `seguir(usuario)`, `dejar_seguir(usuario)`, `num_seguidores()`

**Clase `Post`:**
- Atributos: `autor`, `contenido`, `fecha_hora`, `likes`, `comentarios`
- Métodos: `dar_like(usuario)`, `quitar_like(usuario)`, `agregar_comentario(usuario, texto)`

**Clase `Comentario`:**
- Atributos: `autor`, `texto`, `fecha_hora`

**Clase `RedSocial`:**
- Atributos: `usuarios`, `posts`
- Métodos:
  - `registrar_usuario(username, nombre)`
  - `buscar_usuario(username)`
  - `feed(usuario)` → posts de usuarios que sigue
  - `posts_populares(limite)` → posts con más likes
  - `usuarios_sugeridos(usuario)` → basado en seguidores en común

```python
# Tu código aquí
```

---

### Ejercicio 33: Sistema de Gestión de Cursos Online 🎓
**Dificultad:** ⭐⭐⭐⭐⭐

**Clase `Curso`:**
- Atributos: `titulo`, `descripcion`, `instructor`, `lecciones`, `estudiantes_inscritos`, `precio`
- Métodos: `agregar_leccion()`, `inscribir_estudiante()`, `calificacion_promedio()`

**Clase `Leccion`:**
- Atributos: `titulo`, `contenido`, `duracion_minutos`, `completada_por` (lista de estudiantes)
- Métodos: `marcar_completada(estudiante)`

**Clase `Estudiante`:**
- Atributos: `nombre`, `email`, `cursos_inscritos`, `progreso` (diccionario)
- Métodos: `inscribirse(curso)`, `completar_leccion(leccion)`, `progreso_curso(curso)`

**Clase `Instructor`:**
- Atributos: `nombre`, `bio`, `cursos_creados`, `calificacion`
- Métodos: `crear_curso()`, `calificacion_promedio()`

**Clase `Plataforma`:**
- Atributos: `cursos`, `estudiantes`, `instructores`
- Métodos:
  - `buscar_cursos(palabra_clave)`
  - `cursos_populares()`
  - `ingresos_totales()`
  - `tasa_completacion_promedio()`
  - `mejor_instructor()` (por calificación)

```python
# Tu código aquí
```

---

### Ejercicio 34: Juego de Batalla por Turnos ⚔️
**Dificultad:** ⭐⭐⭐⭐⭐

Crea un juego de batalla completo:

**Clase abstracta `Personaje`:**
- Atributos: `nombre`, `vida`, `vida_maxima`, `ataque`, `defensa`, `velocidad`
- Métodos: `atacar(enemigo)`, `recibir_daño(daño)`, `esta_vivo()`, `usar_habilidad(enemigo)`

**Clases de personajes (mínimo 3):**
- `Guerrero`, `Mago`, `Arquero` (cada uno con habilidades únicas)

**Clase `Habilidad`:**
- Atributos: `nombre`, `descripcion`, `daño`, `cooldown`, `turnos_restantes`
- Método: `usar(usuario, objetivo)`

**Clase `Batalla`:**
- Atributos: `jugador1`, `jugador2`, `turno_actual`, `historial`
- Métodos:
  - `iniciar_batalla()`
  - `turno(personaje, accion)` → procesa el turno
  - `determinar_orden()` → basado en velocidad
  - `verificar_ganador()`
  - `mostrar_estado()`

**Clase `Juego`:**
- Gestiona múltiples batallas, puntuaciones, etc.

```python
# Tu código aquí
```

---

### Ejercicio 35: Sistema de E-commerce Completo 🛍️
**Dificultad:** ⭐⭐⭐⭐⭐

**Clase `Producto`:**
- Atributos: `id`, `nombre`, `descripcion`, `precio`, `stock`, `categoria`, `calificaciones`
- Métodos: `agregar_calificacion()`, `calificacion_promedio()`, `aplicar_descuento()`

**Clase `Carrito`:**
- Métodos: `agregar_producto()`, `eliminar_producto()`, `calcular_subtotal()`, `aplicar_cupon()`

**Clase `Cliente`:**
- Atributos: `nombre`, `email`, `direccion`, `carrito`, `historial_compras`, `lista_deseos`
- Métodos: `agregar_a_lista_deseos()`, `realizar_compra()`

**Clase `Orden`:**
- Atributos: `numero_orden`, `cliente`, `productos`, `total`, `estado`, `fecha`
- Métodos: `confirmar()`, `cancelar()`, `calcular_impuestos()`, `calcular_envio()`

**Clase `Tienda`:**
- Atributos: `productos`, `clientes`, `ordenes`
- Métodos:
  - `buscar_productos(criterio)`
  - `productos_mas_vendidos()`
  - `ingresos_totales(periodo)`
  - `productos_bajo_stock()`
  - `generar_reporte_ventas()`

**Clase abstracta `MetodoEnvio`:**
- Clases derivadas: `EnvioEstandar`, `EnvioExpress`, `Recoleccion`

```python
# Tu código aquí
```

---

## Consejos para Resolver los Ejercicios

### 📝 Antes de Empezar:
1. **Lee el ejercicio completo** antes de escribir código
2. **Identifica las clases** que necesitas
3. **Define los atributos** de cada clase
4. **Planea los métodos** necesarios
5. **Piensa en las relaciones** entre clases (herencia, composición)

### 💡 Durante el Desarrollo:
1. **Empieza con lo básico** (constructor y atributos)
2. **Implementa un método a la vez** y pruébalo
3. **Usa print()** para depurar y ver qué está pasando
4. **Maneja errores** con try-except cuando sea necesario
5. **Comenta tu código** para recordar qué hace cada parte

### ✅ Después de Terminar:
1. **Prueba todos los métodos** con diferentes casos
2. **Prueba casos extremos** (valores negativos, listas vacías, etc.)
3. **Refactoriza** si ves código repetido
4. **Documenta** con docstrings
5. **Compara** con las soluciones (próxima sección)

---

## Estrategia de Práctica Recomendada

### 🗓️ Plan de Estudio (4 semanas):

**Semana 1: Nivel 1 (Ejercicios 1-10)**
- Día 1-2: Ejercicios 1-5
- Día 3-4: Ejercicios 6-10
- Día 5: Repaso y refuerzo

**Semana 2: Nivel 2 (Ejercicios 11-20)**
- Día 1-2: Ejercicios 11-15
- Día 3-4: Ejercicios 16-20
- Día 5: Repaso y refuerzo

**Semana 3: Nivel 3-4 (Ejercicios 21-30)**
- Día 1-2: Ejercicios 21-25
- Día 3-4: Ejercicios 26-30
- Día 5: Repaso y refuerzo

**Semana 4: Nivel 5 (Ejercicios 31-35)**
- Día 1-2: Ejercicio 31-32
- Día 3-4: Ejercicio 33-34
- Día 5: Ejercicio 35 y repaso general

### 🎯 Objetivos de Aprendizaje:

- **Nivel 1:** Comprender clases, objetos, atributos y métodos básicos
- **Nivel 2:** Dominar encapsulación, properties y métodos especiales
- **Nivel 3:** Aplicar herencia y reutilización de código
- **Nivel 4:** Implementar polimorfismo y abstracción
- **Nivel 5:** Integrar todos los conceptos en proyectos complejos

---

## Recursos Adicionales

### 📚 Para Profundizar:
- **Documentación oficial de Python:** https://docs.python.org/3/tutorial/classes.html
- **Real Python - OOP:** Tutoriales detallados
- **Python Tutor:** Visualiza la ejecución de tu código paso a paso
- **GitHub:** Busca proyectos similares para inspirarte

### 🎮 Gamificación:
- Lleva un registro de ejercicios completados ✅
- Cronometra tu tiempo en cada ejercicio ⏱️
- Desafía a un amigo a resolver los mismos ejercicios 🤝
- Sube tus soluciones a GitHub 📤

### 💪 Mantén la Motivación:
- **Celebra los pequeños logros** 🎉
- **No te compares con otros**, compárate con tu yo de ayer
- **Toma descansos** cuando te sientas frustrada
- **Pide ayuda** cuando la necesites
- **Recuerda por qué empezaste** este camino

---

## Próximos Pasos

Una vez completes estos ejercicios:

1. ✅ **Revisa las soluciones** y compara con tu código
2. 🔄 **Refactoriza** tus soluciones para mejorarlas
3. 📝 **Documenta** tu código con docstrings
4. 🧪 **Agrega tests** unitarios (aprende `unittest` o `pytest`)
5. 🚀 **Crea tu propio proyecto** aplicando todo lo aprendido

---

**¡Ánimo, Dan! 💪** Cada ejercicio que resuelvas te acerca más a tu objetivo de convertirte en Data Scientist. Recuerda que la programación orientada a objetos es una habilidad fundamental que usarás constantemente en tu carrera.

**"El código es como humor. Cuando tienes que explicarlo, es malo." – Cory House**

Pero mientras aprendes, ¡explica todo lo que puedas! 😊

---

**Creado por:** Dan  
**Fecha:** Noviembre 2025  
**Nivel:** Básico a Avanzado  
**Tiempo estimado:** 40-60 horas de práctica

**¡Éxito en tu aprendizaje! 🚀**
