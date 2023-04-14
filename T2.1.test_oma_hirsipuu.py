# Hirsipuu
# Peli missä käyttäjän pitää valita vaikeusaste ja arvata sana

# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak


import random
import unittest

runtest=1 # muuta 1 kun haluut testaa

lives = 9

# Sanalistojen määritys vaikeusasteen mukaan
words1 =['koira', 'sieni', 'mieli', 'kovis', 'ankka', 'sohva']
words2 =['lakana', 'random', 'jäinen', 'tv-taso', 'silmät', 'läppäri']
words3 =['ambulanssi', 'aisapari', 'ketutus', 'lumiaura', 'kesäloma', 'aurinkoranta']

# Valikon ohjelmointi
difficulty = input ('Choose difficulty (Taso 1, 2 or 3):\n 1 Helppo\n 2 Normaali\n 3 Vaikea\n')

# Muutetaan merkki kokonaisluvuksi
difficulty = int (difficulty)

# Lives muuttujan ja sanalistan valinta valitun vaikeusasteen mukaan

if difficulty == 1:
    lives = 12
    words = words1

elif difficulty == 2:
    lives = 9
    words = words2

else:
    lives = 6
    words = words3

# Satunnaisen salaisen sanan valinta vaikeusasteen mukaisesta sanalistalta
secret_word = random.choice (words)

# Vinkkilistan pituuden määritys valitun sanan pituuden mukaan
# clue = list('?????')
guessed = []
clue = []
index = 0
heart_symbol = u'\u2764'
guessed_word_correctly = False

while index < len(secret_word):
    clue.append('_')
    index = index + 1

def update_clue (guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print('----------------------')
    print('Arvaa sana: ' + ' '.join(clue))
    print('Henkiä jäljellä: ' + heart_symbol * lives)
    print('Arvatut kirjaimet: ' + ','.join(guessed))
    guess = input ('Arvaa kirjain tai koko sana: ')
    guessed.append(guess)
    

    if guess in secret_word:
        update_clue (guess, secret_word, clue)

    else:
        print('Väärin. Menetit yhden hengen.')
        lives = lives - 1
        if lives == 0:
            print('Hävisit! Salainen sana oli ' + secret_word)
            
    if guess == secret_word:
        guessed_word_correctly = True

        #print(guessed_word_correctly)
        if guessed_word_correctly:
            print('Voitit! Salainen sana oli ' + secret_word)
            break

        if (runtest==0):
            generate_password()

class test_salasana(unittest.TestCase):                     
    def test_generate_password_success(self):
        actual = len(generate_password())
        expected=[11,12,13,1,4,15,16,17,18,19,20]
        print('actual= ',actual)
        self.assertIn(actual,expected)

# Testaa muuta runtest = 1 ja terminaaliin= python3 -m unittest test_hirsipuu.py
# test_hirsipuu.py pitää olla sama kuin tiedoston nimi eli tän jutun nimi