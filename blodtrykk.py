
"""
Dette er et program for analysering av blodtrykksverdier.
"""
# Importerer nødvendige pakker
import random
import statistics

# La brukeren spesifisere hvor mange verdier de ønsker å få generert.
antallVerdier = int(input("Hvor mange verdier ønsker du å få generert? "))

# Bruk en while-løkke for å generere det antall verdier som de ba om å få gjøre. 
# Verdiene skal bli generert ved hjelp av random.randint() og lagret i en liste. 
# Det er snakk om overtrykk, og vi ønsker verdier mellom 100 og 200.
blodtrykksmålinger = []

while antallVerdier > 0:
    blodtrykksmålinger.append(random.randint(100, 200))
    
    antallVerdier -= 1 # Dekrementerer (reduserer) verdien med 1 for å representere en gjennomkjøring.


# Lag en funksjon som tar en liste med blodtrykksmålinger som argument og returnerer gjennomsnitt og standardavvik. 
# For å returnere mer enn en verdi om gangen kan de lagres i en egen liste som returneres. 
# Her skal dere bruke statistics-pakken.
def beregnSnittOgAvvik(målinger):
    gjennomsnitt = statistics.mean(målinger)
    standardavvik = statistics.stdev(målinger)
    snittOgAvvik = [gjennomsnitt, standardavvik]
    
    return snittOgAvvik

# Skriv ut resultatet
snittOgAvvik = beregnSnittOgAvvik(blodtrykksmålinger)
print(f"Gjennomsnittet av målingene er {snittOgAvvik[0]} og standardavviket er {snittOgAvvik[1]}")



