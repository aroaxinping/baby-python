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
