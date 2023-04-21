# Tehtävä T2.5.oma_kaleidospiraali
# Tekee ympyröitä peräkkäin ja aina seuraava on isompi kun edellinen ja se näyttää aivan kukalta
# @author: ak
# @since: 19.4.2023
# @version: 1.0
# @change: ak

import turtle
from itertools import cycle


colors = cycle(['#7A000C', '#8F000E', '#FF0A23', '#7A000C', '#FF0A23', '#8F000E','#FF0A23' ])

def draw_circle(size, angle, shift):
    turtle.pencolor (next(colors))
    turtle.circle (size)
    turtle.right (angle)
    turtle.forward(shift)
    draw_circle(size + 1, angle + 1, shift +1)
  
turtle.bgcolor ('black')
turtle.speed ('fast')
turtle.pensize (3)
draw_circle(30, 45, 10)

turtle.hideturtle()