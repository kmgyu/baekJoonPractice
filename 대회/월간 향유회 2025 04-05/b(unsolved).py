# 6각 타일 회전 효율적으로 하기 문제
# ㅇ느아아ㅏ아아ㅏㅏㅏ
# 그리디? 그리디? 그리디?

# 전부 0, 1, 2회 이내로 가능하다.
input = open(0).readline

def check_cnt(coor):
    # basic = [1,0] # basic vector
    # 몰라 레후 하드코딩
    cur = coor
    if cur[0] > 0:
        if cur[1] == 0 or cur[0] < cur[1]:
            cur[0] = 0 # 0이나 다름 없음 방향 같아서
    
    if cur[0] * cur[1] < 0: # 좌표 +-다름
        return 2
    else:
        if cur[0] * cur[1] != 0 and cur[0] != cur[1]:
            # 1, 1 같은 기울기가 1 아니면 무조건 방향 전환 필요
            return 2
    if cur[0] == cur[1] == 0: return 0
    return 1

Q = int(input())

current = [0, 0]
vector = [1, 0]
# cnt = 0

for _ in range(Q):
    coor = [*map(int, input().split())]
    cnt = check_cnt(coor)
    print(cnt)
