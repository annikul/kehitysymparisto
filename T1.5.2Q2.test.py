# HUOM! testissä ei saa olla ääkkosia!!!

# Anna syottoarvona 1:ssa testauksessa = vetta
# Anna syottoarvona 2:ssa testauksessa = lunta
# Anna syottoarvona 3:ssa testauksessa = aurinkoista

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
    weatherstation('')          # Voit kokeilla että toimiiko koodi kun laitat alas ja ylös runtest 1 ja tähän'' väliin lunta jne 
                                # Tässä kutsutaan funktiota eli weatherstation() on funktio. 
                                # Jos haluat ajaa sen monta kertaa niin tee loop tai kopio tuo rivi alas.

    