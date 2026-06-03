sites = ['Google', 'Wiki', 'Weibo', 'Baidu', 'Taobao']
i = 0
while i < len(sites):
    site = sites[i]
    if site == 'Weibo':
        break

    if len(site) != 4:
        i += 1
        continue

    print(f'Web: {site}')
    i += 1

print('Done')