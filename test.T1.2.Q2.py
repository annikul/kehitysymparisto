
# Ohjelma tulostaa 0-10 luvut ja kertoo mikä niistä on pariton ja mikä parillinen

# Yksikkötestausvaiheet:
# 

for counter in range (10):         # Normaali (10), jos haluaa testata (10+1)
    if(counter % 2) == 0:
        print(counter)
        print('on parillinen')
    else:
        print(counter)
        print('on pariton')