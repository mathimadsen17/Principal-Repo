import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication



window_name, base_class = uic.loadUiType("ventana_juego.ui")


class VentanaJuego(window_name, base_class, QObject):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ventana de juego")

    def abrir(self):
        self.show()


if __name__ == '__main__':

    app = QApplication([])
    form = VentanaJuego()
    form.show()
    sys.exit(app.exec_())
