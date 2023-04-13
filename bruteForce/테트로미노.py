# 14500번 테트로미노
# 돚거. 노가다다. 내가 짠 코드랑 다른점은 방향을 썼다는거정도
# 방향체크 함수 생성
# 회전, 대칭하는 함수 생성
# 제일 왼쪽에 있는 숫자를 기준으로 모든 숫자 반복문 실행하며 수들의 합 구하기

from sys import stdin

# 종이의 세로 크기와 가로 크기 입력받기
n, m = map(int, stdin.readline().rstrip().split())

# 종이에 있는 데이터 리스트 생성
data = []

# 숫자를 한 행씩 입력받기
for _ in range(n):
  data.append(list(map(int, stdin.readline().split())))

# 현재 가리키고 있는 방향
direction = 0

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 오른쪽방향으로 90도 돌기
def turn_right():
  global direction
  direction += 1
  if direction == 4:
    direction = 0

# 테트로미노를 나타내는 함수 

# 1. 4x1 모양
def get_tetro_1(nx, ny):
  global direction
  cnt1 = 0
  # 테트로미노 모양 생성
  for _ in range(4):
      # 종이에 이탈하면 0으로 초기화
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      cnt1 = 0
      return cnt1
    cnt1 += data[nx][ny]
    nx += dx[direction]
    ny += dy[direction]
  
  return cnt1

  
# 2. 2x2 모양
def get_tetro_2(nx, ny):
  cnt2 = 0
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx+1 >= n or ny+1 >= m:
    return cnt2
  cnt2 += data[nx][ny]
  cnt2 += data[nx][ny+1]
  cnt2 += data[nx+1][ny]
  cnt2 += data[nx+1][ny+1]
  return cnt2


# 3. L자모양
def get_tetro_3(nx, ny):
  global direction
  cnt3 = 0

  # 기존 모양대로 회전
  for _ in range(3):
    # 종이를 이탈하면 0으로 반환
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      cnt3 = 0
      return cnt3
    cnt3 += data[nx][ny]
    nx += dx[direction]
    ny += dy[direction]
  # 마지막 이동한 위치로 이동  
  nx -= dx[direction]
  ny -= dy[direction]
  # 이동 방향 설정
  if direction != 0:
    direction -= 1
  else:
    direction = 3
  # 이동할 좌표 설정
  nx += dx[direction]
  ny += dy[direction]
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    cnt3 = 0
    return cnt3
  # 이동하기
  cnt3 += data[nx][ny]
  return cnt3


# 3-1. L자대칭 모양
def sym_tetro_3(sym_nx, sym_ny):
  global direction
  sym_cnt3 = 0

  # 대칭모양 회전
  for _ in range(3):
    # 종이를 이탈하면 0을 반환
    if sym_nx < 0 or sym_ny < 0 or sym_nx >= n or sym_ny >= m:
      sym_cnt3 = 0
      return sym_cnt3     
    sym_cnt3 += data[sym_nx][sym_ny]
    sym_nx += dx[direction]
    sym_ny += dy[direction]
  # 마지막 이동한 위치로 이동  
  sym_nx -= dx[direction]
  sym_ny -= dy[direction]   
  # 이동 방향 설정
  if direction != 3:
    direction += 1
  else:
    direction = 0
  # 이동할 좌표 설정
  sym_nx += dx[direction]
  sym_ny += dy[direction]
  # 이동시 종이를 이탈하면 0을 반환
  if sym_nx < 0 or sym_ny < 0 or sym_nx >= n or sym_ny >= m:
    sym_cnt3 = 0
    return sym_cnt3
  # 이동하기
  sym_cnt3 += data[sym_nx][sym_ny]
  return sym_cnt3


# 4. 지그재그 모양
def get_tetro_4(nx, ny):
  global direction
  cnt4 = 0
  # 현재 위치 값 저장 
  cnt4 += data[nx][ny]
  # 이동할 좌표 설정
  nx += dx[direction]
  ny += dy[direction]
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    cnt4 = 0
    return cnt4
  # 이동하기
  cnt4 += data[nx][ny]
  # 방향 바꾸기
  if direction != 0:
    direction -= 1
  else:
    direction = 3
  # 이동할 좌표 설정
  nx += dx[direction]
  ny += dy[direction]
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    cnt4 = 0
    return cnt4
  # 이동하기
  cnt4 += data[nx][ny]
  # 방향 바꾸기
  if direction != 3:
    direction += 1
  else:
    direction = 0
  # 이동할 좌표 설정
  nx += dx[direction]
  ny += dy[direction]
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    cnt4 = 0
    return cnt4
  cnt4 += data[nx][ny]
  return cnt4

# 4-1 지그재그 대칭 모양
def sym_tetro_4(nx, ny):
  global direction
  sym_cnt4 = 0
  # 현재 위치 값 저장 
  sym_cnt4 += data[nx][ny]
  # 이동할 좌표 설정
  nx += dx[direction]
  ny += dy[direction]
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    sym_cnt4 = 0
    return sym_cnt4
  # 이동하기
  sym_cnt4 += data[nx][ny]
  # 방향 바꾸기
  if direction != 3:
    direction += 1
  else:
    direction = 0
  # 이동할 좌표 설정
  nx += dx[direction]
  ny += dy[direction]
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    sym_cnt4 = 0
    return sym_cnt4
  # 이동하기
  sym_cnt4 += data[nx][ny]
  # 방향 바꾸기
  if direction != 0:
    direction -= 1
  else:
    direction = 3
  # 이동할 좌표 설정
  nx += dx[direction]
  ny += dy[direction]
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    sym_cnt4 = 0
    return sym_cnt4
  sym_cnt4 += data[nx][ny]
  return sym_cnt4


# 5. ㅜ, ㅗ, ㅓ, ㅏ 모양
def get_tetro_5(nx,ny):
  global direction
  cnt5 = 0
  # 이동하기
  for _ in range(3):
    # 종이를 이탈하면 0을 반환
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      cnt5 = 0
      return cnt5
    cnt5 += data[nx][ny]
    nx += dx[direction]
    ny += dy[direction]
  # 가운데 위치로 이동
  for _ in range(2):
    nx -= dx[direction]
    ny -= dy[direction]
  # 방향 바꾸기
  if direction != 3:  
    direction += 1
  else:
    direction = 0
  nx += dx[direction]
  ny += dy[direction]
  # 종이를 이탈하면 0을 반환
  if nx < 0 or ny < 0 or nx >= n or ny >= m:
    cnt5 = 0
    return cnt5
  cnt5 += data[nx][ny]
  return cnt5

# 결과를 출력할 변수 생성
sum = -1e9


# 방향 북쪽으로 설정
direction = 0

# 하나의 숫자를 기준으로 테트로미노인지 확인
for i in range(n):
  for j in range(m):
    # 방향별로 돌리면서 수의 합 구하기
    for k in range(4):
      direction = k
      case1 = get_tetro_1(i, j)
      direction = k
      case2 = get_tetro_2(i, j)
      direction = k
      case3 = get_tetro_3(i, j)
      direction = k
      case3_1 = sym_tetro_3(i, j)
      direction = k
      case4 = get_tetro_4(i, j)
      direction = k
      case4_1 = sym_tetro_4(i, j)
      direction = k
      case5 = get_tetro_5(i, j)
      direction = k
      # 계산결과 중 가장 큰 테트로미노 값으로 반환
      sum = max(sum, case1, case2, case3, case3_1, case4, case4_1, case5)
      # 방향 바꾸기
      turn_right()

# 정답 출력
print(sum)