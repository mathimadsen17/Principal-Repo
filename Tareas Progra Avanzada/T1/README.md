# Tarea 1: DCCanal :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

El programa es capaz de simular un canal de barcos, puede realizar acciones tales como ingresar un barco, desencallar un barco, mostrar el estado del canal, mostrar el riesgo de encallamiento de todos los barcos que se encuentran en el canal y simular una nueva hora. Cuando se simula una nueva hora, ingresamos un barco y luego se simula lo que pasa con todos los barcos que están adentro del canal, revisando si encallan o si ocurren sus eventos especiales, que varían según el tipo de barco. Cuando el barco llega al final del canal, se da el aviso y el canal recibe su pago.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Clase Barcos: Hecha completa
* Subclases de Barcos: Hechas completas
* Clase Mercancia: Hecha completa
* Clase Tripulación: Hecha completa
* CLase Canal: Hecha completa
* Menú inicio: Hecho completo
* Menu acciones: Hecho completo

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```menus.py``` en ```T1```
2. ```acciones.py``` en ```T1```
3. ```cargar_datos.py``` en ```T1```
4. ```clases.py``` en ```T1```
5. ```parametros.py``` en ```T1```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```abc```: ```ABC,abstractmethod / clases.py```
2. ```currency_converter```: ```CurrencyConverter() / acciones.py``` (debe instalarse)

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```main.py```: Es solo para iniciar el programa.
2. ```clases.py```: Contiene todas las clases.
3. ```menus.py```: Contiene el menú de inicio y el menú de acciones.
4. ```acciones.py```: Contiene funciones, que son las acciones que se pueden tomar en el menú de acciones.
5. ```cargar_datos.py```: En este modulo se cargan los datos entregados por los archivos csv a diccionarios.
6. ```parametros.py```: Este módulo contiene los parametros que se usarán en el programa.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

No se realizaron supuestos en esta tarea, todo se hizo según lo que decía el enunciado y las issues marcadas como importantes en Github, lo único que tengo que especificar es que cuando un barco encalla, los barcos que van atras pueden avanzar hasta toparselo.

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


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

No se usó codigo externo en esta entrega.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
