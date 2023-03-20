import turtle
from itertools import cycle

# Vaihdetaan 'red' RGB Hex-muotoon ja lisätään loppuun megenta väri lisää
#colors = cycle(['#FF000', 'orange', 'yellow', 'green', 'blue', 'purple', 'FF00FF', '#00FF00', 'magenta'])

def draw_circle(size, angle, shift):
    turtle.pencolor (next(colors))
    turtle.circle (100)
    turtle.right(20)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift +1)

for i in range(6):
    for colours in ['#FF000', 'orange', 'yellow', 'green', 'blue', 'purple', 'FF00FF', '#00FF00', 'magenta']

turtle.bgcolor ('black')
turtle.speed ('fast')
turtle.pensize (10)
draw_circle(30, 45, 10)

turtle.hideturtle()
    