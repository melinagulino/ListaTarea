
class Tarea:
    def __init__(self):
        self.__lista_tareas = []
        self.tareas_completas = []

    def agregar_una_tarea(self, tarea):
        if tarea in self.__lista_tareas:
            return False
        self.__lista_tareas.append(tarea)
        return True

    def completar_tarea(self, tarea_completa):
        if tarea_completa.lower() in [t.lower() for t in self.__lista_tareas]:
            self.tareas_completas.append(tarea_completa)
            return True
        return False

    def eliminar_tarea(self, tarea):
        if tarea in self.__lista_tareas:
            self.__lista_tareas.remove(tarea)
            return True
        return False

