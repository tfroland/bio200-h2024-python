
"""
Skriv et program som konverterer temperatur fra Celsius til Fahrenheit og omvend
"""

while (True):
    inputtype = input("Skal du oppgi Celsius eller Fahrenheit(C/F)?")
    gradeverdi = int(input("Hvor mange grader skal konverteres (tall)?"))
    
    if(inputtype == "C"):
        # Konverterer fra Celsius til Fahrenheit
        
        #Celsius grader omregnet til fahrenheit: 
        # Man dividerer celsius graden med 5, ganger tallet med 9 og legger 32 til.
        omregnedeGrader = ((gradeverdi / 5) * 9) + 32
        print(gradeverdi, " grader Celsius er lik ", 
              omregnedeGrader, " grader Fahrenheit.")
        
    elif(inputtype == "F"):
        # Konverterer fra Fahrenheit til Celsius
        
        # Man trekker 32 fra fahrenheitgraden, 
        # dividerer tallet med 9 og ganger med 5.
        omregnedeGrader = ((gradeverdi - 32) / 9) * 5
        print(gradeverdi, " grader Fahrenheit er lik ", 
              omregnedeGrader, " grader Celsius.")
    else:
        # Håndterer ukjent input
        print("Ukjent kommando, prøv igjen.")
    
    fortsette = input("Ønsker du å beregne flere verdier?(J/N)")
    if(fortsette == "N"):
        break