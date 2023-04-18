# Jakolasku. Antaa virhettä jos laitat toiseksi numeroksi 0 muuten laskee jakolaskun.
# Nyt koska tässä on virheenkäsittelijä (rivit 10, 12-17)(try, except, else, finally printit) koodi ei kaadu ensimmäiseen virheeseen
# vaan laskee toisenkin laskun

# Jos ottaa pois virheenkäsittelyn rivit (10, 12-17)(try, except, else, finally printit) 
#niin jää vain laskuoperaatio funktiossa ja ajetaan kaksi laskua.
# pitää olla yksi sisennys

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('result is', result)
    finally: 
        print('executing finally clause')

divide(10, 0)         # Kutsu funktiota. Antaa virheen koska toinen numero on 0.
divide(10, 3)         # mutta jos laitat jonkun muun numeron laskee jakolaskun ja antaa sen tuloksen.

