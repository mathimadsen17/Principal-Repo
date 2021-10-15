# Tarea X: Nombre de la tarea :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Voy a hacer esto lo mas facil para el ayudante que me corrija la tarea. Estoy con otros examenes en los que necesito harta nota para pasar, es por eso que casi no tuve tiempo para hacer esta tarea :( , me da mucha verguenza entregar esto pero de verdad que no me están dando los tiempos para terminar el semestre con todos los ramos pasados>

### Cosas implementadas y no implementadas :white_check_mark: :x:

(Para hacer mas simple la corrección solo pondré las cosas implementadas)

* codificacion.py : Se puede codificar un mensaje y descodificarlo, tambíen se puede codificar una ruta de una iamgen.
* Están creadas las ventanas de ingreso, sala y juego, se pueden encontrar en la capeta de Cliente.
* Servidor: El servidor está creado y se puede ejecutar a traves del main.py
* Cliente: hay un backend que verifica el nombre, pero no lo uso porque después me di cuenta de que esa función la debe hacer el servidor.
* 

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```backend.py``` en ```Cliente```
1. ```codificacion.py``` en ```Cliente```
1. ```main_quizas.py``` en ```Cliente``` (ignorar)
1. ```main.py``` en ```Cliente```
1. ```ventana_ingresar.py``` en ```Cliente```
1. ```ventana_ingresar.ui``` en ```Cliente```
1. ```ventana_juego.py``` en ```Cliente```
1. ```ventana_juego.ui``` en ```Cliente```
1. ```ventana_sala.py``` en ```Cliente```
1. ```ventana_sala.ui``` en ```Cliente```
1. ```main.py``` en ```Server```
1. ```servidor.py``` en ```Server```



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sys```: Se usa en varios módulos
2. ```os```: ```codificacion.py``` 


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:


1. ```ventana_juego.py```: Este modulo contiene la clase ```VentanaJuego```.
1. ```ventana_ingresar.py```: Este modulo contiene la clase ```VentanaIngresar```.
1. ```ventana_sala.py```: Este modulo contiene la clase ```VentanaSala```.
1. ```main.py```: Este modulo inicia el cliente o el servidor según el modulo que se este viendo
1. ```backend.py```: Este modulo una función para verificar el nombre.
1. ```servidor.py```: Este modulo contiene la clase ```Servidor``` que es basicamente el servidor.
1. ```parametros.json```: Este modulo guarda todos los parametros.



PD: Lo siento querido ayudante por hacerle perder el tiempo con mi tarea, ojalá este teniendo un buen fin de semestre :)


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
1. Contenidos
2. AF7



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
