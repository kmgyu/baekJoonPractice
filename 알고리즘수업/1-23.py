from collections import deque



queue = deque()
queue.append(0)
queue.append(1)
n = int(input())
for i in range(1, n):
    a = queue.popleft()
    b = queue.popleft()
    queue.append(b)
    queue.append(a+b)
print(queue.popleft())
