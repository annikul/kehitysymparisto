weather = input('Mitä sääennuste lupaa? (vettä/lunta/aurinkoista)')

# Ensimmäinen ehto
if(weather =='vettä'):
    print ('Muista sateenvarjo!')

# Toinen ehto
elif weather == 'lunta':
    print('Muista hanskat!')

# Kolmas ehto

elif weather == 'aurinkoista':
    print('Muista aurinkolasit!')

# Muutoin
else:
     print('Etsi sopivat varusteet, ei vetää, lunta eikä aurinkoista')