action = {"type": "save", "filename": "test.txt", "data": "hello"}

match action:
    case {"type": "save", "filename": name, "data": content}:
        print(f"Saving {content} to {name}")
    case {"type": "load", "filename": name}:
        print(f"Loading {name}")