from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_preparacion import VentanaPreparacion
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post import VentanaPost
from backend.logica_menus import LogicaInicio
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import (QObject, pyqtSignal)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ventana_inicio = VentanaInicio()
    logica_inicio = LogicaInicio()
    
    ventana_inicio.senal_enviar_nombre.connect(logica_inicio.validar_nombre)
    
    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion) 
    

    ventana_inicio.show()

    ventana_ranking = VentanaRanking()
    ventana_preparacion = VentanaPreparacion()
    ventana_juego = VentanaJuego()
    ventana_post = VentanaPost()
    
    ventana_inicio.senal_abrir_ranking.connect(ventana_ranking.abrir_ventana)
    
    ventana_ranking.senal_volver.connect(ventana_inicio.abrir_ventana_inicio)

    ventana_inicio.senal_abrir_preparacion.connect(ventana_preparacion.abrir_ventana_preparacion)    
    
    ventana_preparacion.senal_abrir_ventana_juego.connect(ventana_juego.abrir_ventana)
    
    ventana_juego.senal_salir_post.connect(ventana_post.abrir_ventana)
    
    ventana_juego.senal_mandar_resultados.connect(logica_inicio.calculo_puntaje) 

    logica_inicio.senal_enviar_puntaje.connect(ventana_juego.actualizar_puntaje)

    logica_inicio.senal_enviar_puntaje.connect(ventana_post.actualizar_puntaje)
    
    ventana_post.senal_continuar_jugando.connect(ventana_preparacion.abrir_ventana_preparacion)
    
    ventana_juego.senal_actualizar_ronda.connect(ventana_preparacion.actualizar_ronda)
    
    ventana_juego.senal_enviar_vida.connect(ventana_preparacion.barrita_vida)
    
    ventana_juego.senal_enviar_vida.connect(ventana_post.mostrar_vida)
    
    ventana_juego.senal_enviar_ob_buenos.connect(ventana_post.mostrar_items_buenos)
    
    ventana_juego.senal_enviar_ob_malos.connect(ventana_post.mostrar_items_malos)
    
    ventana_juego.senal_enviar_puntaje.connect(ventana_preparacion.actualizar_puntaje)
    
    logica_inicio.senal_enviar_usuario.connect(ventana_post.recibir_usuario)
    
    ventana_post.senal_enviar_puntaje.connect(logica_inicio.escribir_archivo)
    
    ventana_juego.senal_enviar_items.connect(ventana_preparacion.mostrar_items)
    
    sys.exit(app.exec_())