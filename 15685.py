# 조건 0 : 0세대 드래곤 커브 ㅡ
# 조건 1 : n세대 드래곤 커브 = n-1세대 + n-1세대를 90도
# 조건 2-1 : 생성 규칙 : 0세대 : →  1세대 : → ↑ 2세대 : → ↑(여기서부터 역순으로 뒤집기) ← ↑ 3세대 → ↑ ← ↑(여기서부터 역순으로 뒤집기) ← ↓ ← ↑
# 조건 2-2 : 방향 90도 변환 규칙 : ↑ to ← / ← to ↓ /  ↓ to → / → to ↑ (해당위치 % 4)
# 조건 3 : 시작 방향 고려  
# 조건 4 : 크기가 1x1이면서 네 꼭지점이 모두 드래곤 커브의 일부인 정사각형의 개수
# https://edder773.tistory.com/221

# 미리 방향정보만 기록 후, 지도에 그리는 방식임.
import sys
N = int(sys.stdin.readline())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = [[0]*101 for _ in range(101)] # 0 <= x <= 100
for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    board[x][y] = 1 # 시작 위치 
    curve = [d] # 조건 3 시작 방향 입력

    for _ in range(g):
        for i in range(len(curve)-1, -1, -1): # 조건 0 ~ 2-1 역순으로 90도 뒤집기 시작해야하니
            curve.append((curve[i]+1) % 4) # 조건 2-2


    for i in range(len(curve)): # 커브 방향 동안
        x, y = x + dx[curve[i]], y + dy[curve[i]]
        board[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]: # 조건 4, 사각형
            result += 1
print(result)