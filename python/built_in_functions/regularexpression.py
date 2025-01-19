import re
import strings

print(strings.tweet)

vysledek = re.sub(r"[.,?]+", "", strings.tweet)
print(vysledek)
