
"""
Lag en if-else struktur som sjekker om en gitt variabel `n` 
er større enn, mindre enn eller lik 0.
"""

n = int(input("Gi en tallverdi: "))

if (n > 0):
    print("Tallet er større enn 0.")
elif (n < 0):
    print("Tallet er mindre enn 0.")
else:
    print("Tallet er likt 0.")