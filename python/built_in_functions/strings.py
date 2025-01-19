tweets = [
    "  Právě jsem zjistil, že mám v   lednici jen jednu papriku a tři citrony. Co s tím udělat k večeři?  ",
    "ranní káva chutná o tolik lépe,  když víte, že nemusíte nikam spěchat.",
    "Proč pokaždé, když hledám něco důležitého, najdu jen věci, které jsem ztratil před měsícem?  ",
    " V tramvaji se mi podařilo chytnout místo u okna. Drobné radosti jsou někdy ty nejlepší.",
    "  Čtu knihu,  která mě měla bavit, ale místo toho přemýšlím, co si dám k obědu."
]

tweet = tweets[0]

"""
print(tweet.upper())
print(tweet.lower())
print(tweets[1].capitalize())

pozice_tri = tweet.find("trojka")
print(pozice_tri)

if "?" in tweet:
    print("tohle je otazka")

novy_tweet = tweet.replace("tři", "3")
print(tweet)
print(novy_tweet)

cislo_jako_text = str(12345)
pocet_cifer = len(cislo_jako_text)
print(pocet_cifer)

print(tweet.strip())

tweet_bez_carek = tweet.replace(",", "").replace("?", "").replace(".", "").lower()
slova = tweet_bez_carek.split(" ")
print(slova)

je_otazka = tweet.strip().endswith("?")
if je_otazka:
    print("Ano, je to otazka")

vek_lidi = [24, 28, 15, 30]
vek_lidi_spojeny = ",".join(map(str, vek_lidi))
print(vek_lidi_spojeny)

jmeno = "Franta"
veta = f"{jmeno} je super"

sablona = "{jmeno} je super, vek: {vek}"
vyplnena_sablona = sablona.format(jmeno="Anicka", vek=30)
print(sablona)
print(vyplnena_sablona)
"""
