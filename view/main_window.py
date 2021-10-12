import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QTabWidget,QWidget
class Main_Window(QDialog):
    def __init__(self):
        super(Main_Window,self).__init__()
        loadUi("view/ui/layout pokemon.ui",self)
        self.tabWidget.currentChanged.connect(self.cambiatab)

    def cambiatab(self):
        print(self.tabWidget.currentIndex())

