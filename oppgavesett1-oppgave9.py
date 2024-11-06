
"""
Skriv en for-løkke som itererer fra 1 til 100 og skriver "Fizz" 
for tall som er delelige med 3, "Buzz" for tall som er delelige 
med 5, og "FizzBuzz" for tall som er delelige med både 3 og 5.
"""

# Bruker range-funksjonen til å generere tallene fra 1 til 100.
# Baserer for-løkken på tallrekken fra range-funksjonen.
for tall in range(1, 101):
    
    # Variant 1
    tekststreng = "" # Oppretter en tom streng som vi bygger videre på.
    if(tall % 3 == 0):
        tekststreng += "Fizz" # Legger til "Fizz" i strengen om delelig på 3.
    if(tall % 5 == 0):
        tekststreng += "Buzz" # Legger til "Buzz" i strengen om delelig på 5.
    
    if(tekststreng != ""): # Vi ønsker ikke å skrive ut dersom tekstrengen er tom.
        print(tekststreng)
        
    """
    # Variant 2
    if(tall % 3 == 0 and tall % 5 == 0):
        print(tall, "FizzBuzz") # Skriver ut "FizzBuzz" om delelig på både 3 og 5.
    elif(tall % 3 == 0):
        print(tall, "Fizz") # Skriver ut "Fizz" om delelig på 3.
    elif(tall % 5 == 0):
        print(tall, "Buzz") # Skriver ut "Buzz" om delelig på 5.
    """