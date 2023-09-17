from collections import deque

def move(s):
    global curr_y, curr_x
    dm = {'U':0, 'D':1, 'L':2, 'R':3}
    idx = dm[s]
    
    cx = curr_x + dx[idx]
    cy = curr_y + dy[idx]
    if cx < 0 or cx >= n or cy < 0 or cy >= n: return
    elif mat[cx][cy] != '.': return
    mat[curr_x][curr_y], mat[cx][cy] = mat[cx][cy], mat[curr_x][curr_y]
    curr_x = cx
    curr_y = cy

def charge():
    global gage
    gage += 1

def jump():
    global gage, color
    q = deque()
    q.append((curr_x, curr_y, 0))
    
    visited = [[False]*n for _ in range(n)]
    while q:
        cx, cy, dis = q.popleft()
        if dis >= gage: continue
        for i in range(4):
            mx = cx+dx[i]
            my = cy+dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= n: continue
            if visited[mx][my]: continue
            
            # print(cx, cy, mat[mx][my], dx[i], dy[i], dis)
            if mat[mx][my] not in ['@', '.']:
                mat[mx][my] = ink[color]
            q.append((mx, my, dis+1))
            visited[mx][my] = True
    # for i in mat:
    #     print(*i)
    # print()
    gage = 0
    color = (color + 1)%I

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


I, n, k = map(int, input().split())
ink = list(input())
mat = [list(input()) for _ in range(n)]
command = input()
curr_x = 0
curr_y = 0

gage = 0
color = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] == '@':
            curr_x = i
            curr_y = j
            break

for C in command:
    if C in ['U','D','L','R']:
        move(C)
    if C == 'j':
        charge()
    if C == 'J':
        jump()

for i in mat:
    print(*i, sep="")