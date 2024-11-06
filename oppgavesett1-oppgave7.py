
"""
Implementer en funksjon `karakter(skår)` som returnerer en bokstavkarakter 
(A, B, C, D, E eller F) basert på en numerisk skåringsverdi.
"""

# Ber bruker om å oppgi skår som skal omgjøres til bokstavkarakter.
skaaringsverdi = int(input("Hva er skåren?"))

# Bruker if-elif-else-struktur for å finne korrekt bokstavkarakter.
if(skaaringsverdi >= 85):
    print("A")
elif(skaaringsverdi >= 70):
    print("B")
elif(skaaringsverdi >= 60):
    print("C")
elif(skaaringsverdi >= 40):
    print("D")
elif(skaaringsverdi >= 25):
    print("E")
else:
    print("F")
    