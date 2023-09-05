from math import inf
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [[inf] * n for _ in range(n)]
for i in range(n):
    mat[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    a-=1
    b-=1
    mat[a][b] = 1
    mat[b][a] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])

friend = [0]*n
for i in range(n):
    for j in range(n):
        if mat[i][j] == inf: continue
        friend[i] += mat[i][j]

print(friend.index(min(friend))+1)