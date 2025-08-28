class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'Your input is {self.length}, but at least {self.min_len} is required.'

def input_password():
    pwd = input('Please input your password: ')
    if len(pwd) < 6:
        raise ShortInputError(len(pwd), 6)

try:
    input_password()
except ShortInputError as e:
    print(e)
else:
    print('Password input completed.')