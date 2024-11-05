
"""
Skriv en funksjon `isEven(n)` som returnerer `true` dersom 
`n` er et partall, og `false` ellers.
"""


def erPartall(tall):
    if(tall % 2 == 0):
        print(tall, "er et partall.")
    else:
        print(tall, "er et oddetall.")
    
erPartall(12)
erPartall(133)
erPartall(2444)

