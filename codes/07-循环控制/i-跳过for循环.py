sites = ['Google', 'Wiki', 'Weibo', 'Runoob', 'Baidu']
for site in sites:
    if site == 'Runoob':
        break
    if len(site) != 4:
        continue
    print(f'hello, {site}')
print('Done')