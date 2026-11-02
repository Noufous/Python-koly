import random
tajne_cislo = random.randint(1, 20)

tip=0
pokusy=0
print("Hádej číslo od 1 do 20")

while tip != tajne_cislo:
    tip = int(input("Zadej svůj tip: "))
    pokusy += 1
    if tip < tajne_cislo:
        print("Tvoje číslo je menší než tajné číslo.")
    elif tip > tajne_cislo:
        print("Tvoje číslo je větší než tajné číslo.")
    else:
        print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy} pokusů.")
    if pokusy >= 5:
        print(f"Prohrál jsi! Tajné číslo bylo {tajne_cislo}.")
        break