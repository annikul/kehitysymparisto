# Tehtävä T2.3.robotti_paja.py
# Piirtää eri värisistä suorakaiteista robotin.
# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

# Robotti
import turtle as t

def rectangle (horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color (color)
    t.begin_fill()
    print(t.pos())
    
    for counter in range (1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup ()
t.speed ('fastest')
# t.bgcolor ('Dodger blue')
t.bgcolor ('orange')

# Tulostetaan ikkunan koordinaatit
print('ikkunan korkeus =',t.window_height())
print('ikkunan leveys =',t.window_width())

# jalkaterät
t.goto(-100, -150)
rectangle (50, 20, 'blue')
t.goto(-30, -150)
rectangle (50, 20, 'blue')

# jalat
t.goto(-25, -50)
rectangle (15, 100, 'grey')
t.goto(-55, -50)
rectangle (-15, 100, 'grey')

# ruumis
t.goto(-90, 100)
rectangle (100, 150, 'red')

# käsivarret
t.goto(-150, 70)
rectangle (60, 15, 'grey')
t.goto(-150, 110)
rectangle (15, 40, 'grey')

t.goto(10, 70)
rectangle (60, 15, 'grey')
t.goto(55, 110)
rectangle (15, 40, 'grey')

# kaula
t.goto(-50, 120)
rectangle (15, 20, 'grey')

# pää
t.goto(-85, 170)
rectangle (80, 50, 'red')

# silmät
t.goto(-60, 160)
rectangle (30, 10, 'white')
t.goto(-55, 155)
rectangle (5, 5, 'black')
t.goto(-40, 155)
rectangle (5, 5, 'black')

# suu
t.goto(-65, 135)
rectangle (40, 5, 'black')

t.hideturtle()
