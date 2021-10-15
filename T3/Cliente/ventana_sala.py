import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication



window_name, base_class = uic.loadUiType("ventana_sala.ui")


class VentanaSala(window_name, base_class, QObject):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def abrir(self):
        self.show()
