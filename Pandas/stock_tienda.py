import pandas as pd

# Datos de productos
productos_data = {
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Webcam'],
    'precio': [999.99, 25.50, 75.00, 299.99, 89.99],
    'stock': [5, 15, 8, 3, 12],
    'categoria': ['Electrónica', 'Accesorios', 'Accesorios', 'Electrónica', 'Accesorios']
}

df = pd.DataFrame(productos_data)

print("=== DATAFRAME ORIGINAL ===")
print(df)
print()

# 1. SELECCIONAR MÚLTIPLES COLUMNAS
print("=== SOLO PRODUCTO Y PRECIO ===")
df_precios = df[['producto', 'precio']]  # Nota: doble corchete [[]]
print(df_precios)
print()

# 2. AGREGAR NUEVA COLUMNA (calcular valor total del inventario)
print("=== AGREGANDO COLUMNA 'VALOR_TOTAL' ===")
df['valor_total'] = df['precio'] * df['stock']
print(df)
print()

# 3. ORDENAR por precio (de mayor a menor)
print("=== ORDENADO POR PRECIO (MAYOR A MENOR) ===")
df_ordenado = df.sort_values('precio', ascending=False)
print(df_ordenado)
print()

# 4. FILTRAR productos caros (precio > 100)
print("=== PRODUCTOS CAROS (> 100€) ===")
productos_caros = df[df['precio'] > 100]
print(productos_caros)
print()

# 5. ESTADÍSTICAS
print("=== ESTADÍSTICAS DE PRECIOS ===")
print(f"Precio promedio: {df['precio'].mean():.2f}€")
print(f"Precio máximo: {df['precio'].max():.2f}€")
print(f"Precio mínimo: {df['precio'].min():.2f}€")
print(f"Total productos en stock: {df['stock'].sum()}")
