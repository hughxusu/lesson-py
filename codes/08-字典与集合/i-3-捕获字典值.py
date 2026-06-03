config = {"route": "/home", "method": "GET", "auth": "admin"}

match config:
    case {"route": path, **others}:
        print(f"路径是: {path}")
        print(f"其他参数: {others}")