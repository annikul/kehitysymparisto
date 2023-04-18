# Koodissa on virhe mutta se on hallinnassa

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('result = ',result)
   
# Nollallajako kaataa ohjelman
divide(1, 0)

# Mutta tämäkin lasketaan rivien (4, 6-10) takia
divide(1, 1)
