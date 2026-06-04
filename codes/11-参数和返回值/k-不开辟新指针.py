aa = [10, 20]
bb = aa
print(f'aa={aa}->{id(aa)}, bb={bb}->{id(bb)}')

aa.append(30)
print(f'aa={aa}->{id(aa)}, bb={bb}->{id(bb)}')
