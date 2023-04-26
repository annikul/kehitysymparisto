# Ohjelma tulostaa 1-10 luvut ja kertoo mikä niistä on pariton ja mikä parillinen. 
# Testi tarkistaa mikä luku on pariton ja parillinen
# @author: ak
# @since: 18.4.2023
# @version: 1.0
# @change: ak

# Yksikkötestausvaiheet:
# 1. luo kansio koodille tai lataa github:sta opettajan repositori ja avaa kansio seka luo python file kansioon
# (kansion polussa ei saa olla skandeja joten ala kayta onedrivea koska kulun nimessa on skandeja)
# 2. lisaa koodiin header alkuun mallin mukaan ja lisaa pvm seka omat nimikirjaimet
# 3.. poista koodista kaikki skandit
# 4. muokataan koodi funktiomuotoon (nimea funktio)
# 5. importoidaan yksikkötestikirjasto
# 6. lisätään runtest- muuttuja.
# 7. jos runtest == 0 niin kutsuu em. luotua funktiota ja ohjelma toimii normaalisti
#    testaa etta koodi toimii normaalisti kun runtest == 0
# 8. lisataan testauksessa tarvittavat funktioparametrit ja vertailut
# (kun runtest == 1 niin blokataan mahdolliset kayttoliittymainputit yms. pois koodista)
# -> em. blokatut muuttuja syotetaan funktioparametreina testattavaan funktioon)
# 9. testaa että peruskoodi tulostaa testattavaa numeroa vastaavaan testiarvon
# kun peruskoodi tulostaa oikeita arvoja syottoparametreille niin lisataan testiluokka seka return lauseke
# peruskoodiin
# 10. lisataan testiluokka ja testifunktiot
# 11. ajetaan yksikkotestit terminaalista ja dokumentoidaan koodi (github)
# 12. palauta yksikkötestattu koodi github "fork"- toiminnalla opettajalle opettajan repositoriin

import unittest
runtest=1               # runtest = 1 testataan koodia, runtest = 0 toimii normaalisti   #runtest on muuttuja

def parillisuus(luku):
    for counter in range (1, luku + 1):         # Normaali (10), jos haluaa testata (10+1)
        if(counter % 2) == 0:
            print(counter)
            palautusarvo = 'on parillinen'
            print(palautusarvo)
        else:
            print(counter)
            palautusarvo= 'on pariton'
            print(palautusarvo)

    if runtest == 1:
        return palautusarvo
            
if runtest == 0:
    parillisuus(2)

# Testataan parittomat
class test_parillinen_pariton(unittest.TestCase):
    def test_parillinen_pariton_success_pariton(self):
        testiarvo = 3
        actual = str(parillisuus(testiarvo))
        excepted = 'on pariton'
        try:
            assert actual == excepted
        except:
            print('Virhe parittomuuden tarkistamisessa' + ' Numero = ' + str(testiarvo) + ' ' + actual + ' erisuuri ' + excepted)

# Testataan parilliset 

    def test_parillinen_pariton_success_parillinen(self):
            testiarvo = 4
            actual = str(parillisuus(testiarvo))
            excepted = 'on parillinen'
            try:
                assert actual == excepted
            except:
                print('Virhe parittomuuden tarkistamisessa' + ' Numero = ' + str(testiarvo) + ' ' + actual + ' erisuuri ' + excepted)

# python -m unittest test_parillinen_pariton.py