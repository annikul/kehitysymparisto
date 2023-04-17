# Tehtävä T2.5.kaleidospiraali
# Tekee ympyröitä peräkkäin ja aina seuraava on isompi kun edellinen.
# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

import turtle
from itertools import cycle

# Vaihdetaan 'red' RGB Hex-muotoon ja lisätään loppuun megenta väri lisää
colors = cycle(['#FF0000', 'orange', 'yellow', 'green', 'blue', 'purple', '#FF00FF', '#00FF00', 'magenta'])

def draw_circle(size, angle, shift):
    turtle.pencolor (next(colors))
    turtle.circle (size)
    turtle.right (angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift +1)
  
turtle.bgcolor ('black')
turtle.speed ('fast')
turtle.pensize (10)
draw_circle(30, 45, 10)

turtle.hideturtle()