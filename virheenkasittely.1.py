# ValueError
# Antaa virheen jos laittaa tekstiä

while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print('Oops! That was no valid number Try again') 



# Voisi tehdä myös näin. Käsittelee kaikki virheet
#while True:
    #try:
        #x = int(input('Please enter a number: '))
        #break
    #except
        #print('Tapahtunut virhe') 