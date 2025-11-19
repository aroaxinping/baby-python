# 📚 Sistema de Gestión de Tareas - Python OOP

## 🎯 Descripción del Proyecto

Sistema de gestión de tareas (To-Do List) desarrollado en Python utilizando **Programación Orientada a Objetos (OOP)**. El proyecto demuestra el uso de clases, métodos, y encapsulamiento para crear una aplicación funcional y escalable.

## ✨ Características

- ✅ Agregar tareas con título y descripción
- ✅ Marcar tareas como completadas o pendientes
- ✅ Eliminar tareas por título
- ✅ Visualizar todas las tareas
- ✅ Filtrar tareas completadas
- ✅ Filtrar tareas pendientes
- ✅ Interfaz de consola amigable con emojis

## 🧠 Conceptos de OOP Aplicados

### Clases y Objetos
El proyecto utiliza dos clases principales:
- **`Tarea`**: Representa una tarea individual con sus propiedades y comportamientos
- **`ListaTareas`**: Gestiona una colección de tareas y proporciona operaciones de filtrado

### Encapsulamiento
Los atributos de cada clase están encapsulados y se acceden mediante métodos públicos, siguiendo las mejores prácticas de OOP.

### Métodos
Cada clase implementa métodos específicos que definen su comportamiento:
- Métodos de instancia para modificar estado
- Métodos de visualización para presentar información
- Métodos de filtrado para operaciones de búsqueda

## 🚀 Instalación y Uso

### Requisitos
- Python 3.x

### Ejecución
```bash
python tareas.py
```

### Ejemplo de Uso

```python
# Crear la lista de tareas
lista = ListaTareas()

# Crear tareas individuales
tarea1 = Tarea("Estudiar Python", "Repasar OOP y hacer ejercicios")
tarea2 = Tarea("Hacer ejercicio", "30 minutos de cardio")

# Agregar tareas a la lista
lista.agregar_tarea(tarea1)
lista.agregar_tarea(tarea2)

# Marcar tarea como completada
tarea1.marcar_completada()

# Visualizar tareas
lista.mostrar_todas()
lista.mostrar_completadas()
lista.mostrar_pendientes()

# Eliminar tarea
lista.eliminar_tarea("Hacer ejercicio")
```

## 📁 Estructura del Código

### Clase `Tarea`

```python
class Tarea:
    """Clase que representa una tarea individual"""
    
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self)
    def marcar_pendiente(self)
    def mostrar_info(self)
```

**Atributos:**
- `titulo`: Nombre de la tarea
- `descripcion`: Detalles de la tarea
- `completada`: Estado de la tarea (True/False)

**Métodos:**
- `marcar_completada()`: Cambia el estado a completada
- `marcar_pendiente()`: Cambia el estado a pendiente
- `mostrar_info()`: Muestra la información de la tarea

### Clase `ListaTareas`

```python
class ListaTareas:
    """Clase que gestiona múltiples tareas"""
    
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea)
    def eliminar_tarea(self, titulo)
    def mostrar_todas(self)
    def mostrar_completadas(self)
    def mostrar_pendientes(self)
```

**Atributos:**
- `tareas`: Lista de objetos `Tarea`

**Métodos:**
- `agregar_tarea()`: Añade una nueva tarea
- `eliminar_tarea()`: Elimina una tarea por título
- `mostrar_todas()`: Muestra todas las tareas
- `mostrar_completadas()`: Filtra y muestra tareas completadas
- `mostrar_pendientes()`: Filtra y muestra tareas pendientes

## 💻 Código Completo

```python
class Tarea:
    """Clase que representa una tarea individual"""
    
    def __init__(self, titulo, descripcion):
        """
        Constructor de la clase Tarea
        
        Args:
            titulo (str): El título de la tarea
            descripcion (str): La descripción de la tarea
        """
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """Marca la tarea como completada"""
        self.completada = True
        print(f"✅ Tarea '{self.titulo}' marcada como completada")

    def marcar_pendiente(self):
        """Marca la tarea como pendiente"""
        self.completada = False
        print(f"⏳ Tarea '{self.titulo}' marcada como pendiente")

    def mostrar_info(self):
        """Muestra toda la información de la tarea"""
        estado = "✅ Completada" if self.completada else "❌ Pendiente"
        print(f"\n--- Tarea ---")
        print(f"Título: {self.titulo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Estado: {estado}")


class ListaTareas:
    """Clase que gestiona múltiples tareas"""
    
    def __init__(self):
        """Constructor que inicializa una lista vacía de tareas"""
        self.tareas = []

    def agregar_tarea(self, tarea):
        """
        Agrega una tarea a la lista
        
        Args:
            tarea (Tarea): Objeto de tipo Tarea a agregar
        """
        self.tareas.append(tarea)
        print(f"➕ Tarea '{tarea.titulo}' agregada")

    def eliminar_tarea(self, titulo):
        """
        Elimina una tarea de la lista por su título
        
        Args:
            titulo (str): El título de la tarea a eliminar
        """
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"🗑️ Tarea '{titulo}' eliminada")
                return
        print(f"⚠️ No se encontró la tarea '{titulo}'")

    def mostrar_todas(self):
        """Muestra todas las tareas en la lista"""
        if len(self.tareas) == 0:
            print("\n📭 No hay tareas")
        else:
            print("\n" + "="*40)
            print("📋 TODAS LAS TAREAS")
            print("="*40)
            for tarea in self.tareas:
                tarea.mostrar_info()

    def mostrar_completadas(self):
        """Muestra solo las tareas completadas"""
        print("\n" + "="*40)
        print("✅ TAREAS COMPLETADAS")
        print("="*40)
        hay_completadas = False
        for tarea in self.tareas:
            if tarea.completada:
                tarea.mostrar_info()
                hay_completadas = True
        if not hay_completadas:
            print("\n📭 No hay tareas completadas")

    def mostrar_pendientes(self):
        """Muestra solo las tareas pendientes"""
        print("\n" + "="*40)
        print("⏳ TAREAS PENDIENTES")
        print("="*40)
        hay_pendientes = False
        for tarea in self.tareas:
            if not tarea.completada:
                tarea.mostrar_info()
                hay_pendientes = True
        if not hay_pendientes:
            print("\n📭 No hay tareas pendientes")


# ==========================================
# EJEMPLO DE USO
# ==========================================

if __name__ == "__main__":
    # Crear la lista de tareas
    lista = ListaTareas()
    
    # Crear tareas individuales
    tarea1 = Tarea("Estudiar Python", "Repasar OOP y hacer ejercicios")
    tarea2 = Tarea("Hacer ejercicio", "30 minutos de cardio")
    tarea3 = Tarea("Leer libro", "Terminar capítulo 5 de Clean Code")
    tarea4 = Tarea("Proyecto GitHub", "Documentar aprendizaje de OOP")
    
    # Agregar tareas a la lista
    lista.agregar_tarea(tarea1)
    lista.agregar_tarea(tarea2)
    lista.agregar_tarea(tarea3)
    lista.agregar_tarea(tarea4)
    
    # Marcar algunas tareas como completadas
    tarea1.marcar_completada()
    tarea2.marcar_completada()
    
    # Mostrar todas las tareas
    lista.mostrar_todas()
    
    # Mostrar solo completadas
    lista.mostrar_completadas()
    
    # Mostrar solo pendientes
    lista.mostrar_pendientes()
    
    # Eliminar una tarea
    lista.eliminar_tarea("Leer libro")
    
    # Mostrar todas después de eliminar
    lista.mostrar_todas()
```

## 🔧 Posibles Mejoras

- Persistencia de datos (guardar tareas en archivo JSON o base de datos)
- Prioridad de tareas (alta, media, baja)
- Fechas de vencimiento
- Categorías o etiquetas
- Interfaz gráfica con Tkinter o PyQt
- API REST con Flask o FastAPI

## 🛠️ Tecnologías

- **Python 3.x**
- Programación Orientada a Objetos (OOP)

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

**Última actualización:** Noviembre 2025
