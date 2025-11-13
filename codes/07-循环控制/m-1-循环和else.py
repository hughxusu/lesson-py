sites = ['Google', 'Wiki', 'Weibo', 'Baidu', 'Taobao']
for site in sites:
    if site == 'Weibo':
        break
    if len(site) != 4:
        continue
    print(f'Hello, {site}')
else:
    print('正常循环结束')