class Tarea:
    def __init__(self, id, descripcion):
        self.__id = id
        self.__descripcion = descripcion
        self.__completada = False

    def comprobar_id(self, id):
        return self.__id == id

    def comprobar_descripcion(self, descripcion):
        return self.__descripcion == descripcion

    def marcar_completada(self):
        self.__completada = True

    def esta_completada(self):
        return self.__completada


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



