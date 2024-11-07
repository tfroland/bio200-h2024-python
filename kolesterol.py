# -*- coding: utf-8 -*-
"""
Dette er et program for analysering av kolesterolverdier.
"""
import random

# Lag en tilfeldig samling med 100 kolesterolverdier med gjennomsnitt 5.0 mmol/dL
# og standard deviasjon 1.0 mmol/dL. Dette skal dere gjøre ved hjelp av random.normalvariate 
# (modulen normalvariate i pakken/biblioteket random)

kolesterolverdier = []

for indeks in range(100):
    kolesterolverdier.append(random.normalvariate(5.0, 1.0))
    
# Gå gjennom alle verdiene og tell opp hvor mange som er i hver kategori og 
# lagre de i en liste.

# Liste over, henholdsvis, tilfredsstillende, lett forhøyede, 
# moderat forhøyede og klart forhøyede verdier
kategoriserteVerdier = [[0, "tilfredsstillende"], [0, "lett forhøyede"], 
                        [0, "moderat forhøyede"], [0, "klart forhøyede"]]

# Kategoriserer verdiene og oppdaterer listen over verdier
for element in kolesterolverdier:
    if (element < 5.0): # Tilfredsstillende
        kategoriserteVerdier[0][0] += 1
    elif (element < 6.4): # Lett forhøyet
        kategoriserteVerdier[1][0] += 1
    elif (element < 7.0): # Moderat forhøyet
        kategoriserteVerdier[2][0] += 1
    else: # Klart forhøyet
        kategoriserteVerdier[3][0] += 1
        

"""
kategoriserteVerdier = []

tilfredsstillende = 0
lettForhoyet = 0
moderatForhoyet = 0
klartForhoyet = 0

for element in kolesterolverdier:
    if (element < 5.0):
        tilfredsstillende += 1
    elif (element < 6.4):
        lettForhoyet += 1
    elif (element < 7.0):
        moderatForhoyet += 1
    else:
        klartForhoyet += 1
        
kategoriserteVerdier.append(tilfredsstillende)
kategoriserteVerdier.append(lettForhoyet)
kategoriserteVerdier.append(moderatForhoyet)
kategoriserteVerdier.append(klartForhoyet)
"""


# Skriv ut resultatene på en oversiktlig måte.
#for kategori in kategoriserteVerdier:
for kategori in kategoriserteVerdier:
    print("Det er", kategori[0], "pasienter med", kategori[1], "kolesterolverdier.")