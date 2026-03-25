import share

def double():
    share.share_value *= 2
    print(f"double: {share.share_value}")

def double_list():
    share.share_list *= 2
    print(f"double_list: {share.share_list}")
