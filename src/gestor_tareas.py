from lista_tarea import GestorTarea
from ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__gestor_tarea = GestorTarea()

        self.__ui.Buttonagregar.clicked.connect(self.agregar_tarea)
        self.__ui.Buttoneliminar.clicked.connect(self.eliminar_tarea)
        self.__ui.Lista.itemChanged.connect(self.completar_tarea)

    def agregar_tarea(self):
        descripcion_tarea = self.__ui.lineEdit.text()
        if descripcion_tarea:
            id_tarea = len(self.__gestor_tarea.listar_tareas()) + 1
            self.__gestor_tarea.agregar_tarea(id_tarea, descripcion_tarea)

            item = QListWidgetItem(descripcion_tarea)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.__ui.Lista.addItem(item)
            self.__ui.lineEdit.clear()

    def completar_tarea(self, item):
        row = self.__ui.Lista.row(item)
        tarea = self.__gestor_tarea.listar_tareas()[row]

        if item.checkState() == Qt.Checked:
            tarea.marcar_completada()
            tachado = item.font()
            tachado.setStrikeOut(True)
            item.setFont(tachado)
        else:
            tachado = item.font()
            tachado.setStrikeOut(False)
            item.setFont(tachado)


    def eliminar_tarea(self):
        for item in self.__ui.Lista.selectedItems():
            row = self.__ui.Lista.row(item)
            self.__ui.Lista.takeItem(row)
        tarea = self.__gestor_tarea.listar_tareas()[row]
        self.__gestor_tarea.eliminar_tarea(tarea.get_id())

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
