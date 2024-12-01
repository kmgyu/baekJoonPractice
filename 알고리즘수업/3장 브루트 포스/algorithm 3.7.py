from collections import deque

def bfs(start, end):
    q = deque()
    visited = [False] * len(vertex)
    start_index = vertex.index(start)
    end_index = vertex.index(end)
    q.append(start_index)
    while q:
        current = q.popleft()
        print(vertex[current], end=' ')
        if current == end_index: return True
        visited[current] = True
        for i in range(len(vertex)):
            if adjMat[current][i] and not visited[i]:
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

bfs('A', 'H')