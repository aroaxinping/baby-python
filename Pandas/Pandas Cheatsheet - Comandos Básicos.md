# 🐼 Pandas Cheatsheet - Comandos Básicos

## 📚 Tabla de Contenidos
1. [Importar Pandas](#importar-pandas)
2. [Crear DataFrames](#crear-dataframes)
3. [Ver y Explorar Datos](#ver-y-explorar-datos)
4. [Seleccionar Datos](#seleccionar-datos)
5. [Filtrar Datos](#filtrar-datos)
6. [Ordenar Datos](#ordenar-datos)
7. [Agregar y Eliminar Columnas](#agregar-y-eliminar-columnas)
8. [Operaciones Matemáticas](#operaciones-matemáticas)
9. [Estadísticas Básicas](#estadísticas-básicas)

---

## Importar Pandas

```python
import pandas as pd
```

**Explicación:** Importa la librería Pandas y le da el alias `pd` (convención estándar).

---

## Crear DataFrames

### Desde un diccionario

```python
datos = {
    'columna1': [valor1, valor2, valor3],
    'columna2': [valor1, valor2, valor3]
}

df = pd.DataFrame(datos)
```

**Explicación:** Crea un DataFrame a partir de un diccionario. Cada clave es una columna.

**Ejemplo:**
```python
estudiantes = {
    'nombre': ['Dan', 'Ana', 'Luis'],
    'edad': [25, 22, 28],
    'nota': [8.5, 9.0, 7.5]
}

df = pd.DataFrame(estudiantes)
```

---

## Ver y Explorar Datos

### Ver el DataFrame completo

```python
print(df)
```

**Explicación:** Muestra todo el DataFrame.

---

### Ver primeras filas

```python
df.head()      # Primeras 5 filas (por defecto)
df.head(3)     # Primeras 3 filas
```

**Explicación:** Útil para explorar rápidamente los datos sin ver todo.

---

### Ver últimas filas

```python
df.tail()      # Últimas 5 filas (por defecto)
df.tail(3)     # Últimas 3 filas
```

---

### Información del DataFrame

```python
df.info()
```

**Explicación:** Muestra el tipo de datos de cada columna, valores no nulos, y uso de memoria.

**Ejemplo de salida:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   nombre  3 non-null      object 
 1   edad    3 non-null      int64  
 2   nota    3 non-null      float64
```

---

### Forma del DataFrame (filas y columnas)

```python
df.shape
```

**Explicación:** Devuelve una tupla `(filas, columnas)`.

**Ejemplo:** `(5, 3)` = 5 filas, 3 columnas

---

### Ver nombres de columnas

```python
df.columns
```

**Explicación:** Devuelve una lista con los nombres de todas las columnas.

---

### Ver tipos de datos

```python
df.dtypes
```

**Explicación:** Muestra el tipo de dato de cada columna (int, float, object, etc.).

---

## Seleccionar Datos

### Seleccionar UNA columna

```python
df['nombre_columna']
```

**Explicación:** Devuelve una **Series** (una columna).

**Ejemplo:**
```python
nombres = df['nombre']
```

---

### Seleccionar MÚLTIPLES columnas

```python
df[['columna1', 'columna2']]
```

**Explicación:** Devuelve un **DataFrame** con solo esas columnas. **Nota:** doble corchete `[[]]`

**Ejemplo:**
```python
df_reducido = df[['nombre', 'edad']]
```

---

### Seleccionar UNA fila por índice

```python
df.iloc[0]        # Primera fila (índice 0)
df.iloc[2]        # Tercera fila (índice 2)
df.iloc[-1]       # Última fila
```

**Explicación:** `iloc` = index location (ubicación por índice numérico).

---

### Seleccionar MÚLTIPLES filas

```python
df.iloc[0:3]      # Filas 0, 1, 2 (el 3 no se incluye)
df.iloc[1:4]      # Filas 1, 2, 3
```

---

### Seleccionar fila y columna específica

```python
df.iloc[0, 1]           # Fila 0, columna 1
df.loc[0, 'nombre']     # Fila 0, columna 'nombre'
```

**Explicación:** 
- `iloc` = por índice numérico
- `loc` = por nombre de columna

---

## Filtrar Datos

### Filtro simple

```python
df[df['columna'] > valor]
df[df['columna'] == valor]
df[df['columna'] >= valor]
```

**Explicación:** Filtra filas donde la condición es `True`.

**Ejemplo:**
```python
# Estudiantes con nota mayor a 8
aprobados = df[df['nota'] > 8]

# Estudiantes de edad 25
edad_25 = df[df['edad'] == 25]
```

---

### Filtro AND (`&`)

```python
df[(df['columna1'] > valor1) & (df['columna2'] == valor2)]
```

**Explicación:** Ambas condiciones deben cumplirse. **Importante:** Cada condición entre paréntesis.

**Ejemplo:**
```python
# Estudiantes mayores de 23 Y con nota > 8
filtro = df[(df['edad'] > 23) & (df['nota'] > 8)]
```

---

### Filtro OR (`|`)

```python
df[(df['columna1'] > valor1) | (df['columna2'] == valor2)]
```

**Explicación:** Al menos una condición debe cumplirse.

**Ejemplo:**
```python
# Estudiantes con nota > 9 O edad < 24
filtro = df[(df['nota'] > 9) | (df['edad'] < 24)]
```

---

### Filtro NOT (`~`)

```python
df[~(df['columna'] == valor)]
```

**Explicación:** Lo contrario de la condición.

**Ejemplo:**
```python
# Estudiantes que NO tienen 25 años
filtro = df[~(df['edad'] == 25)]
```

---

### Filtro con múltiples valores (`.isin()`)

```python
df[df['columna'].isin([valor1, valor2, valor3])]
```

**Explicación:** Filtra filas donde el valor está en la lista.

**Ejemplo:**
```python
# Estudiantes llamados Dan, Ana o Luis
filtro = df[df['nombre'].isin(['Dan', 'Ana', 'Luis'])]
```

---

### Filtro "entre valores"

```python
df[(df['columna'] >= valor_min) & (df['columna'] <= valor_max)]
```

**Ejemplo:**
```python
# Notas entre 7 y 9
filtro = df[(df['nota'] >= 7) & (df['nota'] <= 9)]
```

---

## Ordenar Datos

### Ordenar por una columna

```python
df.sort_values('columna')                    # Ascendente (menor a mayor)
df.sort_values('columna', ascending=False)   # Descendente (mayor a menor)
```

**Ejemplo:**
```python
# Ordenar por nota de mayor a menor
df_ordenado = df.sort_values('nota', ascending=False)
```

---

### Ordenar por múltiples columnas

```python
df.sort_values(['columna1', 'columna2'])
```

**Ejemplo:**
```python
# Ordenar por edad y luego por nota
df_ordenado = df.sort_values(['edad', 'nota'])
```

---

## Agregar y Eliminar Columnas

### Agregar una columna nueva

```python
df['nueva_columna'] = valores
```

**Ejemplo:**
```python
# Agregar columna con cálculo
df['nota_doble'] = df['nota'] * 2

# Agregar columna con valor fijo
df['curso'] = 'Python'
```

---

### Agregar columna basada en condición

```python
df['nueva_columna'] = df['columna'].apply(lambda x: valor_si_true if condicion else valor_si_false)
```

**Ejemplo:**
```python
# Agregar columna 'aprobado' (True/False)
df['aprobado'] = df['nota'] >= 5
```

---

### Eliminar columnas

```python
df.drop('columna', axis=1, inplace=True)        # Eliminar una columna
df.drop(['col1', 'col2'], axis=1, inplace=True) # Eliminar múltiples
```

**Explicación:** 
- `axis=1` indica columnas (axis=0 sería filas)
- `inplace=True` modifica el DataFrame original

**Sin inplace:**
```python
df_nuevo = df.drop('columna', axis=1)  # Crea nuevo DataFrame sin modificar el original
```

---

## Operaciones Matemáticas

### Operaciones básicas en columnas

```python
df['columna'] + 10          # Suma 10 a todos los valores
df['columna'] - 5           # Resta 5
df['columna'] * 2           # Multiplica por 2
df['columna'] / 3           # Divide por 3
```

**Ejemplo:**
```python
# Aumentar todas las notas en 0.5
df['nota'] = df['nota'] + 0.5
```

---

### Operaciones entre columnas

```python
df['nueva'] = df['columna1'] + df['columna2']
df['nueva'] = df['columna1'] * df['columna2']
```

**Ejemplo:**
```python
# Calcular salario anual
df['salario_anual'] = df['salario_mensual'] * 12
```

---

## Estadísticas Básicas

### Promedio (media)

```python
df['columna'].mean()
```

**Ejemplo:**
```python
promedio_notas = df['nota'].mean()
print(f"Promedio: {promedio_notas}")
```

---

### Suma

```python
df['columna'].sum()
```

**Ejemplo:**
```python
total_edad = df['edad'].sum()
```

---

### Valor máximo

```python
df['columna'].max()
```

**Ejemplo:**
```python
nota_maxima = df['nota'].max()
```

---

### Valor mínimo

```python
df['columna'].min()
```

---

### Contar valores

```python
df['columna'].count()      # Cuenta valores no nulos
df.shape[0]                # Número total de filas
len(df)                    # Número total de filas (alternativa)
```

---

### Mediana

```python
df['columna'].median()
```

**Explicación:** Valor central cuando los datos están ordenados.

---

### Desviación estándar

```python
df['columna'].std()
```

**Explicación:** Mide la dispersión de los datos.

---

### Estadísticas completas

```python
df.describe()
```

**Explicación:** Muestra count, mean, std, min, 25%, 50%, 75%, max para columnas numéricas.

**Ejemplo de salida:**
```
            edad       nota
count   3.000000   3.000000
mean   25.000000   8.333333
std     3.000000   0.763763
min    22.000000   7.500000
25%    23.500000   7.750000
50%    25.000000   8.500000
75%    26.500000   8.750000
max    28.000000   9.000000
```

---

### Valores únicos

```python
df['columna'].unique()          # Array con valores únicos
df['columna'].nunique()         # Número de valores únicos
```

**Ejemplo:**
```python
# Ver qué departamentos hay
departamentos = df['departamento'].unique()

# Contar cuántos departamentos diferentes hay
num_departamentos = df['departamento'].nunique()
```

---

### Contar frecuencias

```python
df['columna'].value_counts()
```

**Explicación:** Cuenta cuántas veces aparece cada valor.

**Ejemplo:**
```python
# Contar cuántos empleados hay por departamento
df['departamento'].value_counts()

# Salida:
# IT            3
# RRHH          2
# Marketing     1
```

---

## 🎯 Comandos Más Usados - Resumen Rápido

| Comando | Para qué sirve |
|---------|----------------|
| `pd.DataFrame(datos)` | Crear DataFrame |
| `df.head()` | Ver primeras filas |
| `df.info()` | Información general |
| `df['columna']` | Seleccionar una columna |
| `df[['col1', 'col2']]` | Seleccionar múltiples columnas |
| `df.iloc[0]` | Seleccionar fila por índice |
| `df[df['col'] > valor]` | Filtrar datos |
| `(condicion1) & (condicion2)` | Filtro AND |
| `(condicion1) \| (condicion2)` | Filtro OR |
| `~(condicion)` | Filtro NOT |
| `df.sort_values('col')` | Ordenar |
| `df['nueva'] = valores` | Agregar columna |
| `df['col'].mean()` | Promedio |
| `df['col'].sum()` | Suma |
| `df['col'].max()` | Máximo |
| `df['col'].min()` | Mínimo |
| `df.describe()` | Estadísticas completas |
| `df['col'].value_counts()` | Contar frecuencias |

---

## 💡 Consejos Importantes

1. **No memorices todo:** Usa este cheatsheet como referencia
2. **Paréntesis en filtros:** Siempre usa `(condicion1) & (condicion2)`
3. **Doble corchete:** Para múltiples columnas usa `[[]]`
4. **df vs df['col']:** 
   - `df` = DataFrame completo (tabla)
   - `df['col']` = Series (una columna)
5. **Google es tu amigo:** Busca "pandas how to..." cuando tengas dudas

---

## 📚 Recursos Adicionales

- [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet (oficial)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

---

**Última actualización:** Noviembre 2025
