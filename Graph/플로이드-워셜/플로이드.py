import sys
from math import inf
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[inf] * (n) for _ in range(n)]
for i in range(n):
    dist[i][i] = 0


for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
for i in dist:
    for j in i:
        print(0, end=' ') if j == inf else print(j, end=' ')
    print()