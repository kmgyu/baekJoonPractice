from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(m):
        graph[i][j] = s[j]
#A일때 1, B일때 2

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(startx, starty, currentx, currenty, length):
    for i in range(4):
        x = currentx+dx[i]
        y = currenty+dy[i]
        if x >= n or y >= m or x < 0 or y < 0:
            continue
        if length >= 3 and visited[x][y] and graph[x][y] == graph[currentx][currenty] and x == startx and y == starty:
            # print(x, y, currentx, currenty)
            print("Yes")
            exit(0)
        if not visited[x][y] and graph[x][y] == graph[currentx][currenty]:
            visited[x][y]=True
            dfs(startx,starty,x,y,length + 1)
            
visited = []
for i in range(n):
    for j in range(m):
        visited = [[False]*m for _ in range(n)]
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, i, j, 0)
print("No")