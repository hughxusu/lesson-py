sites = ['Google', 'Wiki', 'Weibo', 'Baidu', 'Taobao']
for site in sites:
    if len(site) != 4:
        continue
    if site == 'Weibo':
        break
    print(f'Hello, {site}')
else:
    print('正常循环结束')