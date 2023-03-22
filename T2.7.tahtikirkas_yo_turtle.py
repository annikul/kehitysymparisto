# Tähtikirkas yö 

import turtle as t
import math as m
from random import randint, random
x = 0
y = 0

def draw_star (points, size, col, x, y):
    piirto_menossa = True
    t.goto(x, y)
    t.pendown
    angle = 180 -(180 / points)
    t.color (col)
    t.begin_fill ()
    
    for i in range (points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

# Pääohjelma
t.Screen () .bgcolor('black')

while True:

    koordinaatti = t.pos();
    x = m.floor(koordinaatti[0])
    y = m.floor(koordinaatti [1])
    print(x,y)
    ranPts = randint (2, 5) * 8 + 1
    ranSize = randint (10, 50)
    ranCol = (random(), random(), random())
    draw_star (ranPts, ranSize, ranCol, x, y)
    t.onscreenclick(t.goto(x,y))
