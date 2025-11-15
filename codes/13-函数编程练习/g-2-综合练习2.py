from load import load_data

movies = load_data()


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

                if runtime >= 120:
                    over_120 += 1
                elif runtime < 120:
                    under_120 += 1

    if count > 0:
        avg_runtime = total_runtime / count
    else:
        avg_runtime = 0

    return avg_runtime, over_120, under_120

avg, over_120, under_120 = analyze_runtime(movies)
print(f'平均时长{avg:.0f}，超过120分钟的电影数量{over_120}，小于120分钟的电影数量{under_120}')





