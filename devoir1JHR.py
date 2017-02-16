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

#####

# Solution intéressante, mais il est possible de rédiger un script plus court.
# Voici l'une des propositions que j'ai présentées en classe:

for annee in range(1930,2018): # Boucle qui passe toutes les années de 1930 à 2017
	for code in range(1001,2000): # Boucle qui passe les 1000 numéros de permis possible à chaque année
	# J'imprime ensuite un assemblage fait de :
	# D'abord, je transforme les années en «string» (chaîne de caractères) et je n'en conserve que les deux derniers caractères
	# Puis je transforme aussi en «string» les nombres générés par la 2e boucle (qui va de 1000 à 1999) et je n'en conserve que les trois derniers caractères
		print(str(annee)[2:] + str(code)[1:])

#####

# Ton script est un copié-collé de celui de Véronique Sénécal. Cela a toutes les apparences d'un plagiat. Je ne dis rien pour ce devoir-ci, mais le devoir 2 devra être différent.
