def get_greet_msg(time):
    if time > 5 and time < 8:
        return '亲，早上好！'
    elif time < 12:         
        return '亲，上午好！' 
    elif time < 13:
        return '亲，中午休息一会吧！'
    elif time < 17:
        return '亲，下午好！'
    elif time < 18:
        return '亲，下班了！'
    elif time < 23:
        return '亲，晚上好！'
    else:
        return '亲，深夜了，早点休息吧！'

time = int(input('请输入当前时间：'))
print(get_greet_msg(time))
