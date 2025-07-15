sites = ['Google', 'Wiki', 'Weibo', 'Runoob', 'Baidu', 'Taobao']
i = 0
while i < len(sites):
    site = sites[i]
    if len(site) == 4:
        i += 1
        continue
    if site == 'Runoob':
        break
    print(site)
    i += 1
else:
    print('循环结束')

for site in sites:
    if len(site) == 4:
        continue
    if site == 'Runoob':
        break
    print(site)
else:
    print('循环结束')