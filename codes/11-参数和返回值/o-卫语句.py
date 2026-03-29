def get_score_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:          # 这里隐含了score < 90
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'

score = int(input('请输入成绩：'))
print(f'成绩评级为{get_score_grade(score)}')
