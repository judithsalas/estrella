import turtle

def dibujar_estrella(tamano, tortuga, num_puntas):
    angulo = 180 / num_puntas
    for _ in range(num_puntas):
        tortuga.forward(tamano)
        tortuga.right(180 - angulo)

# Configuración de Turtle
turtle.speed(5)
turtle.pensize(1)
turtle.pencolor("black")

# Creamos una nueva "tortuga"
mi_tortuga = turtle.Turtle()
mi_tortuga.shape("turtle")

# Solicitamos al usuario el número de puntas para la estrella
num_puntas = int(input("\nIngresa el número de puntas para la estrella: "))

# Llamamos a la función para dibujar la estrella
dibujar_estrella(200, mi_tortuga, num_puntas)

# Para finalizar el programa cuando se termine de dibujar la estrella
turtle.done()
