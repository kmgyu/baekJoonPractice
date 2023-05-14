from sys import stdin
from collections import deque
inpuut = stdin.readline
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))
    prior = sorted(doc)
    que = deque(range(n))
    cnt = 0
    while True:
        if doc[que[0]] < prior[-1]:
            que.append(que.popleft())
        else:
            cnt += 1
            prior.pop()
            if que[0] == m:
                break
            que.popleft()
    print(cnt)
