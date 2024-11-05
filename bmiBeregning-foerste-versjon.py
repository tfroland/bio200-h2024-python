
# Ber brukeren om å oppgi vekt og høyde til en pasient.
vekt = input("Oppgi vekt til pasienten i hele kilogram: ")
hoyde = input("Oppgi høyde til pasienten i meter med to desimaler: ")

# Beregner BMI til pasienten og lagrer det i en variabel.
bmi = int(vekt) / (float(hoyde) ** 2)

# Skriver ut tolkning av BMIen til brukeren av programmet.
bmitolkning = "Ingen verdi."

if(bmi < 18.5):
    bmitolkning = "Pasienten er undervektig."
elif(bmi <= 24.9):
    bmitolkning = "Pasienten er normalvektig."
elif(bmi <= 29.9):
    bmitolkning = "Pasienten er overvektig."
elif(bmi <= 34.9):
    bmitolkning = "Pasienten er obese."
else:
    bmitolkning = "Pasienten er sykelig overvektig."
    
print(bmitolkning)