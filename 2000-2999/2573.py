from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline


mx = [1, -1, 0, 0]
my = [0, 0, -1, 1]

def bfs(s1, s2, cnt, visited):
    q = deque()
    q.append((s1, s2))
    visited[s1][s2] = cnt
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            cx, cy = x+mx[i], y+my[i]
            if cx < 0 or cx > N or cy < 0 or cy > M or visited[cx][cy]: continue
            if mat[cx][cy] <= 0: continue
            visited[cx][cy]=cnt
            q.append((cx, cy))
    
    return cnt+1

def minus(mat):
    temp = deepcopy(mat)
    for i in range(N):
        for j in range(M):
            if mat[i][j] > 0:
                for k in range(4):
                    cx, cy = i+mx[k], j+my[k]
                    if cx < 0 or cx > N or cy < 0 or cy > M or mat[cx][cy]: continue
                    temp[i][j] -=1
                if temp[i][j] <= 0:
                    isle.remove((i, j))
                    temp[i][j] = 0
    return temp

N, M = map(int, input().split())

mat = [[*map(int, input().split())] for _ in range(N)]

isle = set()

for i in range(N):
    for j in range(M):
        if mat[i][j]: isle.add((i, j))

t=1
while isle:
    mat = minus(mat)
    
    visited = [[0]*M for _ in range(N)]
    cnt = 1
    for current in isle:
        x, y = current
        if visited[x][y] or not mat[x][y]: continue
        cnt = bfs(x, y, cnt, visited)
    
    if cnt > 2:
        print(t)
        break
    t+=1
    
if not isle:
    print(0)
