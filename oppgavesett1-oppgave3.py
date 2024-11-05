
"""
Lag en tekstbasert kalkulator som utfører de fire grunnleggende aritmetiske operasjonene
(addisjon, subtraksjon, multiplikasjon, og divisjon) på tall gitt fra brukeren. Be brukeren om
tre input: begge operandene og operator. La brukeren få svaret på operasjonen i konsollen.
"""

operand1 = int(input("Oppgi første operand: "))
operand2 = int(input("Oppgi første operand: "))
operator = input("Oppgi operator: ")

resultat = ""

if(operator == "+"):
    resultat = operand1 + operand2
elif(operator == "-"):
    resultat = operand1 - operand2
elif(operator == "*"):
    resultat = operand1 * operand2
elif(operator == "/"):
    while(True):
        if(operand2 == 0):
            print("Kan ikke dividere på 0, oppgi en ny operand: ")
            operand2 = int(input("Ny verdi til andre operand: "))
        else:
            resultat = operand1 / operand2
            break
else:
    print("Ukjent operator.")
    
print(resultat)