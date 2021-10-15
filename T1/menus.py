from clases import Canal
import parametros
from acciones import mostrar_estado, mostrar_riesgo, desencallar_barco, simular_hora

canal = None

def menu_inicio():
    print("***** MENU DE INICIO *****")
    print()
    print("[1] Comenzar una nueva simulacion")
    print("[0] Salir del Programa")
    print()
    valida = False
    while valida == False:
        accion = input("Indique su opción (0, 1): ").strip()
        if accion.isnumeric():
            accion = int(accion)
            if accion == 0:
                break
            if accion == 1:
                valida = True
                hola = False
                while hola == False:
                    print()
                    opcion_canal = input("Escoja el canal que desea simular: ")
                    print()
                    if opcion_canal == "Canal de Panamá":
                        canal = Canal("Canal de Panamá", 80, "principiante")
                        canal.cobro_uso = parametros.COBRO_USO_PRINCIPIANTE
                        parametros.DIF_CANAL = parametros.PONDERADOR_PRINCIPIANTE
                        menu_acciones(canal)
                        return canal
                    
                    if opcion_canal == "Canal de Suez":
                        canal = Canal("Canal de Suez", 193, "avanzado")
                        canal.cobro_uso = parametros.COBRO_USO_AVANZADO
                        parametros.DIF_CANAL = parametros.PONDERADOR_AVANZADO
                        menu_acciones(canal)
                    else:
                        valida = False
            else:
                print()
                print("accion no valida, intnte de nuevo")
                print()
        else:
            print()
            print("accion no valida, intente de nuevo")
            print()

def menu_acciones(canal):
    
    valida = False
    while valida == False:
        print("***** MENU DE ACCIONES *****")
        print()
        print("[1] Mostrar riesgo de encallamiento")
        print("[2] Desencallar barco")
        print("[3] Simular hora nueva")
        print("[4] Mostrar estado")
        print("[5] Volver")
        print("[0] Salir del programa") 
        print()
        accion = input("Indique su opción (0, 1): ").strip()
        if accion.isnumeric():
            accion = int(accion)
            if accion == 0:
                break
            if accion == 1:
                mostrar_riesgo(canal)
            if accion == 2:
                desencallar_barco(canal)
            if accion == 3:
                simular_hora(canal)
            if accion == 4:
                mostrar_estado(canal) 
            if accion == 5:
                return menu_inicio()

           
        else:
            print()
            print("accion no valida, intente de nuevo")
            print()