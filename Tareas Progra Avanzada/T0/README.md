# Tarea 0: Nombre de la tarea : DCConecta2 :


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

El programa es capaz de crear usuarios, iniciar sesión con usuarios existentes, luego se puede elegir si ingresar al menú de contactos o al menú de grupos. En caso de elegir el menú de contactos se puede añadir un contacto o ver los contactos, si se elige añadir un contacto, el programa verifica que el usuario existe y en caso de existir lo agrega a los contactos. En caso de elegir ver los contactos, se desplegan todos los contactos del usuario. En el menú de grupo se ofrece la opción de crear grupo y de ver grupos. Si se elige la opción de crear grupo, se tiene que ingresar el nombre del grupo y al menos 2 participantes. Si se elige la opción de ver grupos se desplegaran todos los grupos del usuario. Tanto en el caso de los contactos como en los grupos si el usuario escribe el nombre del contacto o analogamente el nombre del grupo se desplegará el historial de conversación. Para salir del historial de conversación se debe escribir "\volver". Para correr el programa se debe descargar la carpeta T0 del repositorio personal, abrir esa carpeta desde la terminal y luego correrla con python 3.7.


### Cosas implementadas y no implementadas :white_check_mark: :x:

* Chats regulares: Hecho completo :white_check_mark:
* Chats grupos: Me faltó implementar el parametro para abandonar grupo:x::white_check_mark:
* Menú de inicio: Hecho completo :white_check_mark:
* Menú de chats: Hecho completo :white_check_mark:
* Menú de contactos: Hecho completo :white_check_mark:
* Menú de grupos: Hecho completo :white_check_mark:

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivos.py``` en ```T0```
2. ```contactos.csv``` en ```T0```
3. ```funciones.py``` en ```T0```
4. ```grupos.csv``` en ```T0```
5. ```mensajes.csv``` en ```T0```
6. ```parametros.py``` en ```T0```
7. ```usuarios.csv``` en ```T0```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```función(datetime) / funciones.py```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```main.py```: Esta es el módulo principal y esta hecho para correr el programa.
2. ```funciones.py```: En este modulo están las funciones.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. No es un supuesto pero para el parametro VOLVER_FRASE, no funcionaba con "\\volver" asi que hay que escribir solo "\volver"




-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://programminghistorian.org/es/lecciones/trabajar-con-archivos-de-texto : Use código de esta página para abrir los archivos y trabajar con ellos.
2. https://www.w3schools.com/python/ref_list_sort.asp : Saqué código de esta pagina para ordenar los mensajes de los usuarios por fecha.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
