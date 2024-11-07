
"""
Dette er et program som beregner anion-gapet.
"""

# Definer en funksjon som tar inn nivåene av natrium, 
# klor og bikarbonat som argumenter, med andre ord blir de definert
# som parametre, og returnerer anion-gapet.
def aniongap(natrium, klor, bikarbonat):
    return natrium - (klor + bikarbonat)
    

# La brukeren få spesifisere verdiene til natrium, klor og bikarbonat. 
# Dette skal skje i main-funksjonen.
def main():
    natrium = int(input("Hva er natriumverdien? "))
    klor = int(input("Hva er klorverdien? "))
    bikarbonat = int(input("Hva er bikarbonatverdien? "))
    ag = aniongap(natrium, klor, bikarbonat)

    # Skriver ut en passende melding for resultatet.
    if (ag < 12):
        print("Anion gap er " + str(ag) + ", som er lavere enn normalverdi."
              + " Utredning anbefales.")
    elif (ag <= 16):
        print("Anion gap er " + str(ag) + ", som er innenfor normalen.")
    else:
        print("Anion gap er " + str(ag) + ", som er høyere enn normalverdi."
              + " Utredning anbefales.")

# Tester funksjonen
main()