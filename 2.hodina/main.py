# příkaz větvení
x = -5
a = x

if x > 0:
    print ("kladné")
else:
    if (x<0):
        print("záporné")
        a = -x
    else:
        print("nula")    
# sem směřují skoky ze všech větví příkazu if

print(f"Absolutní hodnota čísla {x} je {a}")

if x>0:
    print("kladné")
elif x<0:
    print("záporné")
    a = -x
else:
    print("nula")


cislo = -50
kladne_cislo = cislo > 0
print(kladne_cislo)