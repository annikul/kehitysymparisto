# Tehtävä T2.1.yhdeksan_henkea.py
# Sinulla on 9 elämää ja sinun pitää selvittää mikä sana on kyseessä, 
# voit arvata kirjaimia tai yrittää arvata koko sanan. 
# @author: ak
# @since: 17.4.2023
# @version: 1.0
# @change: ak

import random

lives = 9
words = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
secret_word = random.choice (words)
# print(secret_word) Kommentoin tämän koska muuten se tulostaa kysytyn sanan heti terminaaliin
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue (guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print (clue)
    print ('Henkiä jäljellä: ' + heart_symbol * lives)
    guess = input ('Arvaa kirjain tai koko sana: ')
    
    if guess in secret_word:
        update_clue (guess, secret_word, clue)
    
    else:
        print ('Väärin. Menetit yhden hengen.')
        lives = lives -1
        if lives == 0:
            print ('Hävisit! Salainen sana oli ' + secret_word)
    if guess == secret_word:
        guessed_word_correctly = True
        
        # print(guessed_word_correctly)
        if guessed_word_correctly:
            print ('Voitit! Salainen sana oli ' + secret_word)
            break
