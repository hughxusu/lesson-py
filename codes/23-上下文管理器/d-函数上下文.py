from contextlib import contextmanager

msg = '''
冰簟银床梦不成，
碧天如水夜云轻。
雁声远过潇湘去，
十二楼中月自明。
'''

@contextmanager
def my_open(path, mode):
    file = open(path, mode)
    print("进入上文")
    yield file
    print("进入下文")
    file.close()
        
with my_open('瑶瑟怨.txt', 'w') as f:
    f.write(msg)
