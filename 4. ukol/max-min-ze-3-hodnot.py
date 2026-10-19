a = (input("zadej a: "))
b = (input("zadej b: "))
c = (input("zadej c: "))

min = a
max = a


if b<min:
    min = b
elif b>max:
    max = b



if c<min:
    min = c
elif c>max:
    max = c

print(f"Min: {min}, Max: {max}")
