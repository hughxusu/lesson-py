from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    try:
        file = open(path, mode)
        yield file
    except Exception as e:
        print(e)
    finally:
        print("over")
        file.close()
        
with my_open('out.txt', 'w') as f:
    f.write("hello, the simplest context manager")