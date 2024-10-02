from tarea import Tarea

class GestorTarea:
    def __init__(self):
        self.__lista_tareas = []

    def agregar_tarea(self, id, descripcion):
        nueva_tarea = Tarea(id, descripcion)
        self.__lista_tareas.append(nueva_tarea)

    def eliminar_tarea(self, id):
        for tarea in self.__lista_tareas:
            if  tarea.comprobar_id(id):
                self.__lista_tareas.remove(tarea)

    def marcar_tarea_completada(self, id):
        for tarea in self.__lista_tareas:
            if tarea.identificador_tarea(id):
                tarea.marcar_completada()

    def listar_tareas(self):
        return self.__lista_tareas

