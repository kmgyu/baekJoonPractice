from heapq import heappop, heappush
from sys import stdin
input = stdin.readline
n, h, t = map(int, input().split())
g = []
for i in range(n):
    heappush(g, -int(input()))
cnt = 0
for i in range(t):
    if g[0] == -1:break
    if g[0] > -h: break
    heappush(g, -(-heappop(g)//2))
    cnt += 1
if g[0] > -h:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(-g[0])