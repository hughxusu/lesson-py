from load import load_data

movies = load_data()

def most_active_director(movies):
    director_count = {}

    for movie in movies:
        director = movie.get("Director", "").strip()
        if director != "":
            if director not in director_count:
                director_count[director] = 1
            else:
                director_count[director] += 1

    max_director = ""
    max_count = 0
    for director, count in director_count.items():
        if count > max_count:
            max_director = director
            max_count = count

    return max_director, max_count

max_director, max_count = most_active_director(movies)
print(f'拍摄电影数量最多的导演是{max_director}，共执导{max_count}部电影')





