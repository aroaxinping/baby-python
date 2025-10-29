# Diccionarios en Python

## ¿Qué es un diccionario?

Un diccionario en Python funciona de manera similar a un diccionario en la vida real. Es una estructura de datos que nos permite asociar una **clave** (key) con un **valor** (value) y emparejar estos dos datos juntos.

Los diccionarios son una de las estructuras de datos más útiles y versátiles en Python, perfectos para almacenar información relacionada de forma organizada.

## Crear un diccionario

Así es como se crea un diccionario en Python:
```python
# Un diccionario de ejemplo
colores = {
    "manzana": "rojo", 
    "pera": "verde", 
    "banana": "amarillo"
}
```

**Nota:** Los diccionarios se definen usando llaves `{}` y cada par clave-valor se separa con dos puntos `:`. Los diferentes pares se separan con comas `,`.

## Acceder a los valores

Para recuperar un valor de un diccionario, usamos la clave correspondiente entre corchetes:
```python
print(colores["pera"])
# Imprimirá: verde
```

## Crear un diccionario vacío

Si necesitas crear un diccionario sin elementos iniciales:
```python
mi_diccionario_vacio = {}
```

También puedes usar el constructor `dict()`:
```python
otro_diccionario_vacio = dict()
```

## Agregar nuevos elementos

Para añadir un nuevo par clave-valor a un diccionario existente:
```python
colores["melocotón"] = "rosa"
```

Después de esta operación, el diccionario `colores` contendrá el nuevo elemento.

## Modificar valores existentes

La misma sintaxis se usa para editar un valor existente en un diccionario:
```python
colores["manzana"] = "verde"
```

Esto sobrescribirá el valor anterior ("rojo") con el nuevo valor ("verde").

## Iterar sobre un diccionario

### Recorrer las claves

Para iterar a través de un diccionario e imprimir todas las claves:
```python
for clave in colores:
    print(clave)
```

También puedes usar el método `.keys()` explícitamente:
```python
for clave in colores.keys():
    print(clave)
```

### Recorrer los valores

Para iterar e imprimir todos los valores:
```python
for clave in colores:
    print(colores[clave])
```

O usando el método `.values()`:
```python
for valor in colores.values():
    print(valor)
```

### Recorrer claves y valores simultáneamente

La forma más eficiente de obtener ambos es usando el método `.items()`:
```python
for clave, valor in colores.items():
    print(f"La clave es {clave} y el valor es {valor}")
```

## Métodos útiles adicionales

### Verificar si una clave existe
```python
if "manzana" in colores:
    print("La clave 'manzana' existe en el diccionario")
```

### Obtener un valor con valor por defecto

Usa `.get()` para evitar errores si la clave no existe:
```python
color = colores.get("naranja", "no encontrado")
# Devuelve "no encontrado" si "naranja" no está en el diccionario
```

### Eliminar elementos
```python
# Eliminar un elemento específico
del colores["pera"]

# Eliminar y obtener el valor
valor_eliminado = colores.pop("banana")

# Eliminar todos los elementos
colores.clear()
```

### Obtener el número de elementos
```python
cantidad = len(colores)
print(f"El diccionario tiene {cantidad} elementos")
```

## Características importantes

- **Las claves deben ser únicas:** No puedes tener dos claves iguales en un diccionario
- **Las claves deben ser inmutables:** Puedes usar strings, números o tuplas como claves, pero no listas
- **Los valores pueden ser de cualquier tipo:** Listas, otros diccionarios, objetos, etc.
- **Los diccionarios son mutables:** Puedes modificarlos después de crearlos
- **Desde Python 3.7+:** Los diccionarios mantienen el orden de inserción

## Ejemplo completo
```python
# Crear un diccionario
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingeniería"
}

# Agregar información
estudiante["universidad"] = "MIT"

# Modificar información
estudiante["edad"] = 21

# Acceder a valores
print(f"{estudiante['nombre']} tiene {estudiante['edad']} años")

# Iterar sobre el diccionario
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
```

---

**Recurso creado para consulta rápida sobre diccionarios en Python** 🐍
