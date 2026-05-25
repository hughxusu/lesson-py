from load import load_data

movies = load_data()


# 统计IMDB_Rating在某个区间内的电影数量，开始和结束是参数。
def count_movies_by_rating(movies, start, end):
    count = 0
    for movie in movies:
        rating = movie.get("IMDB_Rating", None)

        # 确保 rating 有值并且是数字
        if isinstance(rating, (int, float)):
            if start <= rating <= end:
                count += 1
    return count

count = count_movies_by_rating(movies, 8, 9)
print(f'评分在8到9之间的电影数量{count}')
