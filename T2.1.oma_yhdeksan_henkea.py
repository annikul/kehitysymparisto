# Tehtävä T2.1.oma_yhdeksan_henkea.py
# Valitse vaikeustaso 1-3. Vaikeustasosta riippuen sinulla on 6-12 elämää ja sinun 
# pitää selvittää mikä sana on kyseessä, voit arvata kirjaimia tai yrittää arvata koko sanan. 
# Näet koko ajan oikein arvaamasi kirjaimet "ARVAA SANA" kohdassa 
# ja väärin arvaamasi kirjaimet "ARVATUT KIRJAIMET" kohdassa
# @author: ak
# @since: 22.3.2023
# @version: 1.0
# @change: ak



# Peli missä käyttäjän pitää valita vaikeusaste ja arvata sana
import random

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
