import sys
input = sys.stdin.readline

n,m = map(int, input().split())
mat = [input() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
cnt = 0

for a in range(n):
    for b in range(m):
        if a-1>=0 and mat[a][b] == mat[a-1][b] == '|': continue
        if b-1>=0 and mat[a][b] == mat[a][b-1] == '-': continue
        cnt+=1
print(cnt)