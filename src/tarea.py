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





