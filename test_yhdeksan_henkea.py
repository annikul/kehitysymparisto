# Yhde
# Peli missä kayttajan pitaa valita vaikeusaste ja arvata sana

# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak


import random
import unittest

runtest = 1 # muuta 1 kun haluut testaa

def update_clue (guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

def yhdeksanhenkea(guess_test):
    lives = 9
    words =['koira', 'sieni', 'mieli', 'kovis', 'ankka', 'sohva']

    if runtest == 0:
        secret_word = random.choice (words)
    
    if runtest == 1:
        secret_word = guess_test

    print(secret_word)
    clue = list('?????')
    heart_symbol = u'\u2764'
    guessed_word_correctly = False 

    while lives > 0:
        print (clue)
        print ('Henkiä jäljellä: ' + heart_symbol * lives)
    
    if runtest == 0:
        guess = input ('Arvaa kirjain tai koko sana: ')

    if runtest == 1:
        guess = secret_word
    
    if guess in secret_word:
        update_clue (guess, secret_word, clue)

    else:
        print('Väärin. Menetit yhden hengen.')
        lives = lives - 1

    if lives == 0:
        print('Hävisit! Salainen sana oli ' + secret_word)

    if guess == secret_word:
        guessed_word_correctly = True
        
        if guessed_word_correctly:
            print ('Voitit! Salainen sana oli ' + secret_word)
            return secret_word
        
if runtest == 0:
    yhdeksanhenkea()

class yhdeksan_henkea(unittest.TestCase):
    def test_yhdeksan_henkea_success(self):
        actual = yhdeksanhenkea('koira')
        expected = ['koira', 'sieni', 'mieli', 'kovis', 'ankka', 'sohva']    
        print('actual= ', actual)
        self.assertIn(actual, expected)

# Testaa muuta runtest = 1 ja terminaaliin = python3 -m unittest test_yhdeksan_henkea.py