import sys
input = sys.stdin.readline

n = int(input())
mat = [[0] * n for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j]:
            mat[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if not mat[i][j] and mat[i][k] and mat[k][j]:
                mat[i][j] = 1

for i in mat:
    print(*i)