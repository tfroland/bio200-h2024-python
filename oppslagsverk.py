# -*- coding: utf-8 -*-
"""
Oppslagsverk for prosedyrer
"""

# Opprett en dictionary/ordbok som inneholder fem prosedyrer. 
# Nøkkelverdien er navnet på prosedyren og verdien er en kort 
# beskrivelse av den. Her velger dere prosedyrer dere har lært i studiet.
prosedyrer = {
    "Venøs blodprøvetaking": "Tar blod fra vene.",
    "Kapillær blodprøvetaking": "Tar blod fra kapillær.",
    "Hemoglobinmåling": "Måler hemoglobinnivå i blod."
}

while True:
    # Bruker blir bedt om å oppgi navn på prosedyren.
    prosedyrenavn = input("Hvilken prosedyre vil du lese om? ")
    
    # Det skal sjekkes om den finnes i ordboken (datastrukturen).
    if(prosedyrenavn in prosedyrer):
        # Om den finnes skal bruker få printet ut beskrivelsen.
        print(prosedyrer[prosedyrenavn])
    else:
        # Finnes den ikke, vil bruker bli bedt om å oppgi en beskrivelse
        prosedyrebeskrivelse = input("Beskriv prosedyren: ")
        
        # Så skal prosedyren bli lagt til i ordboken og vil nå være en 
        # del av oppslagsverket. Den nye prosedyren skal være søkbar i ordboken.
        prosedyrer[prosedyrenavn] = prosedyrebeskrivelse
    
    # Bruker skal bli spurt om de har lyst til å søke opp en prosedyre 
    # i oppslagsverket. 
    fortsette = input("Ønsker du å fortsette? (ja/nei)")
    
    # Dersom de ønsker det, fortsetter programmet, 
    # ellers vil det bli avsluttet. Dette gjøres ved å ha programmet 
    # innkapslet i en while-løkke (se "ja/nei"-eksempelet).
    if (fortsette == "ja"):
        print("Programmet fortsetter.")
    elif (fortsette == "nei"):
        print("Programmet avsluttes.")
        break
    else:
        print("Ukjent kommando.")
