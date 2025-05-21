# https://velog.io/@gmtmoney2357/%EC%9D%B4%EB%B6%84-%EB%A7%A4%EC%B9%ADBipartite-Matching

# https://www.acmicpc.net/source/82775084
# 위에건 더 빠른 코드
import sys
sys.setrecursionlimit(10**6)
input = open(0).readline
N, M = map(int, input().split())

graph = dict() # 인접 리스트 형태

for i in range(1, N+1):
    graph[i] = [*map(int, input().split())][1:]

# 직업 노드를 기준으로, 연결되는 사원
matched = [0] * (M+1) # matched node graph to jobs index i.
visited = [False] * (M+1) # jobs

def dfs(current):
    for job in graph[current]:
        if visited[job]: continue
        visited[job] = True
        # 연결되지 않았거나, matched[job]노드 재탐사시
        # 다른 경로 존재 시(visited 안겹치면서 다른 경로)
        if not matched[job] or dfs(matched[job]):
            matched[job] = current
            return True
    return False

ans = 0
# 사원을 기준으로 노드탐색
# 사원의 수 N을 넘을 수 없으므로 사원 기준 탐색하는 것이 맞다.
for i in range(1, N+1):
    visited = [False] * (M+1) # 초기화
    if dfs(i): ans += 1
print(ans)