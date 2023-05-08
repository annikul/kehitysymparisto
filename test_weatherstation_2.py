import unittest
runtest = 1        # runtest on muuttuja ja se voi olla minka niminen vaan

def weatherstation(test_input):   # def weatherstation teki tästä funktion plus kaikkien yksi sisennys, mutta funktiota ei vielä kutsuta missään. Vasta alhaalla. Sen jälkeen parametri (test_input) muuttuja. 
    if runtest==0:
        weather = input('Mita saaennuste lupaa? (vetta/lunta/aurinkoista)') 
    if runtest==1:
        weather = test_input    # Silloin kun runtest on 1 annetaan weather muuttujalle test_input arvo
    if weather == 'vetta':
        output = 'Muista sateenvarjo!'      # muutetaan niin että tekstit ovat muuttujissa. output on muuttuja 'Muista sateenvarjo!' =arvo
        print(output)
    elif weather == 'lunta':
        output = 'Muista hanskat!'
        print(output)
    elif weather == 'aurinkoista':
        output = 'Muista aurinkolasit!'
        print(output)
    else:
        output = 'Etsi sopivat varusteet, ei vetta, lunta eika aurinkoista'
        print(output)
    if runtest == 1:
        return output

if runtest==1:

    # weatherstation ('vetta')   
    actual = weatherstation('vetta')
    print(actual)
    expected = 'Muista sateenvarjo!'
    try:
        assert actual == expected
    except:
        print('vetta = virhe')

    # weatherstation ('lunta')
    actual = weatherstation('lunta')
    print(actual)
    expected = 'Muista hanskat!'
    try:
        assert actual == expected
    except:
        print('lunta = virhe')

    # weatherstation ('aurinkoista')          
    actual = weatherstation('aurinkoista')  # Jos tähän teet virheen terminaali kertoo sen muuten toimii oikein.
    print(actual)
    expected = 'Muista aurinkolasit!'
    try:
        assert actual == expected
    except:
        print('aurinkoista = virhe')

# Testaa muuta runtest = 1 ja terminaaliin = python3 -m unittest test_weatherstation_2.py