import funciones
import archivos
import parametros
input_0 = str()
input_chats = str()
input_contactos = str()
input_grupos = str()
usuario = str()
input_mensaje = ()
input_mensaje_grupo = ()
contactos = ()
cerrado = False
menu_inicio = True
menu_chats = False
inicio_sesion = True
menu_contactos = False
menu_grupos = False
ver_contactos = False
ver_grupos = False

while not cerrado:
    #usé booleanos para desplegar los menús 
    if menu_inicio == True :
        print()
        print("**** Menú de Inicio ****")
        print()
        print("Selecciona una opción")
        print()
        print("[1] Crear usuario")
        print("[2] Iniciar sesion")
        print("[0] Salir")
        print()
        opción_valida0 = False
        while opción_valida0 == False:
            input_0 = input("Indique su opción (1 , 2 o 0): ").rstrip()
            if input_0 in ["1","2","0"]:
                opción_valida0 = True
            else:
                print()
                print("Acción no valida, intente nuevamente")
                print()

    #Aca esta el codigo por si es que se crea un nuevo usuario
    if input_0 == "1":
        
            print()
            input_crear_usuario = input("Ingrese su nuevo nombre de usuario de largo entre 3 y 15 c\
                aracteres (No use comas): ")
            #usamos la función que creamos en funciones.py cuyo objetivo es verificar si el usuario \
            # cumple con los requisitos
            if funciones.crear_usuario(input_crear_usuario) == False:
                print()
                print("NOMBRE DE USUARIO NO VALIDO")
                print()
                menu_inicio = True
                input_0 = ()
            #aca nos ponemos en el caso de que ese usuario ya exista
            if input_crear_usuario in archivos.lista_usuarios:
                print()
                print("Ese nombre de usuario ya existe, intenta con otro")
                menu_inicio = True
                input_0 = ()
            #cuando la función nos retorna un true y el usuario no se encuentra registrado, creamos \
            #el usuario
            if funciones.crear_usuario(input_crear_usuario) == True and input_crear_usuario not in\
                archivos.lista_usuarios:
                print()
                print("Se ha creado un nuevo usuario con éxito :)")
                print()
                funciones.modificar_csv("usuarios.csv", input_crear_usuario)
                menu_chats = True
                usuario = input_crear_usuario
                menu_inicio = False
                funciones.actualizar_usuarios()
                input_0 = ()
    #aca se inicia el proceso de iniciar sesión           
    if input_0 == "2":

        print()
        input_inicio_sesion = input("Ingrese su usuario: ")
        print()
        #este if lo que hace es buscar si es que el usuario existe
        if input_inicio_sesion not in archivos.lista_usuarios:
            print("No se ha encontrado usuario con ese nombre")
            print()
            menu_inicio = True
            input_0 = ()
                
        else:
            print("Ha iniciado sesión con exito!")
            print()
            usuario = input_inicio_sesion
            menu_inicio = False
            menu_chats = True
            input_0 = ()
    #aca se cierra el programa
    if input_0 == "0":
        cerrado = True

    #acá se inicia el menu de chats           
    if menu_chats == True:
        print()
        print("**** Menú de Chats ****")
        print()
        print("Selecciona una opción")
        print()
        print("[1] Menu Contactos")
        print("[2] Menu Grupos")
        print("[0] Volver")
        print()
        opción_valida1 = False
        #esto se ve bastante a lo largo del código y es para pedirle un input hasta que ingrese uno\
        # válido
        while not opción_valida1:
            input_chats = input("Indique su opción (1 , 2 o 0): ").rstrip()
            if input_chats in ["1","2","0"]:
                opción_valida1 = True
                menu_chats = False
            else:
                print()
                print("Acción no valida, intente nuevamente")
        #si el input en el menu de chats es 1 nos dirigimos al menú de contactos
        if input_chats == "1":
            menu_contactos = True
        #si el input en el menu de chats es 2 nos dirigimos al menú de grupos
        if input_chats == "2":
            menu_grupos = True
        #si el input en el menu de chats es 1 nos devolvemos al menú de inicio
        if input_chats == "0":
            menu_inicio = True
    #acá se inicia el menu de contactos    
    if menu_contactos == True:
        print()
        print("**** Menú de Contactos ****")
        print()
        print("Selecciona una opción")
        print()
        print("[1] Ver Contactos")
        print("[2] Añadir contacto")
        print("[0] Volver")
        print()
        opción_valida2 = False
        input_contactos = ()
        while not opción_valida2:
            input_contactos = input("Indique su opción (1 , 2 o 0): ").rstrip()
            if input_contactos in ["1","2","0"]:
                opción_valida2 = True
                menu_contactos = False
            else:
                print()
                print("Acción no valida, intente nuevamente")
                print()
        #si el input en el menú de contactos es 1 nos vamos a ver contactos
        if input_contactos == "1": 
            ver_contactos = True
        #si el input en el menu de contactos es 2 iniciamos el proceso para añadir un contacto
        if input_contactos == "2":
            print()
            nuevo_usuario = str(input("Ingrese el usuario que desea añadir a sus contactos: "))
            opción_valida3 = False
            while opción_valida3 == False:
                #usamos una funcíon que verifica el nuevo usuario para ver si puede ser contacto
                if funciones.añadir_contacto(usuario, nuevo_usuario) == True:
                    funciones.actualizar_contactos(usuario, nuevo_usuario)
                    print()
                    print(f"Se ha agregado a {nuevo_usuario} a sus contactos")
                    opción_valida3 = True
                    ver_contactos = False
                    menu_contactos = True
                else:
                    opción_valida3 = True
                    menu_contactos = True
        #si el input del menu de contactos es 0 volvemos al menu de chats
        if input_contactos == "0":
            menu_chats = True
    #aca se inicia la interfaz de ver contactos        
    if ver_contactos == True:
        contactos = funciones.desplegar_contactos(usuario)
        if contactos == None:
            print()
            print("No tienes contactos aun")
            print()
            menu_contactos = True
        else:
            print()
            print("**** Ver Contactos ****")
            print()
            print("Selecciona un usuario para \n ver tus conversaciones,\n o 0 para volver atras")
            print()
            for x in range(len(contactos)):
                print(f"[{x+1}] {contactos[x]}")
            print()
            print("[0] Volver")
            print()
            segundo_usuario = input("Ingrese el usuario: ")
            if segundo_usuario == "0":
                menu_contactos = True
            if segundo_usuario in archivos.diccionario_contactos.get(usuario):
                while True:
                    print()
                    print(f"**** Tu historial con {segundo_usuario} ****")
                    funciones.desplegar_mensajes_regular(usuario,segundo_usuario)
                    print()
                    print(f"**** Fin del historial con {segundo_usuario} ****")
                    input_mensaje = input("escriba un mensaje: ")
                    #si el mensaje escrito es igual a el parametro, volvemos a ver contactos\
                    #de lo contrario, lo escribimos.
                    if input_mensaje == parametros.VOLVER_FRASE:
                        ver_contactos = True
                        break
                        
                    else:    
                        funciones.escribir_mensaje(input_mensaje,usuario,segundo_usuario)
                        funciones.actualizar_mensajes()
            #si en la interfaz de ver contactos se ingresa un 0 volvemos al menu de contactos
            if segundo_usuario == "0":
                menu_contactos = True
                ver_contactos = False
                
    #acá se inicia el menu de grupos       
    if menu_grupos == True:
        print()
        print("**** Menú de Grupos ****")
        print()
        print("Selecciona una opción")
        print()
        print("[1] Ver Grupos")
        print("[2] Crear Grupo")
        print("[0] Volver")
        print()
        opción_valida3 = False
        while opción_valida3 == False:
            input_grupos = input("Indique su opción (1 , 2 o 0): ").rstrip()
            if input_grupos in ["1","2","0"]:
                opción_valida3 = True
                menu_grupos = False
            else:
                print()
                print("Acción no valida, intente nuevamente")
                print()
        #si el input de grupos es 1, mostramos la interfaz de ver grupos
        if input_grupos == "1":
            ver_grupos = True
            
        #si el input de grupos es 2, iniciamos el proceso de crear grupo    
        if input_grupos == "2":
            print()
            nombre_grupo = input("Ingrese el nombre del grupo (no puede tener comas): ")
            print()
            nuevos_usuarios = input("Ingrese al menos 2 usuarios, separados por punto y coma:  ")
            opción_valida4 = False
            while opción_valida4 == False:
                crear_grupos = funciones.crear_grupo(nombre_grupo,usuario,nuevos_usuarios)

                if crear_grupos == False:
                    opción_valida4 = True
                    menu_grupos = True
                if crear_grupos == True:
                    print("Se ha creado el grupo con éxito :)")
                    opción_valida4 = True
                    ver_grupos = False
                    menu_grupos = True
        
        if input_grupos =="0":
            menu_chats = True
    
    #acá se inicia la interfaz de ver grupos
    if ver_grupos == True:
        grupos = funciones.desplegar_grupos(usuario)
        if grupos == None:
            print()
            print("No tienes grupos aun")
            print()
            menu_grupos = True
        else:
            print()
            print("**** Ver Grupos ****")
            print()
            print("Selecciona un grupo para \n ver tus conversaciones,\n o 0 para volver atras")
            print()
            for x in range(len(grupos)):
                print(f"[{x+1}] {grupos[x]}")
            print()
            print("[0] Volver")
            print()
            grupo = input("Ingrese el grupo: ")
            if grupo == "0":
                menu_grupos = True
                ver_grupos = False
            if grupo in archivos.diccionario_grupos.get(usuario):
                while True:
                    print()
                    print(f"**** Tu historial con {grupo} ****")
                    print()
                    funciones.desplegar_mensajes_grupo(grupo)
                    print()
                    print(f"**** Fin del historial con {grupo} ****")
                    input_mensaje_grupo = input("escriba un mensaje: ")
                    #si el mensaje escrito es igual a el parametro, volvemos a ver grupos\
                    #de lo contrario, lo escribimos.
                    if input_mensaje_grupo == parametros.VOLVER_FRASE:
                        ver_grupos = True
                        break
                    else:    
                        funciones.escribir_mensaje_grupo(input_mensaje_grupo,usuario,grupo)
                        funciones.actualizar_mensajes()








