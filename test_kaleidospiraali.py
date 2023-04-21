# Tehtävä test_kaleidospiraali
# Tekee ympyröitä peräkkäin ja aina seuraava on isompi kun edellinen.
# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

import turtle
import unittest
from itertools import cycle
runtest = 1

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

def kaleidospiraali():
    if (runtest == 1): 
            output=[5, colors]   
            return output

if (runtest == 0):
        kaleidospiraali()

class test_kaleidospiraali(unittest.TestCase):
    def test_kaleidospiraali_success(self):
        actual=kaleidospiraali()
        



# Testaa muuta runtest = 1 ja terminaaliin = python3 -m unittest test_kaleidospiraali.py
# test_kaleidospiraali.py pitää olla sama kuin tiedoston nimi eli tän jutun nimi