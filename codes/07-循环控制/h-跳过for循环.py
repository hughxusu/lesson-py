sites = ['Google', 'Wiki', 'Weibo', 'Runoob', 'Baidu']
for site in sites:

    if len(site) != 4:
        continue

    print(f'Hello, {site}')

    if site == 'Runoob':
        break

print('Done')