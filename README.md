# Estrella de 9 puntas
En el proceso de creación de un programa para dibujar una estrella con Turtle en Python, se siguen varios pasos clave. En primer lugar, se importa el módulo Turtle mediante la línea de código **import turtle**, lo que habilita el uso de las funciones necesarias para realizar gráficos.

A continuación, se define la función **dibujar_estrella**, la cual toma tres argumentos: **tamano** (que representa la longitud de los segmentos de la estrella), **tortuga** (la tortuga que realiza el dibujo), y **num_puntas** (el número de puntas deseadas para la estrella). Esta función utiliza un bucle para llevar a cabo el dibujo de la estrella, ajustando el ángulo adecuado para lograr la forma deseada.

Luego, se procede a la configuración de Turtle mediante las líneas de código que establecen la velocidad (**turtle.speed(5)**), el grosor del lápiz (**turtle.pensize(1)**), y el color de la pluma (**turtle.pencolor("black")**). Estos ajustes influyen en la apariencia del dibujo final.

Una vez configurado Turtle, se crea una nueva "tortuga" llamada **mi_tortuga** con la línea **mi_tortuga = turtle.Turtle()**. Esta se utilizará para llevar a cabo el dibujo de la estrella y se configura con la forma de una tortuga.

Para personalizar la estrella según las preferencias del usuario, se incluye una entrada de usuario que solicita el número de puntas para la estrella mediante la línea **num_puntas = int(input("\nIngresa el número de puntas para la estrella: "))**. La respuesta del usuario se almacena en la variable **num_puntas** para su posterior uso.

A continuación, se realiza la llamada a la función **dibujar_estrella** con los parámetros correspondientes, incluyendo la longitud de los segmentos y la tortuga a utilizar. Esto lleva a cabo el proceso de dibujo de la estrella según las especificaciones proporcionadas.

Finalmente, el programa se concluye con la línea **turtle.done()**, la cual mantiene la ventana abierta hasta que el usuario decide cerrarla, permitiendo así la visualización del resultado final del dibujo. Este proceso de desarrollo estructurado garantiza la creación de una estrella personalizable y visualmente atractiva con la ayuda de Turtle en Python.
