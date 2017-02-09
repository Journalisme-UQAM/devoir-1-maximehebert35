#coding: utf-8

# Pour les matricules de 1930 à 1999
for annee in range(30000,100000):
    print(annee)

# Pour les matricules de l'an 2000
for annee in range(0,10):
    print("0000{}".format(annee))
    
for annee in range(10,100):
    print("000{}".format(annee))

for annee in range(100,1000):
    print("00{}".format(annee))

# Pour les matricules de 2001 à 2009    
for annee in range (1000, 10000):
    print("0{}".format(annee))

# Pour les matricules de 2010 à aujourd'hui
for annee in range (10000, 18000):
    print(annee)
