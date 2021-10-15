#En este archivo python abrí todos los archivos para crear diccionarios y listas para armar mi programa
lista_usuarios = []
with open("usuarios.csv") as archivo:
    archivo.readline()
    lineas = archivo.readlines()
    for x in lineas:
            lista_usuarios.append(x.rstrip("\n"))
#---------------------------------------------------
diccionario_contactos = {}
lista_contactos = []
with open("contactos.csv") as f:
    f.readline()
    lineas = f.readlines()
    for x in lineas:
        lista_contactos.append(x.rstrip("\n").rsplit(","))    
for x in lista_contactos:
    if x[0] not in diccionario_contactos.keys():
        diccionario_contactos[x[0]] = []
    diccionario_contactos[x[0]].append(x[1])
#---------------------------------------------------
diccionario_grupos = {}
lista_grupos = []
with open("grupos.csv") as f:
    f.readline()
    lineas = f.readlines()
    for x in lineas:
        lista_grupos.append(x.rstrip("\n").rsplit(","))    
for x in lista_grupos:
    if x[1] not in diccionario_grupos.keys():
        diccionario_grupos[x[1]] = []
    diccionario_grupos[x[1]].append(x[0])
#---------------------------------------------------
diccionario_mensajes = {}
lista_mensajes = []
with open("mensajes.csv") as f:
    f.readline()
    lineas = f.readlines()
    for x in lineas:
        if lineas.count(",") <= 4:
            lista_mensajes.append(x.rstrip("\n").split(",",4))

    for a in lista_mensajes:
        if diccionario_mensajes.get(a[1]) == None:
            diccionario_mensajes[a[1]] = [[a[0],a[1],a[2],a[3],a[4]]]
        else:
            diccionario_mensajes[a[1]].extend([[a[0],a[1],a[2],a[3],a[4]]])
