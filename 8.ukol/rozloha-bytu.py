def spocitej_obsah (a, b):
    if a <= 0 or b <= 0:
        return none
    obsah = a * b
    return obsah

print ("Zadejte rozměry bytu:")
pocet_mistnosti = int(input("Zadejte počet místností: "))
mistnost = 1
while mistnost <= pocet_mistnosti:
    print(f"Zadejte rozměry místnosti {mistnost}.:")
    a= int(input("Zadej rozměr \"a\": "))
    b= int(input("Zadej rozměr \"b\": "))
    obsah += spocitej_obsah(a, b)
    mistnost += 1
print(f"Celkový obsah bytu je: {obsah} ")
    