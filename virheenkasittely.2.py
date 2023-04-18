# Koodissa ei ole virheenkäsittelijää
# -> Koodi kaatuu

def divide(x, y):
    result = x / y

# Nollallajako kaataa ohjelman
divide(1, 0)

# Tätä riviä ei enään ajata koska ohjelma kaatui
divide(1, 1)

# Jos tämä olisi niin kuin virheenkasittely.4.py ohjelma ei kaatuisi vaikka ekassa on virhe.