
"""
Bruk en while-løkke til å skrive ut de første 10 numrene 
i Fibonacci-sekvensen.
"""
# Nummeret på tallet i Fibonacci-sekvensen som vi ønsker oss.
n = 10

# Setter opp grunntilfellene n=0 og n=1
a = 0
b = 1
print(a)
print(b)

# Genererer de n-2 neste tallene ("-2" fordi vi har to verdier som
# grunntilfeller).
indeks = 0
while indeks < n-2:
    c = a + b # Mellomlagrer verdien på det neste tallet i rekken
    print(c)
    
    # Setter de nye verdiene til tallene som neste tall i sekvensen skal basere seg på.
    a = b
    b = c
    
    indeks += 1 # Inkrementerer indeksen for å gå ett steg nærmere avslutning av while-løkken.