import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication



window_name, base_class = uic.loadUiType("ventana_ingresar.ui")


class VentanaIngresar(window_name, base_class, QObject):

    senal_enviar_nombre = pyqtSignal(str)
    senal_abrir_sala = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ventana de inicio")
        self.boton_ingresar.clicked.connect(self.enviar_nombre)

    def enviar_nombre(self):
        texto = self.input_nombre.text()
        self.senal_enviar_nombre.emit(texto)

    def recibir_validacion_nombre(self, validacion):

        if validacion is True:
            self.hide()
            self.senal_abrir_sala.emit()
        else:
            self.input_nombre.setText("Nombre Invalido")


if __name__ == '__main__':

    app = QApplication([])
    form = VentanaSala()
    form.show()
    sys.exit(app.exec_())
