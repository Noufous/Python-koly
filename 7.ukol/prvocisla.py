print("JE ZADANÉ ČÍSLO PRVOČÍSLEM?")
CISLO=int(input("Zadejte číslo: "))

JE_PRVOCISLO=True

if CISLO<2:
    JE_PRVOCISLO=False
elif CISLO==2:
    JE_PRVOCISLO=True
elif CISLO % 2 == 0:
    JE_PRVOCISLO=False
else:
    delitel = 2
    while delitel < math.sqrt(CISLO):
        if CISLO % delitel == 0:
            JE_PRVOCISLO=False
            break
        delitel += 1

if JE_PRVOCISLO:
    print(f"Číslo {CISLO} JE prvočíslo.")
else:
    print(f"Číslo {CISLO} NENÍ prvočíslo.")