# 11375와 유사한 문제
import sys
sys.setrecursionlimit(10**6)
input = open(0).readline
N, M = map(int, input().split())

rooms = dict()
for i in range(1, N+1):
    rooms[i] = list(map(int, input().split()))[1:]

visited = [False]*(M+1)
matched = [0]*(M+1)

def match(cow):
    for room in rooms[cow]:
        if not matched[room]: # 매칭 안되있으면 바로 이어버리기
            matched[room] = cow
            return True
    # 바로 잇는게 불가능할 경우에 대한 추가적인 탐색? 같은 것
    # 뭐라 말하지 으아악
    for room in rooms[cow]:
        if visited[room]: continue
        visited[room] = True
        if match(matched[room]): # matched를 위쪽 for문으로 넘겨버렸다..
            matched[room] = cow
            return True
    return False

cnt = 0
for i in range(1, N+1):
    visited = [False]*(M+1)
    cnt += match(i)
    if cnt == M: break # N과 M 교차 검증
print(cnt)