# Tarea 2: DCCimpson :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

Mi tarea al iniciarla, da dos opciones, ver el ranking de laos 5 mejores resultados o simplemente ingresar un usuario y empezar una partida, para empezar una partida hay que ingresar un usuario alfanumerico. Una vez empezada la partida veremos la ventana de preparación, en la cual podemos escoger una dificultad y un personaje para jugar. Para empezar a jugar simplemente hay que llevar al personaje a su lugar correspondiente (Homero - Planta nuclear, Lisa - Escuela). Una vez que empieza el juego, apareceran obstaculos y cada cierto tiempo y dependiendo de la dificultad escogida, apareceran y desapareceran objetos. Las rondas duran distinto dependiendo de su dificultad. Una vez terminada la ronda, se guardará el puntaje y podrá continuar jugando siempre y cuando tenga vida.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Ventana de Inicio: No senñala cuando el nombre no es correcto, pero si verifica que sea un nombre alfanumerico.
* Ventana de Ranking: Debería funcionar correctamente
* Ventana de Preparación : Hecha completa
* Ventana de Juego : Hecha completa, el puntaje no se va actualizando eso si a medida que pasa el juego, pero todo lo demas si.
* Ventana de post-ronda: Hecha completa.
* Mecanicas de juego: Dividiré la mecánica en items acorde a la pauta
    * Personaje : El movimiento de los personajes es fluido sin embargo no animado, tampoco tienen habilidades especiales, si respetan sus parametros.
    * Lugares de juego: No se muestra un mensaje al colisionar con un lugar incorrecto.
    * Objetos : Hecho completo
    * Obstaculos : No siempre hay suficiente espacio para que el personaje pueda pasar entre ellos.
    * Personaje enemigo : No esta implementado.
    * Fin de Ronda: Hecho completo
    * Fin de Juego: La persona aunque pierda pude seguir jugando, aunque si es notificada, y se almacena su puntaje en ranking.txt aunque a veces pasaba que se escribia 2 veces.
* Cheatcodes : No estan implementados.
* General: Sinceramente me costó mucho distinguir que era para el backend y que era para el frontend, igual tengo una carpeta para backend y otra para frontend sin embargo creo que en el caso de la ventana de juego, hay muchas cosas que deberían ir en el backend. Creo que ese sería el unico problema en este item.
* Bonus: Le puse la música :)

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```ranking.txt``` en ```T2```
2. ```backend``` en ```T2```
3. ```frontend``` en ```T2```
4. ```main.py``` en ```T2```
5. ```Logo.png``` en ```T2```
6. ```ventana_inicio.py``` en ```frontend```
7. ```ventana_juego.py``` en ```frontend```
8. ```ventana_post.py``` en ```frontend```
9. ```ventana_preparacion.py``` en ```frontend```
10. ```ventana_ranking.py``` en ```frontend```
11. ```clases.py``` en ```backend```
12. ```logica_menus.py``` en ```backend```
13. ```parametros.py``` en ```backend```
14. ```ventana_inicio.ui``` en ```T2```
15. ```ventana_juego.ui``` en ```T2```
16. ```ventana_post.ui``` en ```T2```
17. ```ventana_preparacion.ui``` en ```T2```
18. ```ventana_ranking.ui``` en ```T2```
19. ```sprites``` en ```T2```





## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```sis```
2. ```os```: Esta libreria la usé para el path.join()
3. ```PyQt5``` : Creo que esta demas decir para que use esta librería.
3. ```time```: Usé el sleep, para los threads
4. ```operator```: Usé esta librería para ordenar un diccionario para el tema del ranking.
5. ```random```: Usé el random para las probabilidades de los objetos.
### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ventana_juego.py```: Este modulo contiene la clase ```VentanaJuego```.
1. ```ventana_inicio.py```: Este modulo contiene la clase ```VentanaInicio```.
1. ```ventana_post.py```: Este modulo contiene la clase ```VentanaPost```.
1. ```ventana_preparacion.py```: Este modulo contiene la clase ```VentanaPreparacion```.
1. ```main.py```: Este modulo inicia el programa y conecta las señales.
1. ```clases.py```: Este modulo contiene las clases ```ThreadTiempo``` y ```ThreadObjeto``` que son los threads que uso para mi programa.
1. ```logica_menus.py```: Este modulo contiene la clase ```LogicaInicio``` que es donde trabajo la lógica de mi programa.
1. ```parametros.py```: Este modulo guarda todos los parametros.







## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Solo aparece un objeto a la vez, lo hice así por simplicidad y porque no me llevo muy bien con el manejo de los QThreads.

PD: el sprite ```Logo.png``` tiene que estar en la carpeta "T2" al momento de iniciar el programa, si no, no se verá. 

PD2: Perdón por tan poco en esta tarea, se me juntaron pruebas y entregas de otros ramos, además que nunca pude estudiar de la mejor forma la materia de interfaces gráficas. Puse mi máximo esfuerzo en esta tarea y me hubiera encantado terminarla por el hecho de que soy fanatico de los simpsons y la tarea estaba muy entretenida.
Ánimo con las correcciones ayudante(s) :)


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
1. La AF4, de ahí saque codigo para abrir ventanas
2. https://www.delftstack.com/es/howto/python/how-to-sort-a-dictionary-by-value/ de ahí saqué código para ordenar un diccionario por su valor



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
