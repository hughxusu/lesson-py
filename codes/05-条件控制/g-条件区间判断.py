score = 90

if score >= 90:
    print('成绩优秀')
elif score >= 80: # 这里隐含了 score < 90 and score >= 80 的判断条件
    print('成绩良好')
elif score >= 60:
    print('成绩及格')
else:
    print('成绩不及格')