from load import load_data

movies = load_data()

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

total_gross, avg_gross = analyze_gross(movies)
print(f'总票房{total_gross}，平均票房{avg_gross:.0f}')




