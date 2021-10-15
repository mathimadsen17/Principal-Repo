from abc import ABC,abstractmethod
import parametros
from random import uniform

#------------------------------------------------------------------------------------------------------------------------
lista_tripulantes = []
with open("tripulantes.csv", "rt", encoding="utf-8") as archivo:
    next(archivo)
    lineas = archivo.readlines()    

    
    for linea in lineas:
        nombre, tipo, años_experiencia = linea.split(",")
        lista = [nombre, tipo, años_experiencia]
        lista_tripulantes.append(lista)
#------------------------------------------------------------------------------------------------------------------------
class Canal():

    def __init__(self, nombre, largo, dificultad):
        self.nombre = nombre
        self.largo = largo
        self.dificultad = dificultad
        self.cobro_uso = ()
        self.dinero = parametros.DINERO_INICIAL
        self.barcos = []
        self.barcos_encallados = []
        self.horas_simuladas = int()
        self.barcos_pasaron = int()
        self.barcos_encallaron = int()
        self.dinero_gastado = int()
        self.dinero_recibido = float
        self.eventos_ocurridos = int()
        self.dinero_gastado_hora = float()
        self.dinero_recibido_hora = float()
    def ingresar_barco(self,barco):
        if barco.nombre not in self.barcos:
            self.barcos.append(barco.nombre)
            print()
        pass


    def desencallar_barco(self,barco):
        if self.dinero >= parametros.COSTO_DESENCALLAR:
            self.dinero -= parametros.COSTO_DESENCALLAR
            numero = uniform(0.0,1.0)
            probabilidad_exito = parametros.PROB_BASE_DESENCALLAR*parametros.DIF_CANAL
            if numero < probabilidad_exito:
                self.barcos_encallados.remove(barco.nombre)
                barco.encallado = False
                print(f"Se ha desencallado el barco {barco.nombre} con exito")
                print()
            else:
                print("Hemos fallado al tratar de desencallar el barco")
                print()
        else:
            print("No tienes dinero para desencallar")


        pass

    pass
#------------------------------------------------------------------------------------------------------------------------
class Barcos(ABC):

    def __init__(self, nombre, tipo, costo_mantención, velocidad_base, pasajeros, carga_maxima, \
        moneda_origen, tripulación, mercancia):
        self.nombre = nombre
        self.tipo = tipo
        self.costo_mantención = costo_mantención
        self.velocidad_base = velocidad_base
        self.pasajeros = pasajeros
        self.carga_maxima = carga_maxima
        self.moneda_origen = moneda_origen
        self.probabilidad_encallar = 0
        self.tripulacion = tripulación
        self.tiempo_viaje = 0
        self.mercancia = mercancia
        self.ubicacion = 0
        self.encallado = False
        self.evento_especial = False
        self.tiempo_averia = 0
        self.tiempo_en_canal = 0

    @abstractmethod
    def desplazarse():
        pass
    
    @abstractmethod    
    def encallar():
        pass

    @abstractmethod    
    def ejecutar_evento_especial():
        pass

    pass
#------------------------------------------------------------------------------------------------------------------------
class Barco_pasajeros(Barcos):
    
    def __init__(self, nombre, tipo, costo_mantención, velocidad_base, pasajeros, carga_maxima, moneda_origen, tripulacion, mercancia):
        
        Barcos.__init__(self, nombre, tipo, costo_mantención, velocidad_base, pasajeros, carga_maxima, moneda_origen, tripulacion, mercancia)
        self.probabilidad_encallar = 0
        
        
    def desplazarse(self):
        peso_mercancia = int()
        for paquete in self.mercancia:
            peso_mercancia += int(paquete)
        
        formula = max(0.1, min(1, (self.carga_maxima - peso_mercancia - 0.3*self.pasajeros)/self.carga_maxima))*self.velocidad_base

        self.velocidad = round(formula,1)
        if self.encallado == False:
            self.ubicacion += self.velocidad
        
        pass

    def encallar(self):
        exp_tripulacion = 0
        for tripulante in lista_tripulantes:
            if tripulante[0] in self.tripulacion:
                exp_tripulacion += int(tripulante[2])
        peso_mercancia = int()
        for paquete in self.mercancia:
            peso_mercancia += int(paquete)
        
        formula = min(1, (self.velocidad_base + peso_mercancia - exp_tripulacion)/120) * parametros.TENDENCIA_ENCALLAR_PASAJEROS * parametros.DIF_CANAL
        self.probabilidad_encallar = formula
        numero = uniform(0.0,1.0)
        if numero < self.probabilidad_encallar:
            self.encallado = True
            return True
   
        pass

    def ejecutar_evento_especial(self, canal):
        numero = uniform(0.0,1.0)
        if numero < parametros.PROBABILIDAD_EVENTO_ESPECIAL:
            self.evento_especial = True
            canal.dinero += parametros.DINERO_INTOXICACION
            canal.dinero_recibido += parametros.DINERO_INTOXICACION
            canal.dinero_recibido_hora += parametros.DINERO_INTOXICACION
            canal.eventos_ocurridos += 1
            print(f"Todos los pasajeros del barco {self.nombre} han enfermado, el canal recibe {parametros.DINERO_INTOXICACION} por el costo de los medicamentos")
            return True

        pass

    pass
#------------------------------------------------------------------------------------------------------------------------
class Barco_carguero(Barcos):


    def __init__(self, nombre, tipo, costo_mantención, velocidad_base, pasajeros, carga_maxima, moneda_origen, tripulacion, mercancia):
        Barcos.__init__(self, nombre, tipo, costo_mantención, velocidad_base, pasajeros, carga_maxima, moneda_origen, tripulacion, mercancia)
        self.probabilidad_encallar = 0
        

    def desplazarse(self):
        peso_mercancia = int()
        for paquete in self.mercancia:
            peso_mercancia += int(paquete)
        
        formula = max(0.1, min(1, (self.carga_maxima - peso_mercancia - 0.3*self.pasajeros)/self.carga_maxima))*self.velocidad_base

        self.velocidad = round(formula,1)
        self.tiempo_viaje += 1
        if self.encallado == False:
            self.ubicacion += self.velocidad
        


        pass

    def encallar(self):
        exp_tripulacion = 0
        for tripulante in lista_tripulantes:
            if tripulante[0] in self.tripulacion:
                exp_tripulacion += int(tripulante[2])
        peso_mercancia = int()
        for paquete in self.mercancia:
            peso_mercancia += int(paquete)
        
        formula = min(1, (self.velocidad_base + peso_mercancia - exp_tripulacion)/120) * parametros.TENDENCIA_ENCALLAR_CARGUERO * parametros.DIF_CANAL
        self.probabilidad_encallar = formula
        numero = uniform(0.0,1.0)
        if numero < self.probabilidad_encallar:
            self.encallado = True
            return True

    
        pass

    def ejecutar_evento_especial(self,canal):
        numero = uniform(0.0,1.0)
        if numero < parametros.PROBABILIDAD_EVENTO_ESPECIAL:
            self.evento_especial = True
            canal.eventos_ocurridos += 1
            print(f"El barco {self.nombre} ha sido atacado por piratas!!, lo perdieron todo :(")
            return True

        

        pass


    pass
#------------------------------------------------------------------------------------------------------------------------
class Barco_buque(Barcos):

    def __init__(self, nombre, tipo, costo_mantención, velocidad_base, pasajeros, carga_maxima, moneda_origen, tripulacion, mercancia):
        
        Barcos.__init__(self, nombre, tipo, costo_mantención, velocidad_base, pasajeros, carga_maxima, moneda_origen, tripulacion, mercancia)
        self.probabilidad_encallar = 0
        self.tiempo_averia = 0

    def desplazarse(self):
        peso_mercancia = int()
        for paquete in self.mercancia:
            peso_mercancia += int(paquete)
        
        formula = max(0.1, min(1, (self.carga_maxima - peso_mercancia - 0.3*self.pasajeros)/self.carga_maxima))*self.velocidad_base

        self.velocidad = round(formula,1)
        if self.encallado == False:
            self.ubicacion += self.velocidad


        pass

    def encallar(self):
        exp_tripulacion = 0
        for tripulante in lista_tripulantes:
            if tripulante[0] in self.tripulacion:
                exp_tripulacion += int(tripulante[2])
        peso_mercancia = int()
        for paquete in self.mercancia:
            peso_mercancia += int(paquete)
        
        formula = min(1, (self.velocidad_base + peso_mercancia - exp_tripulacion)/120) * parametros.TENDENCIA_ENCALLAR_BUQUE * parametros.DIF_CANAL
        self.probabilidad_encallar = formula
        numero = uniform(0.0,1.0)
        if numero < self.probabilidad_encallar:
            self.encallado = True
            return True

    
        pass

    def ejecutar_evento_especial(self,canal):
        numero = uniform(0.0,1.0)
        if numero < parametros.PROBABILIDAD_EVENTO_ESPECIAL:
            self.evento_especial = True
            self.tiempo_averia = 0
            canal.eventos_ocurridos += 1
            print(f"El barco {self.nombre} se ha averiado :/")
            return True

        
        
        

        pass


    pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
class Tripulantes(ABC):
    def __init__(self, nombre, tipo, años_experiencia):
        self.nombre = nombre
        self.tipo = tipo
        self.años_experiencia = años_experiencia

    pass
#------------------------------------------------------------------------------------------------------------------------
class DCCapitan(Tripulantes):
    def __init__(self, nombre, tipo , años_experiencia):

        Tripulantes.__init__(self, nombre, tipo, años_experiencia)
        self.desencallar = False
#------------------------------------------------------------------------------------------------------------------------
class DCCocinero(Tripulantes):
    def __init__(self, nombre, tipo , años_experiencia):

        Tripulantes.__init__(self, nombre, tipo, años_experiencia)
        self.cocinar = False
#------------------------------------------------------------------------------------------------------------------------
class DCCarguero(Tripulantes):
    def __init__(self, nombre, tipo , años_experiencia):

        Tripulantes.__init__(self, nombre, tipo, años_experiencia)
        self.evento = False
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
class Mercancia():

    def __init__(self, numero_lote, tipo, tiempo_exp, peso):
        
        self.numero_lote = numero_lote
        self.tipo = tipo
        self.tiempo_exp = tiempo_exp
        self.peso = peso
        self.expiro = False
    
    def expirar(self, canal, barco):
        
        if self.tipo == "petróleo":
            canal.dinero -= parametros.MULTA_PETROLEO
            canal.dinero_gastado += parametros.MULTA_PETROLEO
            canal.dinero_gastado_hora += parametros.MULTA_PETROLEO
            self.expiro = True
            print(f"El paquete {self.numero_lote} del barco {barco.nombre} ha expirado, el canal debe pagarles {parametros.MULTA_PETROLEO}")
        if self.tipo == "ropa":
            canal.dinero -= parametros.MULTA_ROPA
            canal.dinero_gastado += parametros.MULTA_ROPA
            canal.dinero_gastado_hora += parametros.MULTA_ROPA
            self.expiro = True
            print(f"El paquete {self.numero_lote} del barco {barco.nombre} ha expirado, el canal debe pagarles {parametros.MULTA_ROPA}")
        if self.tipo == "alimentos":
            canal.dinero -= parametros.MULTA_ALIMENTOS
            canal.dinero_gastado += parametros.MULTA_ALIMENTOS
            canal.dinero_gastado_hora += parametros.MULTA_ALIMENTOS
            self.expiro = True
            print(f"El paquete {self.numero_lote} del barco {barco.nombre} ha expirado, el canal debe pagarles {parametros.MULTA_ALIMENTOS}")
        pass




    