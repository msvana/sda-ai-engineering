def greetings(name):
    return f"Ahoj {name}"

names = ["Togi", "Natalie", "Jirko", "Alesi", "Robine"]

def greet_many(names):
    greeting_full = ""
    for name in names:
        greeting_full = greeting_full + f"Ahoj {name}\n"
    return greeting_full

print(greet_many(names))



