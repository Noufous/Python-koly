print("Mysli si číslo od 1 do 20 a já se ho pokusím uhodnout.")

min_hodnota = 1
max_hodnota = 20
pokusy = 0

while min_hodnota <= max_hodnota:
    tip= (min_hodnota + max_hodnota) // 2
    pokusy += 1

    print(f"nMůj tip č. {pokusy} je: {tip}")
    odpoved = input("Je to správně (=), je tvé číslo větší (>) nebo menší (<)? ")

    if odpoved == "=":
        print(f"Uhodl jsem číslo {tip} na {pokusy} pokusů!")
        break
    elif odpoved == ">":
        min_hodnota = tip + 1
    elif odpoved == "<":
        max_hodnota = tip - 1
    else:
        print("Neplatná odpověď. Zadej '=', '>' nebo '<'.")
        pokusy -= 1  
else:
    print("Prohrál jsem! Zřejmě jsi mi dal špatné informace.")
    