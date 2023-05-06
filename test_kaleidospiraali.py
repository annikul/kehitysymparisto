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

pensize = 3

# Vaihdetaan 'red' RGB Hex-muotoon ja lisätään loppuun megenta väri lisää
colors = cycle(['#7A000C', '#8F000E', '#FF0A23', '#7A000C', '#FF0A23', '#8F000E','#FF0A23'])

def draw_circle(size, angle, shift):
    turtle.pencolor (next(colors))
    turtle.circle (size)
    turtle.right (angle)
    turtle.forward(shift)
    draw_circle(size + 1, angle + 1, shift +1)

turtle.bgcolor ('black')
turtle.speed (6)
turtle.pensize (3)
draw_circle(30, 45, 10)

turtle.hideturtle()

def kaleidospiraali(pensize):
    pensize('pensize')

    if (runtest == 1):    
        return pensize

if (runtest == 0):
        draw_circle()

class test_kaleidospiraali(unittest.TestCase):
    def test_kaleidospiraali_success(self):
        #bgcolor = kaleidospiraali()
        pensize = kaleidospiraali()
        #pensize = kaleidospiraali()
        print('actual= ', pensize)
        self.assertGreater(pensize, 1)
 
# Testaa muuta runtest = 1 ja terminaaliin = python3 -m unittest test_kaleidospiraali.py
# test_kaleidospiraali.py pitää olla sama kuin tiedoston nimi eli tän jutun nimi