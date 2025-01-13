def obvod_kruhu(polomer):
    # o = 2 * pi * polomer
    pi = 3.14159
    obvod = 2 * pi * polomer
    return obvod

o = obvod_kruhu(5)

print(obvod_kruhu(3))

def analyzuj_kruh(polomer):
    obvod = obvod_kruhu(polomer)
    obsah = 3.14159 * polomer**2
    return obvod, obsah

obv, obs = analyzuj_kruh(3)
print(f"Obvod: {obv}")
print(f"Obsah: {obs}")

vysledek = analyzuj_kruh(4)
print(vysledek[0])