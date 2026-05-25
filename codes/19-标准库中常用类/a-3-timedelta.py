from datetime import timedelta, datetime

now = datetime.now()
print(f"现在是：{now}")

future = now + timedelta(days=10)
print(f"10天后是：{future}")

past = now - timedelta(hours=5)
print(f"5小时前是：{past}")
