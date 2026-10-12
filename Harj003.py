###################################################################### 
# Tekijä: Taina Ylikarjula
###################################################################### 
# Laskentaoperaatiot ja tulostaminen
# --- OSA 1: Laskutoimitus apumuuttujilla ---

luku = 5          # 1. Määrittele luku
luku = luku + 34  # 2. Lisää 34
luku = luku * 3   # 3. Kerro kolmella
luku = luku - 6   # 4. Vähennä kuusi

print(luku)       # Tulostaa 111


# --- OSA 2: Sama lasku ilman apumuuttujia ---

tulos = (5 + 34) * 3 - 6
print(tulos)      # Tulostaa 111


# --- OSA 3: Jakojäännös ---
# Jakojäännöksen laskentaoperaattori on Pythonissa %
# 2 menee 13sta 6 kertaa, mutta 1 jää yli

luku1 = 13
luku2 = 2

jakojaannos = luku1 % luku2
print(jakojaannos)   # Tulostaa 1
