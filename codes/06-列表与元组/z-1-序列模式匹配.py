command = ["move", "10", "20"]
# command = ["drop", "sword", "shield"]

match command:
    case ["quit"]:
        print("Goodbye!")
    case ["move", x, y]:
        print(f"Moving to {x}, {y}")
    case ["drop", *items]:  # 使用 * 匹配剩余的所有元素
        print(f"Dropping: {items}")