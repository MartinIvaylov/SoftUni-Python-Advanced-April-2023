
def movie_organizer(*movies):
    genres = {}
    for movie in movies:
        name, genre = movie
        if genre not in genres:
            genres[genre] = []
        genres[genre].append(name)

    output = ''

    for genre in sorted(genres.keys(), key=lambda g: (-len(genres[g]), g)):
        names = sorted(genres[genre])
        output += f"{genre} - {len(names)}\n"
        for name in names:
            output += f"* {name}\n"



    return output


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))





