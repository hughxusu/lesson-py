import json

def load_data():
    f = open('1000_imdb_top.json', 'r', encoding='utf-8')
    movies = json.load(f)
    f.close()
    return movies
