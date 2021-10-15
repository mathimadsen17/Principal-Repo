import sys
import os
from PyQt5 import uic, QtMultimedia
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtCore import (QObject, pyqtSignal)


window_name, base_class = uic.loadUiType("ventana_inicio.ui")


class VentanaInicio(window_name, base_class, QObject):
    
    senal_enviar_nombre = pyqtSignal(str)
    senal_abrir_ranking =pyqtSignal()
    senal_abrir_preparacion = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Ventana Inicio")

        self.boton_iniciar_partida.clicked.connect(self.enviar_nombre)
        self.boton_iniciar_partida.clicked.connect(self.poner_musica)
        self.boton_ventana_ranking.clicked.connect(self.abrir_ranking)
        

    def enviar_nombre(self):
        
        texto = self.linea_texto_usuario.text()
        
        self.senal_enviar_nombre.emit(texto)
    
    def recibir_validacion(self,validado):
        
        if validado:
            self.hide()
            self.senal_abrir_preparacion.emit()
            
        else:
            self.linea_texto_usuario.clear()
            self.line_edit_nombre.setPlaceholderText("Nombre inválido")
    
    def abrir_ranking(self):
    
        self.hide()
        
        self.senal_abrir_ranking.emit()
        
    def abrir_ventana_inicio(self):
        
        self.show()

    
    def poner_musica(self):
        
        QtMultimedia.QSound.play(os.path.join("sprites","canciones","musica.wav"))   
    
        
