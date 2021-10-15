import sys
from backend import Logica
from ventana_ingresar import VentanaIngresar
from ventana_sala import VentanaSala
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":

    app = QApplication(sys.argv)
# -------------Instancias---------------
    ventana_ingresar = VentanaIngresar()
    logica = Logica()
    ventana_sala = VentanaSala()

    ventana_ingresar.show()
# -------------Señales---------------
    ventana_ingresar.senal_enviar_nombre.connect(logica.validar_nombre)
    logica.senal_nombre_validado.connect(ventana_ingresar.recibir_validacion_nombre)
    ventana_ingresar.senal_abrir_sala.connect(ventana_sala.abrir)

    sys.exit(app.exec_())
