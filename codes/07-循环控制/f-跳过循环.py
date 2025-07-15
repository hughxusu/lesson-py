sites = ['Google', 'Wiki', 'Weibo', 'Runoob', 'Baidu', 'Taobao']
i = 0
while i < len(sites):
    site = sites[i]
    if site == 'Runoob':
        break
    if len(site) == 4:
        i += 1
        continue
    print(site)
    i += 1