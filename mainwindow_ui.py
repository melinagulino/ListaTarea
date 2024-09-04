# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QScrollBar,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(573, 478)
        MainWindow.setStyleSheet(u"background-color: rgb(154, 153, 150);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, -10, 761, 471))
        self.ingresar = QTextEdit(self.widget)
        self.ingresar.setObjectName(u"ingresar")
        self.ingresar.setGeometry(QRect(150, 30, 231, 31))
        self.ingresartarea = QLabel(self.widget)
        self.ingresartarea.setObjectName(u"ingresartarea")
        self.ingresartarea.setGeometry(QRect(10, 29, 131, 31))
        self.Buttonagregar = QPushButton(self.widget)
        self.Buttonagregar.setObjectName(u"Buttonagregar")
        self.Buttonagregar.setGeometry(QRect(390, 30, 91, 31))
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 100, 256, 192))
        self.verticalScrollBar = QScrollBar(self.widget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(290, 100, 16, 191))
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        self.listatarea = QLabel(self.widget)
        self.listatarea.setObjectName(u"listatarea")
        self.listatarea.setGeometry(QRect(60, 110, 181, 21))
        self.consultartarea = QLabel(self.widget)
        self.consultartarea.setObjectName(u"consultartarea")
        self.consultartarea.setGeometry(QRect(20, 330, 141, 21))
        self.consultar = QTextEdit(self.widget)
        self.consultar.setObjectName(u"consultar")
        self.consultar.setGeometry(QRect(160, 330, 231, 31))
        self.Buttoneliminar = QPushButton(self.widget)
        self.Buttoneliminar.setObjectName(u"Buttoneliminar")
        self.Buttoneliminar.setGeometry(QRect(400, 330, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 573, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ingresartarea.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#241f31;\">Ingresar tarea:</span></p></body></html>", None))
        self.Buttonagregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.listatarea.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#241f31;\">Lista de tareas</span></p></body></html>", None))
        self.consultartarea.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#241f31;\">Consultar tarea:</span></p><p><span style=\" font-size:14pt; color:#241f31;\"><br/></span></p></body></html>", None))
        self.Buttoneliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

