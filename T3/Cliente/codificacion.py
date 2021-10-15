import sys
import json
import os
"""
Modulo para funciones de codificacion y decodificacion para envio de mensajes.
Recuerda, no debes modificar los argumentos que recibe cada funcion,
y debes entregar exactamente lo que esta pide en el enunciado.
"""


# Codificar un mensaje a un bytearray segun el protocolo especificado.
def codificar_mensaje(mensaje):
    # COMPLETAR ESTA FUNCION
    muchos_bytes = json.dumps(mensaje).encode("utf-8")
    tipo = (2).to_bytes(4, byteorder = "little")
    primeros_4 = (len(muchos_bytes)).to_bytes(4, byteorder = "big")

    TAMANO_CHUNK = 60
    mensaje_final = bytearray()
    mensaje_final.extend(primeros_4)
    mensaje_final.extend(tipo)
    contador = 0
    for i in range(0, len(muchos_bytes), TAMANO_CHUNK):
        chunk = (muchos_bytes[i:i+TAMANO_CHUNK])
        bloque_contador = (contador).to_bytes(4, byteorder= "little")
        mensaje_final.extend(bloque_contador)
        contador += 1
        mensaje_final.extend(chunk)
    
    if len(mensaje_final) > 60:
        bytes_restantes = (contador+1)*60 - len(mensaje_final)
    else:
        bytes_restantes = 60 - len(mensaje_final)
    
    mensaje_final.extend(bytearray(bytes_restantes))
    
   
    
    return mensaje_final
    pass


# Decodificar un bytearray para obtener el mensaje original.
def decodificar_mensaje(mensaje):
    # COMPLETAR ESTA FUNCION
  
    msj = bytearray
    
    TAMANO_CHUNK = 60
    contador = 0
    inicio = 12
    largo = mensaje[0:4]
    largo_decodificado = int.from_bytes(largo, byteorder='big')
    tipo = mensaje[4:8]
    tipo_decodificado = int.from_bytes(tipo, byteorder='little')
    if largo_decodificado < 60:
        msj = mensaje[12:12+largo_decodificado]

    
    return msj
            
            
    pass


# Codificar una imagen a un bytearray segun el protocolo especificado.
def codificar_imagen(ruta):
    # COMPLETAR ESTA FUNCION
    codigo = None
    if ruta == os.path.join("Cliente", "sprites", "Avatares","avatar-1.png"):
        codigo = 1
    elif ruta == os.path.join("Cliente", "sprites", "Avatares","avatar-2.png"):
        codigo = 2
    elif ruta == os.path.join("Cliente", "sprites", "Avatares","avatar-3.png"):
        codigo = 3
    elif ruta == os.path.join("Cliente", "sprites", "Avatares","avatar-4.png"):
        codigo = 4
        
    muchos_bytes = json.dumps(ruta).encode("utf-8")
    tipo = (1).to_bytes(4, byteorder = "little")
    largo = (len(muchos_bytes)).to_bytes(4, byteorder = "big")
    codigo_codificado = (codigo).to_bytes(4, byteorder= "big")
    TAMANO_CHUNK = 100
    mensaje_final = bytearray()
    mensaje_final.extend(largo)
    mensaje_final.extend(tipo)
    mensaje_final.extend(codigo_codificado)
    contador = 0
    for i in range(0, len(muchos_bytes), TAMANO_CHUNK):
        chunk = (muchos_bytes[i:i+TAMANO_CHUNK])
        bloque_contador = (contador).to_bytes(4, byteorder= "little")
        mensaje_final.extend(bloque_contador)
        contador += 1
        mensaje_final.extend(chunk)
    
    if len(mensaje_final) > 100:
        bytes_restantes = (contador+1)*100 - len(mensaje_final)
    else:
        bytes_restantes = 100 - len(mensaje_final)
    
    
    mensaje_final.extend(bytearray(bytes_restantes))
    return mensaje_final
    pass


# Decodificar un bytearray a una lista segun el protocolo especificado.
def decodificar_imagen(mensaje):
    # COMPLETAR ESTA FUNCION
    pass

if __name__ == "__main__":
  
    mensaje = codificar_mensaje({"usuario": "mathias"})
    print(decodificar_mensaje(mensaje))