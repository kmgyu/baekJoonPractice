# refer: https://m.blog.naver.com/fbfbf1/222226473643

import sys
sys.setrecursionlimit(10**6)
input = open(0).readline
N, M = map(int, input().split())

rooms = [[]] + [[*map(int, input().split())][1:] for _ in range(N)]

visited = [False]*(N+1)
matched = [0]*(M+1)

def match(worker):
    
    if visited[worker]: return False
    visited[worker] = True
    for room in rooms[worker]:
        if not matched[room]: # 매칭 안되있으면 바로 이어버리기
            matched[room] = worker
            return True
    # 바로 잇는게 불가능할 경우
    for room in rooms[worker]:
        if match(matched[room]): # matched를 위쪽 for문으로 넘겨버렸다..
            matched[room] = worker
            return True
    return False

# 왜 두번하면 되는거임...?
cnt = 0
for i in range(1, N+1):
    visited = [False]*(N+1)
    cnt += match(i)
    visited = [False]*(N+1)
    cnt += match(i)
    if cnt == M: break
print(cnt)