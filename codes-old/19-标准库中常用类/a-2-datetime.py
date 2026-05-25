from datetime import datetime

now = datetime.now()
print(f"{type(now)}")
print(f"日期是：{now.year}年{now.month}月{now.day}日")
print(f"时间是：{now.hour}时{now.minute}分{now.second}秒")

date = now.date()
print(f"date类型：{type(date)}")

time = now.time()
print(f"time类型：{type(time)}")

time_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(f"{time_str} 类型：{type(time_str)}")

date_str = "2026-03-28 14:30:00"
date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f"{date}")