
"""
Lag en switch-case-struktur som returnerer navnet på en dag 
i uken basert på en numerisk verdi (1 for mandag, 2 for tirsdag, osv.).
"""

# Ber bruker om å oppgi hvilken dag det er i numerisk verdi.
dagtall = int(input("Hvilken dag er det? (1-7)"))

# Bruker en switch-/match-case statement som alternativ til if-elif-else
match dagtall:
    case 1:
        print("mandag")
    case 2:
        print("tirsdag")
    case 3:
        print("onsdag")
    case 4:
        print("torsdag")
    case 5:
        print("fredag")
    case 6:
        print("lørdag")
    case 7:
        print("søndag")
    case default:
        print("Ukjent dag.")