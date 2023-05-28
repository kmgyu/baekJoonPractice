import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
pic = []
pic2 = [[] for _ in range(n)] #비어있는 n*0 2차원 배열 생성
visited = [[False]*n for _ in range(n)]
for i in range(n):
    s = input().rstrip()
    pic.append(s)
    for token in s: #pic2에 토큰 단위로 분리 및 G를 R로 통일
        if token == 'G':
            pic2[i].append('R')
        else:
            pic2[i].append(token)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(color, x, y): #normal
    visited[x][y] = True
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if mx >= n or my >= n or mx < 0 or my < 0: continue
        if pic[mx][my] == color and not visited[mx][my]:
            dfs(color, mx, my)

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]: continue
        dfs(pic[i][j], i, j)
        cnt += 1
print(cnt, end = " ")

cnt = 0
visited = [[False]*n for _ in range(n)] #visited 초기화
pic = pic2 #R과 G통일 및 pic에 pic2의 주소값 참조시킴.
for i in range(n):
    for j in range(n):
        if visited[i][j]: continue
        dfs(pic[i][j], i, j)
        cnt += 1
print(cnt)