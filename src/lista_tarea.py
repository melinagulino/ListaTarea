class Tarea:
    def __init__(self):
        self.lista_tareas = []
        self.tareas_completas = []

    def agregar_una_tarea(self, tarea):
        if tarea:
            self.lista_tareas.append(tarea)
            return True
        return False

    def completar_tarea(self, tarea_completa):
        if tarea_completa:
            self.tareas_completas.append(tarea_completa)
            print("La tarea ha sido completada")
            return True
        return False

    def eliminar_tarea(self, tarea):
        if tarea in self.lista_tareas:
            self.lista_tareas.remove(tarea)
            return True
        return False