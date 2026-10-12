###################################################################### 
# Tekijä: Taina Ylikarjula
###################################################################### 
# Käyttäjän syötteen muuttaminen kokonaisluvuksi

# tässä visiin ei haluta että käyttäjä syöttää desimaaliluvun
# joten mennään kokonaisluvulla

# Kysytään hinnat ja muutetaan ne kokonaisluvuiksi
hinta1 = int(input("Anna tuotteen 1 hinta: "))
hinta2 = int(input("Anna tuotteen 2 hinta: "))

# Tulostetaan hinnat
print("Tuote 1 maksaa", hinta1, "e ja tuote 2 maksaa", hinta2, "e.")

# Lasketaan ja tulostetaan summa
summa = hinta1 + hinta2
print("Tuotteiden summa on", summa, "euroa.")
