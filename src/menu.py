from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt
from mainwindow_ui import Ui_MainWindow
from lista_tarea import Tarea

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tarea = Tarea()

        self.ui.Buttonagregar.clicked.connect(self.agregar_tarea)
        self.ui.Buttoneliminar.clicked.connect(self.eliminar_tarea)
        self.ui.listWidget.itemChanged.connect(self.completar_tarea)  #

    def agregar_tarea(self):
        tarea_ingresada = self.ui.ingresar.toPlainText()
        if self.tarea.agregar_una_tarea(tarea_ingresada):
            item = QListWidgetItem(tarea_ingresada)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.ui.listWidget.addItem(item)
            self.ui.ingresar.clear()

    def eliminar_tarea(self):
        tarea_ingresada = self.ui.consultar.toPlainText()
        if self.tarea.eliminar_tarea(tarea_ingresada):
            items = self.ui.listWidget.findItems(tarea_ingresada, Qt.MatchExactly)
            if items:
                for item in items:
                    self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
            self.ui.consultar.clear()

    def completar_tarea(self, item):
        if item.checkState() == Qt.Checked:
            tarea_ingresada = item.text()
            if self.tarea.completar_tarea(tarea_ingresada):
                return True

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
