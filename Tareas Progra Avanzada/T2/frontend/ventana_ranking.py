import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import (QObject, pyqtSignal)
import operator


"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

window_name, base_class = uic.loadUiType("ventana_ranking.ui")


class VentanaRanking(window_name, base_class):
    
    senal_volver = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Ventana Ranking")
        
        self.boton_volver_ranking.clicked.connect(self.volver)
        
    def abrir_ventana(self):
        
        self.mostrar_ranking()
        self.show()
    
    def volver(self):
        
        self.hide()
        self.senal_volver.emit()
    
    def mostrar_ranking(self):
        lista_puntajes = []
        dic_puntajes = {}
        with open("ranking.txt") as f:
            lineas = f.readlines()
            for linea in lineas:
                lista_puntajes.append(linea.rstrip("\n").split(","))
        
        for x in lista_puntajes:
            dic_puntajes[x[0]] = x[1]
            
        dic_ordenado = sorted(dic_puntajes.items(), key=operator.itemgetter(1), reverse= True)
            
        self.label_primero.setText(f"Jugador: {dic_ordenado[0][0]}     Puntaje : {dic_ordenado[0][1]}")
        self.label_segundo.setText(f"Jugador: {dic_ordenado[1][0]}     Puntaje : {dic_ordenado[1][1]}")
        self.label_tercero.setText(f"Jugador: {dic_ordenado[2][0]}     Puntaje : {dic_ordenado[2][1]}")
        self.label_cuarto.setText(f"Jugador: {dic_ordenado[3][0]}     Puntaje : {dic_ordenado[3][1]}")
        self.label_quinto.setText(f"Jugador: {dic_ordenado[4][0]}     Puntaje : {dic_ordenado[4][1]}")
                
