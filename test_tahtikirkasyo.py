# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

# Tähtikirkas yö 

import turtle as t
import unittest
import math as m
from random import randint, random
runtest = 1

x = 0
y = 0

def draw_star(points, size, col, x, y):
    piirto_menossa = True
    t.speed(6)
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 -(180 / points)
    t.color(col)
    t.begin_fill()
    
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

# Pääohjelma
def tahtikirkasyo():
    t.Screen().bgcolor('black')

    while True:

        koordinaatti = t.pos();
        x = m.floor(randint(-200, 200))
        y = m.floor(randint(-200, 200))
        print(x,y)
        ranPts = randint(2, 5) * 2 + 1
        ranSize = randint(10, 50)
        ranCol =(random(), random(), random())
        draw_star(ranPts, ranSize, ranCol, x, y)
        t.onscreenclick(t.goto(x,y))

        if (runtest == 1): 
            output=[x.real, y.real]  # real = kokonaisluku. Vektori siinä on kaksi jos on useempia se on matriisi
            return output
        
if (runtest == 0):
    tahtikirkasyo()

class test_tahtikirkasyo(unittest.TestCase):
    def test_tahtikirkasyo_success(self):
        actual=tahtikirkasyo()

# Testaa muuta runtest = 1 ja terminaaliin = python3 -m unittest test_tahtikirkasyo.py
# test_tahtikirkasyo.py pitää olla sama kuin tiedoston nimi eli tän jutun nimi