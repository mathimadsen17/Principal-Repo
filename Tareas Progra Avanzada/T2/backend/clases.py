from PyQt5.QtCore import (QObject, pyqtSignal, QRect, QThread, QTimer)
from time import sleep
import backend.parametros as p

class ThreadTiempo(QThread):
   
 
    def __init__(self, senal_actualizar,senal_salir,dificultad):
        super().__init__()
        self.senal_actualizar = senal_actualizar
        self.dificultad = dificultad
        self.senal_salir = senal_salir
        

    def run(self):
        if self.dificultad == "Intro":
            counter = 1
            for i in range(p.DURACION_INTRO):
                sleep(1)
                self.senal_actualizar.emit(str(i)) 
                    
        else:
            for i in range(p.DURACION_AVANZADA):
                sleep(1)
                self.senal_actualizar.emit(str(i))
        
            
        sleep(1)
        self.senal_actualizar.emit("FIN")
        self.senal_salir.emit()

class ThreadObjeto(QThread):
    
    def __init__(self, senal_objetos, senal_objetosx2, dificultad):
        super().__init__()
        self.senal = senal_objetos
        self.dificultad = dificultad
        self.senalx2 = senal_objetosx2
        
    def run(self):
        if self.dificultad == "Intro":
            for i in range(100):
                self.senal.emit()
                sleep(p.APARICION_INTRO)
                if i == 2:
                    self.senalx2.emit()
                if i == 5:
                    self.senalx2.emit()
                
        if self.dificultad == "Avanzada":
            for i in range(100):
                self.senal.emit()
                sleep(p.APARICION_AVANZADA)
                if i == 2:
                    self.senalx2.emit()
                elif i==5:
                    self.senalx2.emit()
                    
                    
    pass