time = int(input('请输入当前时间：'))
if time > 5 and time < 8:
    print('亲，早上好！')
elif time < 12:          # 这里隐含了 time >= 8 and time < 12 的判断条件
    print('亲，上午好！') 
elif time < 13:
    print('亲，中午休息一会吧！')
elif time < 17:
    print('亲，下午好！')
elif time < 18:
    print('亲，下班了！')
elif time < 23:
    print('亲，晚上好！')
else:
    print('亲，深夜了，早点休息吧！')
