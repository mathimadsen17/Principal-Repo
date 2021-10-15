from PyQt5.QtCore import QObject, pyqtSignal


class Logica(QObject):

    senal_nombre_validado = pyqtSignal(bool)

    def __init__(self):

        super().__init__()

    def validar_nombre(self, nombre):
        if nombre.isalnum() is True and len(nombre) < 15:
            self.senal_nombre_validado.emit(True)
        else:
            self.senal_nombre_validado.emit(False)
