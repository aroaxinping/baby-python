class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True
        print(f"Tarea '{self.titulo}' marcada como completada")

    def marcar_pendiente(self):
        self.completada = False
        print(f"Tarea '{self.titulo}' marcada como pendiente")

    def mostrar_info(self):
        estado = "✅ Completada" if self.completada else "❌ Pendiente"
        print(f"\n--- Tarea ---")
        print(f"Título: {self.titulo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Estado: {estado}")


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.titulo}' agregada")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"Tarea '{titulo}' eliminada")
                return
        print(f"No se encontró la tarea '{titulo}'")

    def mostrar_todas(self):
        if len(self.tareas) == 0:
            print("\nNo hay tareas")
        else:
            print("\n=== TODAS LAS TAREAS ===")
            for tarea in self.tareas:
                tarea.mostrar_info()

    def mostrar_completadas(self):
        print("\n=== TAREAS COMPLETADAS ===")
        hay_completadas = False
        for tarea in self.tareas:
            if tarea.completada:
                tarea.mostrar_info()
                hay_completadas = True
        if not hay_completadas:
            print("No hay tareas completadas")

    def mostrar_pendientes(self):
        print("\n=== TAREAS PENDIENTES ===")
        hay_pendientes = False
        for tarea in self.tareas:
            if not tarea.completada:
                tarea.mostrar_info()
                hay_pendientes = True
        if not hay_pendientes:
            print("No hay tareas pendientes")


