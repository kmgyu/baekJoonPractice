# 백조의 호수
import sys
from collections import deque
input = sys.stdin.readline

def swanbfs():
    global swanq, tmp_swanq
    # swan 탐색 집중, 얼음에 막히면 임시큐에 저장
    q = swanq
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not swanvisit[nx][ny]:
                if mat[nx][ny] == 'X':
                    tmp_swanq.append((nx,ny))
                else:
                    if mat[nx][ny] == 'L': return 1
                    q.append((nx, ny))
                swanvisit[nx][ny] = 1
    return 0
    
def meltbfs():
    global waterq, melter
    # 녹이기 집중
    q = waterq
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not watervisit[nx][ny]:
                if mat[nx][ny] == 'X':
                    mat[nx][ny] = '.'
                    melter.append((nx,ny))
                else:
                    q.append((nx, ny))
                watervisit[nx][ny] = 1

def solve():
    global swanq, tmp_swanq, waterq, melter
    day = 0
    while True:
        if swanbfs(): return day
        meltbfs()
        # print(*watervisit, sep='\n')
        # print(day)
        swanq = tmp_swanq
        waterq = melter
        melter = deque()
        tmp_swanq = deque()
        day += 1
    
    
    
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
r, c = map(int, input().split())

mat = []
swan = []
swanvisit = [[0] * c for _ in range(r)]
watervisit = [[0] * c for _ in range(r)]

swanq = deque()
tmp_swanq = deque()
waterq = deque()
melter = deque()

for i in range(r):
    s = input().strip()
    for j in range(c):
        if s[j] != 'X': waterq.append((i, j))
        if s[j] == 'L': swan.append((i, j))
    mat.append(list(s))

swanq.append(swan[0])
swanvisit[swan[0][0]][swan[0][1]] = 1

print(solve())