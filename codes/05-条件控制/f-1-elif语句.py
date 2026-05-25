score = int(input('请输入成绩：'))
if score >= 90:
    print('成绩评级为A')
elif score >= 80:          # 这里隐含了score < 90
    print('成绩评级为B')
elif score >= 70:
    print('成绩评级为C')
elif score >= 60:
    print('成绩评级为D')
else:
    print('成绩评级为E')
