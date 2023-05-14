from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
cq = deque(range(1, n+1))
cnt = 0
for i in nums:
    if cq[0] == i:
        cq.popleft()
    elif len(cq) - cq.index(i) < cq.index(i):
        while cq[0] != i:
            cq.appendleft(cq.pop())
            cnt += 1
        cq.popleft()
    else:
        while cq[0] != i:
            cq.append(cq.popleft())
            cnt += 1
        cq.popleft()
print(cnt)