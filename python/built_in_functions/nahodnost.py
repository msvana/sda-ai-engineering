import random

print(random.random())
print(random.randint(1, 6))

jmena = ["Miloš", "Jirka", "Robin", "Natalie"]
print(random.choice(jmena))

print(random.gauss(100, 20))
print(random.uniform(10, 20))

random.shuffle(jmena)
print(jmena)

nahodna_jmena = random.sample(jmena, 2)
print(nahodna_jmena)