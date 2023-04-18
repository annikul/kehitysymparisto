# Anna syöttöarvona 1:ssä testauksessa = vettä
# Anna syöttöarvona 2:ssä testauksessa = lunta
# Anna syöttöarvona 3:ssä testauksessa = aurinkoista

weather = input('Mitä sääennuste lupaa? (vettä/lunta/aurinkoista)')

# Ensimmäinen ehto. Tämä lohko suoritetaan jos ensimmäinen ehto on tosi
if weather =='vettä':
    print ('Muista sateenvarjo!')

# Toinen ehto
elif weather == 'lunta':
    print('Muista hanskat!')

# Kolmas ehto
elif weather == 'aurinkoista':
    print('Muista aurinkolasit!')

# Muutoin
else:
     print('Etsi sopivat varusteet, ei vettä, lunta eikä aurinkoista')