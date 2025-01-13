
def pozdrav(jmeno):
    print(f"Ahoj {jmeno}")

pozdrav("Milosi")
pozdrav("Anicko")

def pozdrav_s_opakovanim(jmeno, opakovani=5):
    vynasobeny_pozdrav = f"Ahoj {jmeno}\n" * opakovani
    print(vynasobeny_pozdrav)

pozdrav_s_opakovanim("Milosi")
pozdrav_s_opakovanim("Franto")
pozdrav_s_opakovanim("Alesi")
pozdrav_s_opakovanim("Natalie")
pozdrav_s_opakovanim("Jirko", 10)

pozdrav_s_opakovanim(opakovani=3, jmeno="Franto")

print("Jirka", "Natalie", "Ales", "Milos", sep=":", end=".\n")
