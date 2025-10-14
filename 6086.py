# https://iknoom.tistory.com/13
# https://unorderedmap.tistory.com/6
# 최대 유량 문제와 알고리즘

import sys

input = sys.stdin.readline

h = lambda x: ord(x) - ord('A') if x <= 'Z' else ord(x) - ord('a') + 26

# 가중치 갱신 함수 F()
def make_flow(S, T, path):
    c = float('inf')
    cur = T
    while cur != S:
        c = min(c, capacity[path[cur]][cur] - flow[path[cur]][cur])
        cur = path[cur]
    cur = T
    while cur != S:
        flow[path[cur]][cur] += c
        flow[cur][path[cur]] -= c # 유량 대칭
        cur = path[cur]
    return c

def bfs(S, T):
    path = [-1] * 52
    queue = [S] # 큐에 노드 추가, 삭제는 하지 않고 계속해서 넣어주며 조회함.
    for u in queue:
        for v in adj[u]:
            if capacity[u][v] - flow[u][v] > 0 and path[v] < 0: # 미탐색, 기존 유량보다 더 강한 유량
                queue.append(v)
                path[v] = u # 경로 이어주기
                if v == T:
                    return make_flow(S, T, path) # 갱신되면 유량 가중치 갱신
    return 0

def edmonds_karp(S, T):
    max_flow = 0
    while True:
        c = bfs(S, T)
        if c > 0:
            max_flow += c
        else:
            break
    return max_flow


N = int(input())

flow = [[0] * 52 for _ in range(52)] # 유량
capacity = [[0] * 52 for _ in range(52)] # 각 네트워크 최대 수용량
adj = [[] for _ in range(52)] # 인접 리스트

for i in range(N):
    u, v, c = input().split()
    u, v, c = h(u), h(v), int(c)
    capacity[u][v] += c
    capacity[v][u] += c
    adj[u].append(v)
    adj[v].append(u)

S = h('A') # start
T = h('Z') # target
max_flow = edmonds_karp(S, T)
print(max_flow)