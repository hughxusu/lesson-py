status = int(input('请输入当前状态：'))
match status:
    case 200:
        print("Success")
    case 400 | 404 | 405: 
        print("Not found / Not allowed")
    case 500:
        print("Server error")
    case _: 
        print("Unknown status")
