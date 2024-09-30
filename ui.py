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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 362)
        MainWindow.setStyleSheet(u"background-color: rgb(154, 153, 150);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, -10, 761, 471))
        self.widget.setStyleSheet(u"color: rgb(251, 245, 245);")
        self.Buttonagregar = QPushButton(self.widget)
        self.Buttonagregar.setObjectName(u"Buttonagregar")
        self.Buttonagregar.setGeometry(QRect(210, 20, 80, 23))
        self.Lista = QListWidget(self.widget)
        self.Lista.setObjectName(u"Lista")
        self.Lista.setGeometry(QRect(5, 51, 371, 241))
        self.Lista.setStyleSheet(u"color: rgb(251, 245, 245);")
        self.Buttoneliminar = QPushButton(self.widget)
        self.Buttoneliminar.setObjectName(u"Buttoneliminar")
        self.Buttoneliminar.setGeometry(QRect(220, 300, 111, 31))
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 191, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 499, 20))
        self.menuLista_de_Tareas = QMenu(self.menubar)
        self.menuLista_de_Tareas.setObjectName(u"menuLista_de_Tareas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLista_de_Tareas.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Buttonagregar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Buttonagregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Buttoneliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.menuLista_de_Tareas.setTitle(QCoreApplication.translate("MainWindow", u"Lista de Tareas", None))
    # retranslateUi

