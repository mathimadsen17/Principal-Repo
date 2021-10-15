import sys
import os
from PyQt5 import uic, QtMultimedia
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import (QObject, pyqtSignal)


window_name, base_class = uic.loadUiType("ventana_preparacion.ui")

class VentanaPreparacion(window_name, base_class, QObject):
    
    senal_abrir_ventana_juego = pyqtSignal(str,str)
    senal_dificultad = pyqtSignal(str)
    
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.personaje = None
        self.setWindowTitle("Ventana Preparación")
        self.dificultad = None
        self.checkbox_homero.clicked.connect(self.mostrar_homero)
        self.checkbox_lisa.clicked.connect(self.mostrar_lisa)
        self.checkbox_intro.clicked.connect(self.dificultad_intro)
        self.checkbox_avanzada.clicked.connect(self.dificultad_avanzada)
        
        

    def abrir_ventana_preparacion(self):
        
        self.show()

    
    def mostrar_homero(self):
        
        self.personaje = "Homero"
        
        
        ruta_foto = os.path.join("sprites","Personajes","Homero","down_3.png")
        
        pixeles = QPixmap(ruta_foto)
        
        self.label_personaje.setPixmap(pixeles)
        
        self.label_personaje.setScaledContents(True)
    
    def mostrar_lisa(self):
        
        self.personaje = "Lisa"
        
        
        ruta_foto = os.path.join("sprites","Personajes","Lisa","down_1.png")
        
        pixeles = QPixmap(ruta_foto)
        
        self.label_personaje.setPixmap(pixeles)
        
        self.label_personaje.setScaledContents(True)
    
    def verificar_interseccion(self):
        
        planta = self.label_planta.geometry()
        escuela = self.label_escuela.geometry()
        personaje = self.label_personaje.geometry()
        
        if self.personaje == "Homero":
            if personaje.intersects(planta)==True:
                self.hide()
                self.senal_abrir_ventana_juego.emit(self.personaje,self.dificultad)
        if self.personaje == "Lisa":
            if personaje.intersects(escuela)==True:
                self.hide()
                self.senal_abrir_ventana_juego.emit(self.personaje,self.dificultad)
    
    def keyPressEvent(self,event):
        
        x = self.label_personaje.x()
        y = self.label_personaje.y()
        
        if self.personaje == "Homero":
        
            if event.key() == QtCore.Qt.Key_W:
                
                ruta_foto = os.path.join("sprites","Personajes","Homero","up_1.png")
            
                pixeles = QPixmap(ruta_foto)
            
                self.label_personaje.setPixmap(pixeles)
            
                self.label_personaje.setScaledContents(True)
                
                self.label_personaje.move(x,y-10)
                
                self.verificar_interseccion()
                
            elif event.key() == QtCore.Qt.Key_S:
                
                ruta_foto = os.path.join("sprites","Personajes","Homero","down_1.png")
            
                pixeles = QPixmap(ruta_foto)
            
                self.label_personaje.setPixmap(pixeles)
            
                self.label_personaje.setScaledContents(True)
                
                self.label_personaje.move(x,y+10)
                
                self.verificar_interseccion()
                pass
                
            elif event.key() == QtCore.Qt.Key_A:
                
                ruta_foto = os.path.join("sprites","Personajes","Homero","left_3.png")
            
                pixeles = QPixmap(ruta_foto)
            
                self.label_personaje.setPixmap(pixeles)
            
                self.label_personaje.setScaledContents(True)
                
                self.label_personaje.move(x-10,y)
                
                self.verificar_interseccion()
                pass
                
            elif event.key() == QtCore.Qt.Key_D:
                
                ruta_foto = os.path.join("sprites","Personajes","Homero","right_3.png")
            
                pixeles = QPixmap(ruta_foto)
            
                self.label_personaje.setPixmap(pixeles)
            
                self.label_personaje.setScaledContents(True)
                
                self.label_personaje.move(x+10,y)
                
                self.verificar_interseccion()
                pass
        
        if self.personaje == "Lisa":
        
            if event.key() == QtCore.Qt.Key_W:
                
                ruta_foto = os.path.join("sprites","Personajes","Lisa","up_2.png")
            
                pixeles = QPixmap(ruta_foto)
            
                self.label_personaje.setPixmap(pixeles)
            
                self.label_personaje.setScaledContents(True)
                
                self.label_personaje.move(x,y-10)
                
                self.verificar_interseccion()
                
                
            elif event.key() == QtCore.Qt.Key_S:
                
                ruta_foto = os.path.join("sprites","Personajes","Lisa","down_2.png")
            
                pixeles = QPixmap(ruta_foto)
            
                self.label_personaje.setPixmap(pixeles)
            
                self.label_personaje.setScaledContents(True)
                
                self.label_personaje.move(x,y+10)
                
                self.verificar_interseccion()
                pass
                
            elif event.key() == QtCore.Qt.Key_A:
                
                ruta_foto = os.path.join("sprites","Personajes","Lisa","left_1.png")
            
                pixeles = QPixmap(ruta_foto)
            
                self.label_personaje.setPixmap(pixeles)
            
                self.label_personaje.setScaledContents(True)
                
                self.label_personaje.move(x-10,y)
                
                self.verificar_interseccion()
                pass
                
            elif event.key() == QtCore.Qt.Key_D:
                
                ruta_foto = os.path.join("sprites","Personajes","Lisa","right_2.png")
            
                pixeles = QPixmap(ruta_foto)
            
                self.label_personaje.setPixmap(pixeles)
            
                self.label_personaje.setScaledContents(True)
                
                self.label_personaje.move(x+10,y)
                
                self.verificar_interseccion()
                pass
            
    def dificultad_intro(self):
        
        self.dificultad = "Intro"
        pass
    
    def dificultad_avanzada(self):
        
        self.dificultad = "Avanzada"
        pass
    
    def actualizar_ronda(self,ronda):
        
        self.label_rondas.setText(f"RONDA: {ronda}")
    
    def barrita_vida(self, vida):
        
        self.barra_vida.setValue(vida)
    
    def actualizar_puntaje(self, puntaje_total):
        
        self.label_puntaje.setText(f"PUNTAJE TOTAL: {puntaje_total}")
    
    
    def mostrar_items(self, buenos, malos):
        
        self.label_items_buenos.setText(f"ITEMS BUENOS: {buenos}")
        self.label_items_malos.setText(f"ITEMS MALOS: {malos}")
        
        
        
        