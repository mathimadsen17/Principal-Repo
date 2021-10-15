import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import (QObject, pyqtSignal)


window_name, base_class = uic.loadUiType("ventana_post.ui")

class VentanaPost(window_name, base_class, QObject):
    
    senal_continuar_jugando = pyqtSignal()
    senal_enviar_puntaje = pyqtSignal(str,int)
    
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_continuar_jugando.clicked.connect(self.continuar_jugando)
        self.usuario = None
        self.puntaje_total = 0
        
        
    def abrir_ventana(self):
        self.show()
        
    def actualizar_puntaje(self, puntaje):
        
        self.puntaje_total += puntaje
        self.label_puntaje_ronda.setText(f"{puntaje}")    

    def salir(self):
        
        self.hide()
    
    def continuar_jugando(self):
        
        self.senal_continuar_jugando.emit()
        self.hide()
    
    def mostrar_vida(self,vida):
        
        self.label_vida.setText(f"{vida}0%")
        
        if vida <= 0:
            self.label_cartel.setText("    Ya no puedes seguir jugando")
            self.label_cartel.setStyleSheet("background-color: red")
            self.enviar_puntaje()
            self.label_vida.setText("0%")
            
            
    
    def mostrar_items_buenos(self, items):
        
        self.label_items_buenos.setText(f"{items}")
        
    def mostrar_items_malos(self, items):
        
        self.label_items_malos.setText(f"{items}")   
    
    def recibir_usuario(self,usuario):
        
        self.usuario = usuario
        
    def enviar_puntaje(self):
        
        self.senal_enviar_puntaje.emit(self.usuario, self.puntaje_total)
        
        