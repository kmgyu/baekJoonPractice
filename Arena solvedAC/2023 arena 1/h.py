import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
matrow = [0]*n
matcol = [0]*m
for i in range(q):
    s, r, v = map(int, input().split())
    r -= 1
    if s == 1: matrow[r] += v
    else: matcol[r] += v

for i in range(n):
    for j in range(m):
        print(matrow[i] + matcol[j], end =" ")
    print()