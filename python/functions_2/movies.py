from data import movies

def get_drama_movies(movie_list):
    drama_movies = []
    for movie in movie_list:
        if "Drama" in movie["genres"]:
            drama_movies.append(movie["title"])
    return drama_movies

def find_by_genre(movie_list, genre):
    drama_movies = []
    for movie in movie_list:
        if genre in movie["genres"]:
            drama_movies.append(movie["title"])
    return drama_movies

def find_by_genre_full(movie_list, genre):
    drama_movies = []
    for movie in movie_list:
        if genre in movie["genres"]:
            drama_movies.append(movie)
    return drama_movies

def get_longest_movie(movie_list):
    longest_movie = movie_list[0]

    for movie in movie_list[1:]:
        if movie["runtime"] > longest_movie["runtime"]:
            longest_movie = movie

    return longest_movie

def get_longest_movie_by_genre(movie_list, genre):
    movies_in_genre = find_by_genre_full(movie_list, genre)
    longest_movie = movies_in_genre[0]

    for movie in movies_in_genre[1:]:
        if movie["runtime"] > longest_movie["runtime"]:
            longest_movie = movie

    return longest_movie

def get_longest_movie_by_genre_2(movie_list, genre):
    longest_movie = None

    for movie in movie_list:
        if genre not in movie["genres"]:
            continue

        if longest_movie is None:
            longest_movie = movie
            continue

        if movie["runtime"] > longest_movie["runtime"]:
            longest_movie = movie

    return longest_movie

# drama_titles = get_drama_movies(movies)
# print(drama_titles)

# comedy_titles = find_by_genre(movies, "Comedy")
# print(comedy_titles[:5])

# longest_movie = get_longest_movie(movies)
# print(longest_movie)

longest_comedy = get_longest_movie_by_genre_2(movies, "Comedy")

print(longest_comedy)