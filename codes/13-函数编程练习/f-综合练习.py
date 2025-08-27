import json

f = open('1000_imdb_top.json', 'r', encoding='utf-8')
movies = json.load(f)
f.close()

# 1. 统计2000年及以后上映的电影数量。
def count_movies_after_2000(movies):
    count = 0
    for movie in movies:
        year_str = movie.get("Released_Year", "").strip()
        if year_str.isdigit():
            year = int(year_str)
            if year >= 2000:
                count += 1
    return count


# 2. 计算所有电影的平均时长（分钟），超过120分钟的电影数量，和小于120分钟的电影数量。
def analyze_runtime(movies):
    total_runtime = 0
    count = 0
    over_120 = 0
    under_120 = 0

    for movie in movies:
        runtime_str = movie.get("Runtime", "").strip()
        if runtime_str.endswith("min"):
            number_part = runtime_str.replace("min", "").strip()

            if number_part.isdigit():
                runtime = int(number_part)
                total_runtime += runtime
                count += 1

                if runtime > 120:
                    over_120 += 1
                elif runtime < 120:
                    under_120 += 1

    if count > 0:
        avg_runtime = total_runtime / count
    else:
        avg_runtime = 0

    return avg_runtime, over_120, under_120


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

# 4. 统计拍摄电影数量最多的导演，并输出该导演的电影数。
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

# 5. 统计所有电影的票房总和（Gross），并计算有票房数据的电影平均票房。
def analyze_gross(movies):
    total_gross = 0
    count = 0

    for movie in movies:
        gross_str = movie.get("Gross", None)

        if gross_str is not None and isinstance(gross_str, str):
            gross_str = gross_str.replace(",", "").strip()

            if gross_str.isdigit():  # 确保是数字
                gross = int(gross_str)
                total_gross += gross
                count += 1

    if count > 0:
        avg_gross = total_gross / count
    else:
        avg_gross = 0

    return total_gross, avg_gross


print(f'2000年以后的电影数量{count_movies_after_2000(movies)}')

avg, over_120, under_120 = analyze_runtime(movies)
print(f'平均时长{avg:.0f}，超过120分钟的电影数量{over_120}，小于120分钟的电影数量{under_120}')

count = count_movies_by_rating(movies, 8, 9)
print(f'评分在8到9之间的电影数量{count}')

max_director, max_count = most_active_director(movies)
print(f'拍摄电影数量最多的导演是{max_director}，共执导{max_count}部电影')

total_gross, avg_gross = analyze_gross(movies)
print(f'总票房{total_gross}，平均票房{avg_gross:.0f}')




