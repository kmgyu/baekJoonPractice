from collections import deque
from heapq import heappush, heappop

# dijikstra 알고리즘을 이용한 풀기
# https://www.acmicpc.net/source/86181303
# 원리는 같은데 이런식으로 dp 풀이도 가능함.

N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
visited = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

movement = [(1,0), (1,1), (0, 1)] # or condition? lol
# 가로(0, 1), 대각선(0, 2), 세로(1, 2)
# bit mask : 1, 3, 2 (0, 2, 1)

def bfs():
    q = deque()
    q.append((0, 1))
    hq = [(1, 0, 1)]
    visited[0][1] = [1, 0, 0]
    masked = [[False] * N for _ in range(N)]
    
    while hq:
        # x, y = q.popleft()
        _, x, y = heappop(hq)
        
        for mx, my in movement: # 파이프 선택
            cx, cy = x+mx, y+my
            # 벽 아니고 방문 안함.
            if not ((0<=cx<N) and (0<=cy<N)): continue
            # 비트 연산을 통한 벽체크
            field_block = False
            for i in range(1,4):
                # i로부터 check bit 추출
                row = i&(mx*2) > 0
                col = i&(my) > 0
                if mat[x+row][y+col]:
                    field_block=True
            
            if field_block: continue
            
            # 비트 연산을 통해 경우의 수 더하기
            # 현재 선택한 파이프(비어있음)에 기존 파이프와 비교해서 경우의 수를 더한다.
            # 맨하탄 거리 + bfs라 순차적으로 되서 계산 시 꼬이지 않는다.
            # 혹시 몰라서 masked라고 visited 체킹 해주었는데 모르겠다.
            for i in range(3):
                if i+1 & (mx*2 + my):
                    visited[cx][cy][mx*2+my-1] += visited[x][y][i]
                    # if (cx == 3 or cx == 4) and cy == 6:
                    #     print(i, mx + my*2, i+1 & (mx*2 + my), visited[x][y], visited[cx][cy])

                # visited[cx][cy]+=visited[x][y]
            if not masked[cx][cy]:
                heappush(hq, ((cx+cy), cx, cy))
                # q.append((cx, cy))
                masked[cx][cy]=True
    
    # for line in visited:
    #     print(*line)
    return sum(visited[N-1][N-1])

if mat[N-1][N-1]: print(0)
else: print(bfs())