import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel 
from PyQt5.QtCore import (QObject, pyqtSignal, QRect, QThread, QTimer)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
import random
import backend.parametros as p
from time import sleep
from backend.clases import ThreadTiempo , ThreadObjeto

window_name, base_class = uic.loadUiType("ventana_juego.ui")

class VentanaJuego(window_name, base_class, QObject):

    senal_thread = pyqtSignal(str)
    senal_generar_objeto = pyqtSignal()
    senal_generar_objetox2 = pyqtSignal()
    senal_salir = pyqtSignal()
    senal_salir_post = pyqtSignal()
    senal_mandar_resultados = pyqtSignal(int,int,int)
    senal_actualizar_ronda = pyqtSignal(int)
    senal_enviar_vida = pyqtSignal(int)
    senal_enviar_ob_malos = pyqtSignal(int)
    senal_enviar_ob_buenos = pyqtSignal(int)
    senal_enviar_puntaje = pyqtSignal(int)
    senal_enviar_items = pyqtSignal(int,int)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ventana Juego")
        self.personaje = None
        self.boton_salir.clicked.connect(self.salir)
        self.thread = None
        self.thread_objeto = None
        self.senal_thread.connect(self.actualizar_labels)
        self.senal_generar_objeto.connect(self.generador_objetos)
        self.senal_generar_objetox2.connect(self.generador_objetosx2)
        self.senal_salir.connect(self.mostrar_postronda)
        self.objeto = None
        self.ob_buenos = 0
        self.ob_malos = 0
        self.obx2 = 0
        self.puntaje = 0
        self.activo = True
        self.activo2 = True
        self.vida = 10
        self.ronda = 1
        self.puntaje_total = 0
        self.ob_buenos_total = 0
        self.ob_malos_total = 0
        
        
    def abrir_ventana(self,personaje,dificultad):
        
        self.personaje = personaje
        self.ob_buenos = 0
        self.ob_malos = 0
        self.mostrar_mapa(personaje)
        self.mostrar_obstaculos()
        self.show()
        self.temporizador(dificultad)
        self.generar_objetos(dificultad)
        self.barrita_vida()
        self.label_puntaje.setText("PUNTAJE: 0")

    
    def mostrar_mapa(self, personaje):
        
        if personaje == "Homero":
        
            ruta_foto = os.path.join("sprites","Mapa","Planta_nuclear","Mapa.png")
            pixeles = QPixmap(ruta_foto)
            self.label_mapa.setPixmap(pixeles)
            self.label_mapa.setScaledContents(True)
            ruta_foto1 = os.path.join("sprites","Personajes","Homero","down_3.png")
            pixeles1 = QPixmap(ruta_foto1)
            self.label_personaje.setPixmap(pixeles1)
            self.label_personaje.setScaledContents(True)    
            
        if personaje == "Lisa":
            
            ruta_foto = os.path.join("sprites","Mapa","Primaria","Mapa.png")
            pixeles = QPixmap(ruta_foto)
            self.label_mapa.setPixmap(pixeles)
            self.label_mapa.setScaledContents(True)   
            ruta_foto1 = os.path.join("sprites","Personajes","Lisa","down_1.png")
            pixeles1 = QPixmap(ruta_foto1)
            self.label_personaje.setPixmap(pixeles1)
            self.label_personaje.setScaledContents(True)   
            
    def keyPressEvent(self,event):
        
        x = self.label_personaje.x()
        y = self.label_personaje.y()
        
        if self.personaje == "Homero":
        
            if event.key() == QtCore.Qt.Key_W:
                
                if self.verificar_restriccion_obstaculo("W") == False:
                    ruta_foto = os.path.join("sprites","Personajes","Homero","up_1.png")
                    pixeles = QPixmap(ruta_foto)
                    self.label_personaje.setPixmap(pixeles)
                    self.label_personaje.setScaledContents(True)
                    self.label_personaje.move(x,y-p.VELOCIDAD_HOMERO)
                    self.verificar_interseccion()
        
                
            elif event.key() == QtCore.Qt.Key_S:
                
                if self.verificar_restriccion_obstaculo("S") == False:
                    ruta_foto = os.path.join("sprites","Personajes","Homero","down_1.png")
                    pixeles = QPixmap(ruta_foto)
                    self.label_personaje.setPixmap(pixeles)
                    self.label_personaje.setScaledContents(True)
                    self.label_personaje.move(x,y+p.VELOCIDAD_HOMERO)
                    self.verificar_interseccion()
                
            elif event.key() == QtCore.Qt.Key_A:
                
                if self.verificar_restriccion_obstaculo("A") == False:
                    ruta_foto = os.path.join("sprites","Personajes","Homero","left_3.png")
                    pixeles = QPixmap(ruta_foto)
                    self.label_personaje.setPixmap(pixeles)
                    self.label_personaje.setScaledContents(True)
                    self.label_personaje.move(x-p.VELOCIDAD_HOMERO,y)
                    self.verificar_interseccion()
                
            elif event.key() == QtCore.Qt.Key_D:
                if self.verificar_restriccion_obstaculo("D") == False:
                    ruta_foto = os.path.join("sprites","Personajes","Homero","right_3.png")
                    pixeles = QPixmap(ruta_foto)
                    self.label_personaje.setPixmap(pixeles)
                    self.label_personaje.setScaledContents(True)
                    self.label_personaje.move(x+p.VELOCIDAD_HOMERO,y)
                    self.verificar_interseccion()
                
        if self.personaje == "Lisa":
        
            if event.key() == QtCore.Qt.Key_W:
                
                if self.verificar_restriccion_obstaculo("W") == False:
                    ruta_foto = os.path.join("sprites","Personajes","Lisa","up_2.png")
                    pixeles = QPixmap(ruta_foto)
                    self.label_personaje.setPixmap(pixeles)
                    self.label_personaje.setScaledContents(True)
                    self.label_personaje.move(x,y-p.VELOCIDAD_LISA)
                    self.verificar_interseccion()
                
            elif event.key() == QtCore.Qt.Key_S:
                if self.verificar_restriccion_obstaculo("S") == False:
                    ruta_foto = os.path.join("sprites","Personajes","Lisa","down_2.png")
                    pixeles = QPixmap(ruta_foto)
                    self.label_personaje.setPixmap(pixeles)
                    self.label_personaje.setScaledContents(True)
                    self.label_personaje.move(x,y+p.VELOCIDAD_LISA)
                    self.verificar_interseccion()
                
            elif event.key() == QtCore.Qt.Key_A:
                
                if self.verificar_restriccion_obstaculo("A") == False:
                    
                    ruta_foto = os.path.join("sprites","Personajes","Lisa","left_1.png")
                    pixeles = QPixmap(ruta_foto)
                    self.label_personaje.setPixmap(pixeles)
                    self.label_personaje.setScaledContents(True)
                    self.label_personaje.move(x-p.VELOCIDAD_LISA,y)               
                    self.verificar_interseccion()
                
            elif event.key() == QtCore.Qt.Key_D:
                
                if self.verificar_restriccion_obstaculo("D") == False:
                    
                    ruta_foto = os.path.join("sprites","Personajes","Lisa","right_2.png")
                    pixeles = QPixmap(ruta_foto)
                    self.label_personaje.setPixmap(pixeles)
                    self.label_personaje.setScaledContents(True)
                    self.label_personaje.move(x+p.VELOCIDAD_LISA,y)
                    self.verificar_interseccion()
                
    def verificar_interseccion(self):
        
        personaje = self.label_personaje.geometry()
        objeto = self.label_objeto1.geometry()
        objetoX2 = self.label_objeto2.geometry()

        if personaje.intersects(objeto) == True and self.activo == True:
            self.label_objeto1.hide()
            
            if self.objeto == "Dona" or self.objeto == "Saxofon":
                self.ob_buenos += p.PUNTOS_OBJETO_NORMAL
                self.activo = False
                self.objetos_buenos()
            
            if self.objeto == "Veneno":
                self.ob_malos += 1
                self.ob_malos_total += 1
                self.activo = False
                self.objetos_malos()
                self.vida -= p.PONDERADOR_VENENO
                self.barrita_vida()
                if self.vida <= 0:
                    self.mostrar_postronda()
            
            if self.objeto == "Corazon":
                if self.vida < 10:
                    self.vida += p.PONDERADOR_CORAZON
                    self.barrita_vida()
                self.activo = False
        
        if personaje.intersects(objetoX2) == True and self.activo2 == True:
            
            self.label_objeto2.hide()
            self.obx2 += 2
            self.ob_buenos += 1
            self.ob_buenos_total += 1
            self.objetos_buenos()
            self.activo2 = False

    def salir(self):
        
        self.hide()
        
    def mostrar_postronda(self):
        
        self.hide()
        self.senal_salir_post.emit()
        self.senal_mandar_resultados.emit(self.ob_buenos, self.obx2, self.vida)
        self.senal_enviar_ob_buenos.emit(self.ob_buenos)
        self.senal_enviar_ob_malos.emit(self.ob_malos)
        self.ronda += 1
        self.actualizar_ronda()
        self.senal_enviar_vida.emit(self.vida)
        self.senal_enviar_items.emit(self.ob_buenos_total, self.ob_malos_total)
         
    def mostrar_obstaculos(self):
        
        personaje = self.label_personaje.geometry()
        
        if self.personaje == "Homero":
            
            self.label_ob1.move(random.randint(10,700),random.randint(260,470))
            self.label_ob2.move(random.randint(10,700),random.randint(260,470))
            self.label_ob3.move(random.randint(10,700),random.randint(260,470))
        
            ob1 = self.label_ob1.geometry()
            ob2 = self.label_ob2.geometry()
            ob3 = self.label_ob3.geometry()
            
            intersectan = True
            while intersectan == True:
                if ob1.intersects(ob2) == False and ob1.intersects(ob3) == False and ob2.intersects\
                    (ob3) == False and personaje.intersects(ob1) == False and personaje.intersects(\
                        ob2) == False and personaje.intersects(ob3) == False:
                    intersectan = False
                else:
                    intersectan = True
                    self.label_ob1.move(random.randint(10,700),random.randint(260,470))
                    self.label_ob2.move(random.randint(10,700),random.randint(260,470))
                    self.label_ob3.move(random.randint(10,700),random.randint(260,470))
                    
        if self.personaje == "Lisa":
            
            ruta_foto1 = os.path.join("sprites","Mapa","Primaria","Obstaculo1.png")
            ruta_foto2 = os.path.join("sprites","Mapa","Primaria","Obstaculo2.png")
            ruta_foto3 = os.path.join("sprites","Mapa","Primaria","Obstaculo3.png")
            pixeles1 = QPixmap(ruta_foto1)
            pixeles2 = QPixmap(ruta_foto2)
            pixeles3 = QPixmap(ruta_foto3)
            self.label_ob1.setPixmap(pixeles1)
            self.label_ob2.setPixmap(pixeles2)
            self.label_ob3.setPixmap(pixeles3)
            self.label_ob1.move(random.randint(10,700),random.randint(260,470))
            self.label_ob2.move(random.randint(10,700),random.randint(260,470))
            self.label_ob3.move(random.randint(10,700),random.randint(260,470))
            
            ob1 = self.label_ob1.geometry()
            ob2 = self.label_ob2.geometry()
            ob3 = self.label_ob3.geometry()
            
            intersectan = True
            while intersectan == True:
                if ob1.intersects(ob2) == False and ob1.intersects(ob3) == False and ob2.intersects\
                    (ob3) == False and personaje.intersects(ob1) == False and personaje.intersects\
                        (ob2) == False and personaje.intersects(ob3) == False:
                    intersectan = False
                else:
                    intersectan = True
                    self.label_ob1.move(random.randint(10,700),random.randint(260,470))
                    self.label_ob2.move(random.randint(10,700),random.randint(260,470))
                    self.label_ob3.move(random.randint(10,700),random.randint(260,470))
                   
        pass
    
    def temporizador(self, dificultad):
        
        if self.thread is None or not self.thread.isRunning():
            self.thread = ThreadTiempo(self.senal_thread,self.senal_salir,dificultad)
            self.thread.start()

    def actualizar_labels(self, evento):

        self.label_tiempo.setText(f"{evento}")
    
    def generar_objetos(self, dificultad):
        
        if self.thread_objeto is None or not self.thread_objeto.isRunning():
            self.thread_objeto = ThreadObjeto(self.senal_generar_objeto,self.senal_generar_objetox2\
                , dificultad)
            self.thread_objeto.start()
                
    def generador_objetos(self):
        
        self.activo = True
        self.label_objeto1.show()
        
        if self.personaje == "Homero":
        
            numero = random.random()
        
            if numero < p.PROB_NORMAL:
                ruta_foto = os.path.join("sprites","Objetos","Dona.png")
                pixeles = QPixmap(ruta_foto)
                self.label_objeto1.setPixmap(pixeles)
                self.label_objeto1.move(random.randint(10,700),random.randint(260,470))
                self.objeto = "Dona"
            
            if p.PROB_NORMAL < numero and numero < p.PROB_NORMAL + p.PROB_BUENO:
                ruta_foto = os.path.join("sprites","Objetos","Corazon.png")
                pixeles = QPixmap(ruta_foto)
                self.label_objeto1.setPixmap(pixeles)
                self.label_objeto1.move(random.randint(10,700),random.randint(260,470))
                self.objeto = "Corazon"
                
            if p.PROB_NORMAL + p.PROB_BUENO < numero and numero < p.PROB_NORMAL + p.PROB_BUENO\
                + p.PROB_VENENO:
                ruta_foto = os.path.join("sprites","Objetos","Veneno.png")
                pixeles = QPixmap(ruta_foto)
                self.label_objeto1.setPixmap(pixeles)
                self.label_objeto1.move(random.randint(10,700),random.randint(260,470))
                self.objeto = "Veneno"
        
        if self.personaje == "Lisa":
        
            numero = random.random()
        
            if numero < p.PROB_NORMAL:
                ruta_foto = os.path.join("sprites","Objetos","Saxofon.png")
                pixeles = QPixmap(ruta_foto)
                self.label_objeto1.setPixmap(pixeles)
                self.label_objeto1.move(random.randint(10,700),random.randint(260,470))
                self.objeto = "Saxofon"
            if p.PROB_NORMAL < numero and numero < p.PROB_NORMAL + p.PROB_BUENO:
                ruta_foto = os.path.join("sprites","Objetos","Corazon.png")
                pixeles = QPixmap(ruta_foto)
                self.label_objeto1.setPixmap(pixeles)
                self.label_objeto1.move(random.randint(10,700),random.randint(260,470))
                self.objeto = "Corazon"
            if p.PROB_NORMAL + p.PROB_BUENO < numero and numero < p.PROB_NORMAL + p.PROB_BUENO\
                + p.PROB_VENENO:
                ruta_foto = os.path.join("sprites","Objetos","Veneno.png")
                pixeles = QPixmap(ruta_foto)
                self.label_objeto1.setPixmap(pixeles)
                self.label_objeto1.move(random.randint(10,700),random.randint(260,470))  
                self.objeto = "Veneno"          
            
    def objetos_buenos(self):
        self.label_objetos_buenos.setText(f"ITEMS BUENOS: {self.ob_buenos}")            
                
    def objetos_malos(self):
        self.label_objetos_malos.setText(f"ITEMS MALOS: {self.ob_malos}")
                     
    def generador_objetosx2(self):
                
        if self.personaje == "Homero":
            ruta_foto = os.path.join("sprites","Objetos","DonaX2.png")
            pixeles = QPixmap(ruta_foto)
            self.label_objeto2.setPixmap(pixeles)
            self.label_objeto2.move(random.randint(10,700),random.randint(260,470))
         
        if self.personaje == "Lisa":
            ruta_foto = os.path.join("sprites","Objetos","SaxofonX2.png")
            pixeles = QPixmap(ruta_foto)
            self.label_objeto2.setPixmap(pixeles)
            self.label_objeto2.move(random.randint(10,700),random.randint(260,470))    
      
    def barrita_vida(self):
        
        self.barra_vida.setValue(self.vida)
        self.senal_enviar_vida.emit(self.vida)
        
    def actualizar_puntaje(self,puntaje):
        
        self.puntaje = puntaje
        self.puntaje_total += puntaje 
        self.label_puntaje.setText(f"PUNTAJE: {puntaje}")
        self.senal_enviar_puntaje.emit(self.puntaje_total)
        
    def actualizar_ronda(self):
        
        self.label_ronda.setText(f"RONDA: {self.ronda}")
        self.senal_actualizar_ronda.emit(self.ronda)
    
    def verificar_restriccion_obstaculo(self, tecla):
    
        x = self.label_personaje.x()
        y = self.label_personaje.y()
        width = self.label_personaje.width()
        height = self.label_personaje.height()
        self.label = QLabel()
        self.label.setGeometry(x,y,width,height)
    
        obstaculo1 = self.label_ob1.geometry()
        obstaculo2 = self.label_ob2.geometry()
        obstaculo3 = self.label_ob3.geometry()
        
        if self.personaje == "Homero":
            if tecla == "A":
                self.label.move(x-p.VELOCIDAD_HOMERO,y)
                label = self.label.geometry()
                if label.intersects(obstaculo1) or label.intersects(obstaculo2) or label.intersects\
                    (obstaculo3):
                    return True
                else:
                    return False
                
            if tecla == "D":
                
                self.label.move(x+p.VELOCIDAD_HOMERO,y)
                label = self.label.geometry()
                if label.intersects(obstaculo1) or label.intersects(obstaculo2) or label.intersects\
                    (obstaculo3):
                    return True
                else:
                    return False
            if tecla == "S":
                self.label.move(x,y+p.VELOCIDAD_HOMERO)
                label = self.label.geometry()
                if label.intersects(obstaculo1) or label.intersects(obstaculo2) or label.intersects\
                    (obstaculo3):
                    return True
                else:
                    return False       
            if tecla == "W":
                self.label.move(x,y-p.VELOCIDAD_HOMERO)
                label = self.label.geometry()
                if label.intersects(obstaculo1) or label.intersects(obstaculo2) or label.intersects\
                    (obstaculo3):
                    return True
                else:
                    return False
        
        else:
            if tecla == "A":
                self.label.move(x-p.VELOCIDAD_LISA,y)
                label = self.label.geometry()
                if label.intersects(obstaculo1) or label.intersects(obstaculo2) or label.intersects\
                    (obstaculo3):
                    return True
                else:
                    return False
                
            if tecla == "D":
                
                self.label.move(x+p.VELOCIDAD_LISA,y)
                label = self.label.geometry()
                if label.intersects(obstaculo1) or label.intersects(obstaculo2) or label.intersects\
                    (obstaculo3):
                    return True
                else:
                    return False
            if tecla == "S":
                self.label.move(x,y+p.VELOCIDAD_LISA)
                label = self.label.geometry()
                if label.intersects(obstaculo1) or label.intersects(obstaculo2) or label.intersects\
                    (obstaculo3):
                    return True
                else:
                    return False       
            if tecla == "W":
                self.label.move(x,y-p.VELOCIDAD_LISA)
                label = self.label.geometry()
                if label.intersects(obstaculo1) or label.intersects(obstaculo2) or label.intersects\
                    (obstaculo3):
                    return True
                else:
                    return False
            
    
           
        