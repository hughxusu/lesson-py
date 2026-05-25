sites = ['Google', 'Wiki', 'Weibo', 'Baidu', 'Taobao']
for site in sites:
    if site == 'Weibo':
        break

    if len(site) != 4:
        continue

    print(f'Hello, {site}')

print('Done')