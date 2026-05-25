try:
    f = open('todolist.pkl', 'rb')
except FileNotFoundError:
    print('File not found!')