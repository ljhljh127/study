from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue.popleft())
print(queue)

# 부록
# queue reverse
queue.reverse()
print(queue)

# queue to list
print(list(queue))