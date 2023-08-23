import sys
from math import inf
input = sys.stdin.readline

v, e = map(int, input().split())

dist = [[inf] * v for _ in range(v)]

for i in range(e):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], c)

for k in range(v):
    for i in range(v):
        if k == i: continue
        for j in range(v):
            if k == j: continue
            dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
ans = inf
for i in range(v):
    ans = min(ans, dist[i][i])
print(ans) if ans != inf else print(-1)

