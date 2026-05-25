from load import load_data

movies = load_data()
def count_movies_after_2000(movies):
    count = 0
    for movie in movies:
        year_str = movie.get("Released_Year", "").strip()
        if year_str.isdigit():
            year = int(year_str)
            if year >= 2000:
                count += 1
    return count

print(f'2000年以后的电影数量{count_movies_after_2000(movies)}')





