
"""
Lag et program som tar et årstall som input fra brukeren, og bestemmer om det er et
skuddår eller ikke. (Tips: Et skuddår er delelig med 4, men ikke med 100, med mindre det
også er delelig med 400). Tips: sjekk opp syntaks for if-else-struktur og bruk dette.
"""

aarstall = int(input("Oppgi årstall: "))

if(aarstall % 4 == 0 and not aarstall % 100 == 0):
    print(aarstall, "er et skuddår.")
elif(aarstall % 100 == 0 and aarstall % 400 == 0):
    if (aarstall % 4 == 0):
        print(aarstall, "er et skuddår.")
    else:
        print(aarstall, "er ikke et skuddår.")
else:
    print(aarstall, "er ikke et skuddår.")
    

if(aarstall % 4 == 0):
    if (not aarstall % 100 == 0):
        print(aarstall, "er et skuddår.")
    elif(aarstall % 400 == 0):
        print(aarstall, "er et skuddår.")
    else:
        print(aarstall, "er ikke et skuddår.")
else:
    print(aarstall, "er ikke et skuddår.")