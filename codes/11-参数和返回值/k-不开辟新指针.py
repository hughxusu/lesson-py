aa = [10, 20]
bb = aa

print(f'a={aa}, b={bb}')
print(f'a_id={id(aa)}, b_id={id(bb)}')

aa.append(30)
print(f'a={aa}, b={bb}')
print(f'a_id={id(aa)}, b_id={id(bb)}')