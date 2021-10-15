from archivos import diccionario_contactos,diccionario_grupos,lista_usuarios,lista_grupos,diccionario_mensajes,lista_mensajes
from datetime import datetime
#esta función se usa para crear el usuario
def crear_usuario(x):
    if len(x)<=3:
        return False
    if len(x)>=15:
        return False
    if x.count(",")>=1:
        return False
    return True
#esta función es para modificar un archivo csv
def modificar_csv(archivo, input):
    with open(archivo , "a") as f:
        f.write("\n"+input)
    
#con esta función desplegamos los contactos
def desplegar_contactos(usuario):
    x = diccionario_contactos.get(usuario)
    return x
#con esta función desplegamos los grupos
def desplegar_grupos(usuario):
    x = diccionario_grupos.get(usuario)
    return x
#con esta función añadimos un usuario
def añadir_contacto(usuario,nuevo_usuario):
    if diccionario_contactos.get(usuario) == None:
        diccionario_contactos[usuario] = []

    contactos = diccionario_contactos.get(usuario)
    if nuevo_usuario not in lista_usuarios:
        print("El usuario ingresado no existe")
        return False
    if nuevo_usuario not in contactos:
        modificar_csv("contactos.csv", f"{usuario},{nuevo_usuario}")
        modificar_csv("contactos.csv", f"{nuevo_usuario},{usuario}")
        actualizar_contactos(usuario,nuevo_usuario)
        return True

#con esta función actualizamos el dicccionario y la lista de contactos
def actualizar_contactos(usuario,nuevo_usuario):
    lista_contactos = []
    with open("contactos.csv") as f:
        f.readline()
        lineas = f.readlines()
        for x in lineas:
            lista_contactos.append(x.rstrip("\n").rsplit(","))    
    if nuevo_usuario not in diccionario_contactos.get(usuario):
        diccionario_contactos[usuario].append(nuevo_usuario)
    if diccionario_contactos.get(nuevo_usuario) == None:
        diccionario_contactos[nuevo_usuario] = []
    if usuario not in diccionario_contactos.get(nuevo_usuario):
        diccionario_contactos[nuevo_usuario].append(usuario)

#con esta función creamos un grupo
def crear_grupo(nombre_grupo,usuario,nuevos_usuarios):
    lista_grupo = nuevos_usuarios.split(";")
    lista_grupo.append(usuario)
    for i in lista_grupos:
        if nombre_grupo == i[0]:
            print()
            print("Este grupo ya existe, intenta con otro nombre")
            return False
    if len(nombre_grupo)<=1:
        print()
        print("El nombre del grupo es demasiado corto")
        print()
        return False
    if nombre_grupo.count(",")>=1:
        print()
        print("El nombre del grupo no puede tener comas")
        return False
    if len(lista_grupo)<=2:
        print()
        print("Tiene que ingresar mas de 1 usuarios")
        return False
    for x in lista_grupo:
        if x not in lista_usuarios:
            print()
            print(f"el usuario {x} no existe")
            return False
    for a in lista_grupo:
        modificar_csv("grupos.csv",f"{nombre_grupo},{a}")
        actualizar_grupos()
    return True

#con esta función actualizamos la lista y el diccionario de grupos
def actualizar_grupos():
    lista_grupos = []
    with open("grupos.csv") as f:
        f.readline()
        lineas = f.readlines()
        for x in lineas:
            lista_grupos.append(x.rstrip("\n").rsplit(","))    
    for x in lista_grupos:
        if x[1] not in diccionario_grupos.keys():
            diccionario_grupos[x[1]] = []
        if x[0] not in diccionario_grupos.get(x[1]):
            diccionario_grupos[x[1]].append(x[0])

#con esta funciñon actualizamos la lista de usuario
def actualizar_usuarios():
    with open("usuarios.csv") as archivo:
        archivo.readline()
        lineas = archivo.readlines()
        for x in lineas:
                lista_usuarios.append(x.rstrip("\n"))

#esta función es para usarla como key en el sort para ordenar los mensajes por fecha.
def fechas(x):
    a = x[3]
    return a 

#con esta función desplegamos los mensajes de los chats regulares
def desplegar_mensajes_regular(usuario,segundo_usuario):
    mensajes1 = diccionario_mensajes.get(usuario)
    mensajes2 = diccionario_mensajes.get(segundo_usuario)
    mensajes2_final = []
    mensajes1_final = []
    if mensajes1 == None:
        mensajes1 = []
    for x in mensajes1:
        if x[2] == segundo_usuario:
            mensajes1_final.append(x)
    if mensajes2 == None:
        mensajes2 = []
    for i in mensajes2:
        if i[2] == usuario:
            mensajes2_final.append(i)
    lf = mensajes1_final+mensajes2_final
    lf.sort(key = fechas )
    for a in lf:
        if a[1] == usuario:
            print(f"{a[3]}, {usuario}: {a[4]}")
        else:
            print(f"{a[3]}, {segundo_usuario}: {a[4]}")

#con esta función escribimos el mensaje en el archivo csv
def escribir_mensaje(input, usuario, segundo_usuario):
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    with open("mensajes.csv" , "a") as f:
        f.write("\n"+f"regular,{usuario},{segundo_usuario},{dt_string},{input}")

#con esta función actualizamos el diccionario de mensajes
def actualizar_mensajes():
    lista_mensajes = []
    with open("mensajes.csv") as f:
        f.readline()
        lineas = f.readlines()
        for x in lineas:
            lista_mensajes.append(x.rstrip("\n").split(",",4))

        for a in lista_mensajes:
            if diccionario_mensajes.get(a[1]) == None:
                diccionario_mensajes[a[1]] = [[a[0],a[1],a[2],a[3],a[4]]]
            if a not in diccionario_mensajes.get(a[1]):
                diccionario_mensajes[a[1]].extend([[a[0],a[1],a[2],a[3],a[4]]])

#con esta función actualizamos la lista de mensajes
def actualizar_lista_mensajes():
    lista_mensajes = []
    with open("mensajes.csv") as f:
        f.readline()
        lineas = f.readlines()
        for x in lineas:
            lista_mensajes.append(x.rstrip("\n").split(",",4))
    return lista_mensajes

#con esta función desplegamos los mensajes de grupo
def desplegar_mensajes_grupo(grupo):
    lista_mensajes = actualizar_lista_mensajes()
    lista_final = []
    for x in lista_mensajes:
        if x[2] == grupo:
            lista_final.append(x)
    lista_final.sort(key = fechas)
    for i in lista_final:
        print(f"{i[3]}, {i[1]}: {i[4]}")

#con esta función escribimos los mensajes de grupo en el archivo csv
def escribir_mensaje_grupo(input,usuario,grupo):
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    with open("mensajes.csv" , "a") as f:
        f.write("\n"+f"grupo,{usuario},{grupo},{dt_string},{input}")
