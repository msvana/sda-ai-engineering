from data import movies

strany_ctvercu = [10, 5, 3.5, 4]
obvody_ctvercu = list(map(lambda a: 4 * a, strany_ctvercu))
print(obvody_ctvercu)

movie_titles = list(map(lambda m: m["title"], movies))
print(movie_titles[:5])

tabulka = [
    [28, 178],
    [29, 165],
    [44, 181]
]

print(list(map(lambda r: r[1] / r[0], tabulka)))

obvod_obdelniku = lambda a, b: 2*a + 2*b
print(obvod_obdelniku(4, 2))

drama_movies = filter(lambda m: "Drama" in m["genres"], movies)
drama_titles = map(lambda m: m["title"], drama_movies)
print(list(drama_titles))