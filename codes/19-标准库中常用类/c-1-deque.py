from collections import deque

deq = deque()

# 添加至队尾
deq.append(2)    
deq.append(4)

# 添加至队首
deq.appendleft(3)  
deq.appendleft(1)

for item in deq:
    print(item, end=' ')
print()

# 弹出队尾元素
print(f"弹出队尾元素: {deq.pop()}") 

# 弹出队首元素 
print(f"弹出队首元素: {deq.popleft()}")  
