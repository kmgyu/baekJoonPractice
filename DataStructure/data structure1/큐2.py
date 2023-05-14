from collections import deque
from sys import stdin
input = stdin.readline
q = deque()
for i in range(int(input())):
    inter = list(input().split())
    if inter[0] == 'push':
        q.append(inter[1])
    elif inter[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif inter[0] == 'size':
        print(len(q))
    elif inter[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif inter[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif inter[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
