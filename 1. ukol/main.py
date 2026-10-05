# ********************************
# Kalkulačka spropitného
#30.9. 2026
# ********************************

print("kalkulačka spropitného")     # titulní text
celkova_cena = float(input("Zadejte celkovou cenu: "))  #celková cena
spropitne = int(input("Zadejte procento spropitného: "))  # procento spropitného
pocet_lidi = int(input("Zadejte počet lidí: "))  # počet lidí

# celkova_cena = celkova_cena + celkova_cena * spropitne / 100 #vypocet uctu
# celkova_cena = celkova_cena *(1+ spropitne / 100)
celkova_cena += celkova_cena * spropitne / 100
uhradit = round(celkova_cena / pocet_lidi)  # vypocet kolik zaplatí každý

#výstup859

print(f"Celková cena {celkova_cena} dělená {pocet_lidi} je {uhradit} Kč")

