# Tehtävä test_salasana_valitsin.py
# Testi tulostaa sinulle salasanan random sanoista, numeroista, erikoismerkeistä
# ja kertoo montako merkkiä siinä on. 
# Testi menee läpi jos salasanassa on 11 tai enempi merkkiä.
# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

import random
import string
import unittest

runtest=1 # muuta 1 kun haluut testaa

def generate_password():
    nouns = ['omena','dinosaurus','pallo','paahdin','vuohi','lohikäärme',
             'vasara','sorsa','panda','puhelin','banaani','opettaja']

    adjectives = ['uninen','hidas','haiseva','märkä','lihava','punainen',
                  'oranssi','keltainen','vihreä','sininen','purppura','pörröinen',
                  'valkoinen','leuhka','uljas']

    while True:

        # valitaan satunnaisesti adjectives listalta
        adjective = random.choice(adjectives)

        # valitaan satunnaisesti nouns listalta
        noun = random.choice (nouns)

        # satunnainen numero väliltä 0...99
        number = random.randrange(0, 100)

        special_char = random.choice(string.punctuation)
        
        # rakennetaan salasana
        password = adjective + noun + str(number) + special_char

        print(' Uusi salasanasi on: %s' % password)

        return password
    
if (runtest==0):
    generate_password()

class test_salasana(unittest.TestCase):
    def test_generate_password_success(self):
        actual = len(generate_password())
        print('actual= ',actual)
        self.assertGreater(actual, 11)  # Jotta testi menee läpi salasanan pituus on 11 merkkiä tai enemmän.

# Voisi testa myös näin mutta silloin pitää laittaa expected kohtaan kaikki numerot.
"""class test_salasana(unittest.TestCase):
    def test_generate_password_success(self):
        actual = len(generate_password())
        expected=[11,12,13,14,15,16,17,18,19,20]  # Sallitut pituudet salasanalle, jos on pitempi kuin 20 tulee virhe
        print('actual= ',actual)
        self.assertIn(actual,expected)   # assertIn = että ei saa olla minkään muun pituinen kuin 11-20 kirjainta muuten tulee virhe
        """

# Testaa muuta runtest = 1 ja terminaaliin = python3 -m unittest test_salasana_valitsin.py
# test_salasana.py pitää olla sama kuin tiedoston nimi eli tän jutun nimi