# Tehtävä T1.9.3.Q2.oma_salasana_valitsin.py
# Tulostaa sinulle salasanan random sanoista, numeroista, erikoismerkeistä
# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak

import random
import string

def generate_password():
    nouns = ['koira','pallokala','aita','höyry','ovi','ampiainen',
             'kirves','kallo','nenä','lanka','tryffeli','valo']

    adjectives = ['violetti','nopea','oksettava','nenäkäs','iso','karvainen',
                  'kiltti','fiksu','hauska','kaikkitietävä','musta','harmaa',
                  'pehmeä','hiljainen','ahdistava']

    while True:

        # valitaan satunnaisesti adjectives listalta
        adjective = random.choice(adjectives)

        # valitaan satunnaisesti nouns listalta
        noun = random.choice(nouns)

        # satunnainen numero väliltä 0...99
        number = random.randrange(0, 100)

        special_char= random.choice(string.punctuation)
       
       # rakennetaan salasana
        password = adjective + noun + str(number) + special_char

        print(' Uusi salasanasi on: %s' % password)

        response = input("Haluatko toisen salasanan? Vastaa k tai e ")

        if response == 'e':
            break
        else:
            return password

generate_password()