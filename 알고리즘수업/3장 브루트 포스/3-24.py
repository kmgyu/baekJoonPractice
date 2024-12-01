from collections import deque

# 탐색 가능 유무만을 검사함.
# 방문한 노드를 기록하지 않음.
def dfs(current, end, visited):
    # 재귀함수를 이용한 DFS
    if current == end:
        return True
    cur_index = vertex.index(current)
    for i in range(len(vertex)):
        if adjMat[cur_index][i] and not visited[cur_index]:
            # 연결되어 있고 방문하지 않은 경우
            visited[cur_index] = True
            if dfs(vertex[i], end, visited): return True
            visited[cur_index] = False # 백트래킹
    return False # 탐색 불가

def bfs(start, end):
    q = deque()
    # 함수 내에서 방문 노드 기록
    visited = [False] * len(vertex)
    start_index = vertex.index(start)
    end_index = vertex.index(end)
    q.append(start_index)
    while q:
        current = q.popleft() # 현재 인덱스
        if current == end_index: return True
        visited[current] = True
        for i in range(len(vertex)):
            if adjMat[current][i] and not visited[i]: # 무방향 그래프이므로 adjMat[i][current]로 검사해도 상관 없다.
                # 미방문했으며 연결되어 있는 경우 큐에 추가
                q.append(i)
    return False

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

visited = [False] * len(vertex)
start = 'A'
end = 'H'
print(f"DFS from {start} to {end} : {dfs(start, end, visited)}")
print(f"BFS from {start} to {end} : {bfs(start, end)}")