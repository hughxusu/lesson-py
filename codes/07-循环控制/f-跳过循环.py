sites = ['Google', 'Wiki', 'Weibo', 'Runoob', 'Baidu', 'Taobao']
i = 0
while i < len(sites):
    site = sites[i]

    if len(site) != 4:
        i += 1
        continue

    print(f'Hello, {site}')

    if site == 'Runoob':
        break
    i += 1

print('Done')