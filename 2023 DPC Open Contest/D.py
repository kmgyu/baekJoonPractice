from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    visited = [[0] * w for _ in range(h)]
    q = deque()
    q.append((x,y))
    
    while q:
        a, b = q.pop()
        for i in range(4):
            cx = a + dx[i]
            cy = b + dy[i]
            
            if cx < 0 or cy < 0 or cx >= h or cy >= w: continue
            
            if board[cx][cy] == 2 and visited[a][b] <= 14:
                return True
            
            if visited[cx][cy] == 0 and board[cx][cy] == 1:
                if cx == x and cy == y: continue
                visited[cx][cy] += visited[a][b]+1
                q.append((cx, cy))
            elif visited[cx][cy] > visited[a][b] + 1:
                visited[cx][cy] = visited[a][b] + 1
                q.append((cx,cy))
    
    return False


h, w = map(int, input().split())
board = [[0]*w for _ in range(h)]
n = int(input())

lamp = []
lamp_on = 0

for i in range(n):
    name, x, y = input().split()
    x = int(x)
    y = int(y)
    if name[9:] == "block":
        board[x][y] = 2
    elif name[9:] == "dust":
        board[x][y] = 1
    elif name[9:] == "lamp":
        board[x][y] = 5
        lamp.append((x,y))

# print(*board, sep="\n")
for x, y in lamp:
    if not bfs(x,y):
        print("failed")
        exit(0)
print("success")


