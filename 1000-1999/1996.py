from sys import stdin
input = stdin.readline
n = int(input())
map_ = []
for i in range(n):
    map_.append(list(input().rstrip()))

result = [[0]*n for _ in range(n)]
dx = [-1,0,1]
dy = [-1,0,1]
for i in range(n):
    for j in range(n):
        if map_[i][j] != ".":
            for a in dx:
                for b in dy:
                    if a == 0 and b == 0: result[i][j] = "*"
                    if i+a < 0 or j+b <0 or i+a >= n or j+b >= n: continue
                    if result[i+a][j+b] != "*" and result[i+a][j+b] != "M":
                        result[i+a][j+b] += int(map_[i][j])
                        if result[i+a][j+b] >= 10: result[i+a][j+b] = "M"
for i in result:
    print(*i, sep="")