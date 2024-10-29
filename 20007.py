from heapq import heappush, heappop
from math import inf
import sys
input = sys.stdin.readline

n, m, x, y = map(int, input().split())

home = [inf]*n
road = [[] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    road[a].append((b, c))
    road[b].append((a, c))

q = []
heappush(q, (0, y))
home[y] = 0
while q:
    edge, node = heappop(q)
    
    for k in road[node]:
        v, e = k
        if home[v] > edge + e:
            home[v] = edge + e
            heappush(q, (home[v], v))

home.sort()
blu = 0
cnt = 1
for i in home:
    if i > x:
        print(-1)
        exit()
    if blu+i*2 > x:
        cnt += 1
        blu = i*2
    else:
        blu += i*2
print(cnt)