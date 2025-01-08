import sys
from heapq import heappush, heappop

def input(): return sys.stdin.readline().rstrip()

def solve(W, H, mat, start, end):
    # visited에 거울 갯수 기록
    # chk에 수직 수평 방향 기록(인덱스를 이용해 i%2로 구분)
    visited[start[0]][start[1]] = 0
    q = []
    heappush(q, [0, *start])
    
    while q:
        mirror, x, y = heappop(q)
        mirror += 1
        for i in range(4):
            cx, cy = x, y
            while True:
                cx = cx + mx[i]
                cy = cy + my[i]
                if cx < 0 or cx >= H or cy < 0 or cy >= W: break
                if mat[cx][cy] == "*": break
                if visited[cx][cy] < mirror: break
                if visited[cx][cy] == mirror and chk[i%2][cx][cy]: break # 거울 갯수 같은데 방향 다르면 거울 설치해야 되서 continue
                visited[cx][cy] = mirror
                chk[i%2][cx][cy] = True
                heappush(q, [mirror, cx, cy])
    return visited[end[0]][end[1]]-1


mx, my = [0, 1, 0, -1], [1, 0, -1, 0]

W, H = map(int, input().split())
mat = []
start, end = [], []
for i in range( H):
    temp = list(input())
    for j in range(W):
        if temp[j] == 'C':
            if not start: start = [i, j]
            else: end = [i, j]
    mat.append(temp)

visited = [[float('inf') for _ in range(W)] for _ in range(H)]
chk = [[[False for _ in range(W)] for _ in range(H)] for _ in range(2)]


print(solve(W, H, mat, start, end))