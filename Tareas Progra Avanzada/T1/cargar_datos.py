from clases import Barco_pasajeros, Barco_carguero, Barco_buque, DCCapitan, DCCarguero, DCCocinero, Mercancia
#------------------------------------------------------------------------------------------------------------------------
barcos = {}
tripulantes = {} 
mercancias = {}
#------------------------------------------------------------------------------------------------------------------------
def cargar_barcos(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
        next(archivo)
        lineas = archivo.readlines()

        lista_barcos = []
        for linea in lineas:
            nombre, tipo, costo_mantención, velocidad_base, pasajeros, carga_maxima, \
                moneda_origen, tripulacion, mercancia = linea.split(",")
            tripulacion = tripulacion.split(";")
            mercancia = mercancia.rstrip("\n").split(";")
            lista = [nombre, tipo, int(costo_mantención), int(velocidad_base), int(pasajeros), int(carga_maxima), \
                moneda_origen, tripulacion, mercancia]
            lista_barcos.append(lista)
            
            
    return lista_barcos
#------------------------------------------------------------------------------------------------------------------------
lista_barcos = cargar_barcos("barcos.csv")
for barco in lista_barcos:
    if barco[1]=="Pasajero":
        barcos[barco[0]] = Barco_pasajeros(barco[0], barco[1], barco[2], barco[3], barco[4], barco[5], barco[6], barco[7], barco[8])
    if barco[1]=="Carguero":
        barcos[barco[0]] = Barco_carguero(barco[0], barco[1], barco[2], barco[3], barco[4], barco[5], barco[6], barco[7], barco[8])
    if barco[1]=="Buque":
        barcos[barco[0]] = Barco_buque(barco[0], barco[1], barco[2], barco[3], barco[4], barco[5], barco[6], barco[7], barco[8])
#------------------------------------------------------------------------------------------------------------------------
def cargar_tripulantes(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
        next(archivo)
        lineas = archivo.readlines()    

        lista_tripulantes = []
        for linea in lineas:
            nombre, tipo, años_experiencia = linea.split(",")
            lista = [nombre, tipo, años_experiencia]
            lista_tripulantes.append(lista)

    return lista_tripulantes
#------------------------------------------------------------------------------------------------------------------------
lista_tripulantes = cargar_tripulantes("tripulantes.csv")
for tripulante in lista_tripulantes:
    if tripulante[1] == "DCCapitán":
        tripulantes[tripulante[0]] = DCCapitan(tripulante[0], tripulante[1], tripulante[2]) 
    if tripulante[1] == "DCCocinero":
        tripulantes[tripulante[0]] = DCCocinero(tripulante[0], tripulante[1], tripulante[2])     
    if tripulante[1] == "DCCarguero":
        tripulantes[tripulante[0]] = DCCarguero(tripulante[0], tripulante[1], tripulante[2])         
#------------------------------------------------------------------------------------------------------------------------
def cargar_mercancia(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as archivo:
        next(archivo)
        lineas = archivo.readlines()    

        lista_mercancias = []
        for linea in lineas:
            numero, tipo, tiempo_exp, peso = linea.rstrip("\n").split(",")
            tiempo_exp = int(tiempo_exp)
            lista = [numero, tipo, tiempo_exp, peso]
            lista_mercancias.append(lista)

    return lista_mercancias
#------------------------------------------------------------------------------------------------------------------------
lista_mercancias = cargar_mercancia("mercancia.csv")
for mercancia in lista_mercancias:
    mercancias[mercancia[0]] = Mercancia(mercancia[0], mercancia[1], mercancia[2], mercancia[3])