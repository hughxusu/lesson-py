import json

f = open('1000_imdb_top.json', 'r', encoding='utf-8')
movies = json.load(f)
f.close()

print(f'Number: {len(movies)}')
print('='*50)
for key, value in movies[0].items():
    print(f'{key}: {value}')