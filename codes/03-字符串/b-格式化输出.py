name = '龙傲天'
age = 18
height = 1.82
student_id = 12345678
print('你好，我是 %s，请多多关照！' % name)
print('我今年 %d 岁' % age)
print('我今年 %04d 岁' % age)
print('姓名: %s，年龄: %d，身高: %.02f 米' % (name, age, height))
print('我的学号是 %06d' % student_id)
print('百分比为: %.0f%%' % (0.35 * 100))
print('#########################')

print('姓名: {}，学号: {:07d}，身高: {:.03f} 米'.format(name, student_id, height))
print('学生 {0} - 姓名: {0}，学号: {1:07d}，身高: {2:.03f} 米'.format(name, student_id, height))
print('#########################')


print(f'姓名: {name}，学号: {student_id:07d}，身高: {height:.03f} 米')