from collections import deque

def bfs():
    q = deque()
    q.append([scv, 0])
    memoi = dict()
    memoi[tuple(scv)] = 0 # tuple memoization
    while q:
        current, cnt = q.popleft()
        # print(current)
        if current == [0,0,0]: return cnt
        cnt += 1
        for i in range(6): # 공격의 경우의 수
            temp = current[:]
            
            for j in range(3): # 공격 순서
                temp[j] -= attack[i][j]
            for j in range(3): # 음수는 0으로 만들기
                if temp[j] < 0: temp[j] = 0
            temp.sort() #정렬
            
            if tuple(temp) in memoi and memoi[tuple(temp)] <= cnt: continue
            q.append([temp, cnt])
            memoi[tuple(temp)] = cnt

attack = [1, 3, 9], [1, 9, 3], [3, 1, 9], [3, 9, 1], [9, 1, 3], [9, 3, 1]

n = int(input())
scv = list(map(int, input().split()))
if len(scv) < 3: scv += [0]*(3-len(scv))
print(bfs())

