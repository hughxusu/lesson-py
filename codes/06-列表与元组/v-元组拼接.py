sites = ('Google', 'Runoob', 'Wiki', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
short_sites = ('Tiktok', 'Facebook')
all_sites = sites + short_sites
print(all_sites)
print(type(all_sites))

sites += short_sites
print(sites)

sites *= 2
print(sites)

