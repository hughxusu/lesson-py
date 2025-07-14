is_error = False
error_hint = '程序数据错误'
hint = '程序正常'

#        为真时的结果 if 判定条件  else 为假时的结果
result = error_hint if is_error else hint
print(result)