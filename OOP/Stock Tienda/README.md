# 🛒 Sistema de Gestión de Inventario - Python OOP

## 🎯 Descripción del Proyecto

Sistema de gestión de inventario para tiendas desarrollado en Python utilizando **Programación Orientada a Objetos (OOP)**. Permite administrar productos, controlar stock, realizar ventas y generar reportes de inventario.

## ✨ Características

- ✅ Agregar productos al inventario
- ✅ Gestionar stock (agregar/reducir cantidades)
- ✅ Realizar ventas con validación de stock
- ✅ Buscar productos por nombre
- ✅ Visualizar inventario completo
- ✅ Filtrar productos sin stock
- ✅ Filtrar productos disponibles
- ✅ Validaciones automáticas de operaciones

## 🧠 Conceptos de OOP Aplicados

### Clases y Objetos
El proyecto utiliza dos clases principales:
- **`Producto`**: Representa un producto individual con sus atributos (nombre, precio, cantidad)
- **`Tienda`**: Gestiona una colección de productos y proporciona operaciones de inventario

### Encapsulamiento
Los datos de productos están encapsulados en objetos, y todas las operaciones se realizan mediante métodos que garantizan la integridad de los datos.

### Validaciones
El sistema incluye validaciones automáticas:
- Verificación de stock antes de ventas
- Mensajes informativos para el usuario
- Control de productos inexistentes

## 🚀 Instalación y Uso

### Requisitos
- Python 3.x

### Ejecución
```bash
python tienda.py
```

### Ejemplo de Uso

```python
# Crear la tienda
tienda = Tienda()

# Crear productos
laptop = Producto("Laptop", 999.99, 5)
mouse = Producto("Mouse", 25.50, 0)

# Agregar a inventario
tienda.agregar_producto(laptop)
tienda.agregar_producto(mouse)

# Realizar venta
laptop_encontrada = tienda.buscar_producto("Laptop")
if laptop_encontrada:
    laptop_encontrada.vender(2)

# Agregar stock
mouse.agregar_stock(10)

# Ver reportes
tienda.mostrar_inventario()
tienda.productos_sin_stock()
```

## 📁 Estructura del Código

### Clase `Producto`

```python
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def agregar_stock(self, cantidad)
    def vender(self, cantidad)
    def mostrar_info(self)
```

**Atributos:**
- `nombre`: Nombre del producto
- `precio`: Precio unitario del producto
- `cantidad`: Cantidad disponible en stock

**Métodos:**
- `agregar_stock(cantidad)`: Incrementa el stock del producto
- `vender(cantidad)`: Reduce el stock si hay suficiente disponible
- `mostrar_info()`: Muestra la información completa del producto

### Clase `Tienda`

```python
class Tienda:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto)
    def buscar_producto(self, nombre)
    def mostrar_inventario(self)
    def productos_sin_stock(self)
    def productos_disponibles(self)
```

**Atributos:**
- `productos`: Lista de objetos `Producto` en el inventario

**Métodos:**
- `agregar_producto(producto)`: Añade un nuevo producto al inventario
- `buscar_producto(nombre)`: Busca y retorna un producto por su nombre
- `mostrar_inventario()`: Muestra todos los productos del inventario
- `productos_sin_stock()`: Filtra y muestra productos con stock = 0
- `productos_disponibles()`: Filtra y muestra productos con stock > 0

## 💻 Código Completo

```python
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregar_stock(self, cantidad):
        self.cantidad = self.cantidad + cantidad
        print(f"Stock agregado. Nuevo stock de {self.nombre}: {self.cantidad}")

    def vender(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad = self.cantidad - cantidad
            print(f"✅ Venta realizada. Stock restante de {self.nombre}: {self.cantidad}")
        else:
            print(f"❌ Stock insuficiente de {self.nombre}. Disponible: {self.cantidad}")

    def mostrar_info(self):
        print(f"\n--- Producto ---")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Stock: {self.cantidad}")


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"➕ Producto '{producto.nombre}' agregado al inventario")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        print(f"⚠️ Producto '{nombre}' no encontrado")
        return None

    def mostrar_inventario(self):
        if len(self.productos) == 0:
            print("\n📭 El inventario está vacío")
        else:
            print("\n" + "="*40)
            print("📦 INVENTARIO COMPLETO")
            print("="*40)
            for producto in self.productos:
                producto.mostrar_info()

    def productos_sin_stock(self):
        print("\n" + "="*40)
        print("⚠️ PRODUCTOS SIN STOCK")
        print("="*40)
        hay_sin_stock = False
        for producto in self.productos:
            if producto.cantidad == 0:
                producto.mostrar_info()
                hay_sin_stock = True
        if not hay_sin_stock:
            print("\n✅ Todos los productos tienen stock")

    def productos_disponibles(self):
        print("\n" + "="*40)
        print("✅ PRODUCTOS DISPONIBLES")
        print("="*40)
        hay_disponibles = False
        for producto in self.productos:
            if producto.cantidad > 0:
                producto.mostrar_info()
                hay_disponibles = True
        if not hay_disponibles:
            print("\n❌ No hay productos disponibles")


# ==========================================
# EJEMPLO DE USO
# ==========================================

if __name__ == "__main__":
    # Crear la tienda
    tienda = Tienda()
    
    # Crear productos
    producto1 = Producto("Laptop", 999.99, 5)
    producto2 = Producto("Mouse", 25.50, 0)
    producto3 = Producto("Teclado", 75.00, 10)
    
    # Agregar productos a la tienda
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)
    tienda.agregar_producto(producto3)
    
    # Mostrar inventario completo
    tienda.mostrar_inventario()
    
    # Mostrar productos sin stock
    tienda.productos_sin_stock()
    
    # Mostrar productos disponibles
    tienda.productos_disponibles()
    
    # Buscar un producto específico y venderlo
    laptop = tienda.buscar_producto("Laptop")
    if laptop:
        laptop.vender(2)
        laptop.vender(5)  # Intentar vender más de lo disponible
    
    # Agregar stock a un producto sin stock
    mouse = tienda.buscar_producto("Mouse")
    if mouse:
        mouse.agregar_stock(15)
    
    # Mostrar inventario actualizado
    tienda.mostrar_inventario()
```

## 🎮 Casos de Uso

### Gestión de Stock
```python
producto = Producto("Monitor", 299.99, 3)
producto.agregar_stock(5)  # Ahora tiene 8 unidades
```

### Procesamiento de Ventas
```python
producto.vender(2)  # Resta 2 del stock
producto.vender(10)  # Muestra error: stock insuficiente
```

### Búsqueda y Filtrado
```python
# Buscar producto específico
teclado = tienda.buscar_producto("Teclado")

# Ver solo productos disponibles
tienda.productos_disponibles()

# Ver productos que necesitan reabastecimiento
tienda.productos_sin_stock()
```

## 🔧 Posibles Mejoras

- **Base de datos**: Persistencia con SQLite o PostgreSQL
- **Categorías**: Organizar productos por categorías
- **Alertas**: Notificaciones cuando el stock es bajo
- **Historial**: Registro de ventas y movimientos de inventario
- **Reportes**: Generación de reportes en PDF o Excel
- **Interfaz gráfica**: GUI con Tkinter o PyQt
- **API REST**: Endpoints con Flask o FastAPI para integración web
- **Códigos de barras**: Sistema de escaneo de productos
- **Proveedores**: Gestión de proveedores y órdenes de compra
- **Descuentos**: Sistema de precios especiales y promociones

## 📊 Aplicaciones Prácticas

Este sistema puede ser utilizado en:
- Pequeñas tiendas de retail
- Almacenes
- Farmacias
- Tiendas online
- Gestión de inventario personal
- Proyectos educativos de gestión

## 🛠️ Tecnologías

- **Python 3.x**
- Programación Orientada a Objetos (OOP)
- Manejo de listas y estructuras de datos
- Validaciones y control de flujo

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y comercial.

---

**Última actualización:** Noviembre 2025
