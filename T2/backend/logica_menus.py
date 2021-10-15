from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5 import QtMultimedia

class LogicaInicio(QObject):
    
    senal_respuesta_validacion = pyqtSignal(bool)
    senal_enviar_puntaje = pyqtSignal(int)
    senal_enviar_usuario = pyqtSignal(str)
    
    def __init__(self):
        
        super().__init__()
        
        
    def validar_nombre(self,nombre):
      
        if nombre.isalnum() == True:

            self.senal_respuesta_validacion.emit(True)
            self.senal_enviar_usuario.emit(nombre)
        else:
            self.senal_respuesta_validacion.emit(False)
    
    def calculo_puntaje(self,buenos,x2,vida):
        
        if vida > 0:
        
            puntaje = ((buenos + x2)*(vida/10))*100
            self.senal_enviar_puntaje.emit(puntaje)
        else:
            vida1 = -vida
            puntaje = ((buenos + x2)*(vida1/10))*100
            self.senal_enviar_puntaje.emit(puntaje)
            
            

    def escribir_archivo(self,nombre,puntaje):
        
        with open("ranking.txt", "a") as archivo:
            archivo.write(f"\n{nombre},{puntaje}")
              
        
            
    