import math

print(abs(-5), abs(7.8))
print(round(-4.212432153253125, 3))
print(pow(2, 4), 2**4)

veky = [30, 10, 28, 15]
soucet_veku = sum(veky)
print(soucet_veku)

print(min(veky))
print(max(veky))

print(min(10, 5))

for vek in veky:
    print(min(vek, 28))

print(int("11", 2))
print(float("1.245"))
print(complex(1, 1))


print(math.floor(7.8))
print(math.ceil(6.1))
print(math.sqrt(9), 9**(1/3))

print(math.exp(10))
print(math.log(22026))

print(math.e, math.pi)

rads = math.radians(90)
print(math.sin(rads))


vzdalenost = math.dist((1,1),(3, 2))
print(vzdalenost)