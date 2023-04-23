# test_tahtikirkasyo.py
# Testi testaa että piirtonopeus on enemmän kuin 6. Nopeus 1-6 antaa virheen ja 7-> testi menee läpi.
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
speed = 7 # piirtonopeus. Tähän laittamalla 1-6 tulee virhekoodi


def draw_star(points, size, col, x, y, speed): # lisätty speed
    piirto_menossa = True
    t.speed(speed)  # Muutettu (speed)
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
        draw_star(ranPts, ranSize, ranCol, x, y, speed) # lisätty speed
        t.onscreenclick(t.goto(x,y))

        if (runtest == 1): 
            return speed            
        
if (runtest == 0):
    tahtikirkasyo()

class test_tahtikirkasyo(unittest.TestCase):
    def test_tahtikirkasyo_success(self):
        speed = tahtikirkasyo()
        print('actual= ', speed)
        self.assertGreater(speed, 6)  # assertGreater tekee sen että speed pitää olla enempi kuin 6. 0-6 antaa virhekoodin

# Testaa muuta runtest = 1 ja terminaaliin = python3 -m unittest test_tahtikirkasyo.py
# test_tahtikirkasyo.py pitää olla sama kuin tiedoston nimi eli tän jutun nimi

"""Voisi tehdä myös näin, mutta sitten lukuja joutuisi kirjoittamaan loputtomiin asti
class test_tahtikirkasyo(unittest.TestCase):
    def test_tahtikirkasyo_success(self):
        speed = tahtikirkasyo()
        sallitutArvot = [6,7,8,9,0] 
        print('actual= ', speed)
        self.assertIn(speed,sallitutArvot)
        """