from sys import stdin
input = stdin.readline

while True:
    r, c = map(int, input().split())
    if r == c == 0:break
    map_ = []
    for i in range(r):
        map_.append(list(input().rstrip()))

    result = [[0]*c for _ in range(r)]
    dx = [-1,0,1]
    dy = [-1,0,1]
    for i in range(r):
        for j in range(c):
            if map_[i][j] == "*":
                for a in dx:
                    for b in dy:
                        if a == 0 and b == 0: result[i][j] = "*"
                        if i+a < 0 or j+b <0 or i+a >= r or j+b >= c: continue
                        if result[i+a][j+b] != "*":
                            result[i+a][j+b] += 1
    for i in result:
        print(*i, sep="")
