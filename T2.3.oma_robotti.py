# Tehtävä T2.3.oma_robotti.py
# Piirtää suorakaiteista ja ympyrästä robotin, jolla on hiukset, hymyhuulilla ja silmät liikkuvat.
# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

# Robotti
import turtle as t

def rectangle (horizontal, vertical, color, teksti):
    t.pendown()
    t.pensize(1)
    t.color (color)
    t.begin_fill()
    print(str(t.pos()) + " = " + teksti)

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
t.bgcolor ('black')

# Tulostetaan ikkunan koordinaatit
print('ikkunan korkeus =',t.window_height())
print('ikkunan leveys =',t.window_width())

# Oikea jalkaterä
t.goto(-30, -90)
rectangle (50, 20, '#ed265b', 'teksti')

# Vasen jalkaterät
t.goto(-100, -90)
rectangle (50, 20, '#02e3f7', 'teksti')

# Oikea jalka
t.goto(-25, -30)
rectangle (15, 60, 'blue', 'oikea jalka')

# Vasen jalka
t.goto(-55, -30)
rectangle(-15 ,60, 'darkblue', 'vasen jalka')

# Oikea käsi
t.goto(10, 70)
rectangle (60, 15, 'purple', 'oikea kasi')
t.goto (55, 110)
rectangle (15, 40, 'purple', 'oikea kasi')

# Vasen käsivarsi
t.goto(-150, 70)
rectangle (60, 15, '#8d51f5', 'vasen kasivarsi')

# Vasen käsi
t.goto (-160, 70)
rectangle (15, 50, '#8d51f5', 'vasen kasi')

# Kaula 
t.goto(-50, 120)
rectangle (10, 30, 'orange', 'kaula')

# Ruumis
t.goto(-40, -60)

# set the fillcolor
t.fillcolor('#d2fa0a')
  
# start the filling color
t.begin_fill()
  
# drawing the circle of radius r
t.circle(80)
  
# ending the filling of the color
t.end_fill()

# Pää
t.goto(-85, 170)
rectangle (80, 50, '#02f727', 'teksti')

# Hiukset
t.goto(-50, 200)
rectangle (2, 30, '#1002d1', 'keskel_hiukset')

t.goto(-53, 181)
rectangle (2, 10, '#07fad1', 'vasen_hiukset')

t.goto(-56, 190)
rectangle (2, 10, '#07fad1', 'vasen_hiukset')

t.goto(-43, 181)
rectangle (2, 10, '#fa07cd', 'oikea_hiukset')

t.goto(-40, 190)
rectangle (2, 10, '#fa07cd', 'oikea_hiukset')

# Silmät
while True:
    # Tämä pitäisi tehdä funktiossa kuten tehtävä esimerkissä
    # eli piirtää yhdellä kertaa silmät
    t.goto(-60, 160)
    rectangle (30, 10, 'white','silmien valkoinen tausta')
    t.goto(-55, 155)
    rectangle (5, 5, 'black','silmat')
    t.goto(-40, 155)
    rectangle (5, 5, 'black','silmat')

    # Suu
   
    t.goto(-70, 140)
    rectangle (5, 10, '#f7021f', 'suu_vasen')
    
    t.goto(-70, 130)
    rectangle (50, 5, '#f7021f', 'suu_keskel')

    t.goto(-25, 140)
    rectangle (5, 10, '#f7021f', 'suu_oikea')

    t.hideturtle()
