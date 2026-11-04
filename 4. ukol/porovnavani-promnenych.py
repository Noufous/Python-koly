a = (input("zadej a: "))
b = (input("zadej b: "))
c = (input("zadej c: "))

if a>b:
    p=a
    a=b
    b=p
if b>c:
    p=b
    b=c
    c=p
if a>b:
    p=a
    a=b
    b=p    


print(f"{a}, {b}, {c}")