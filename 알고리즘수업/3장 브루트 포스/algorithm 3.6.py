
def dfs(start, end):
    visited = set()
    length = len(vertex)
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current, end=' ')
            visited.add(current)
            index = vertex.index(current)
            for i in range(length):
                if adjMat[index][i]: stack.append(vertex[i])
        if current == end: return True
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
print('how to dfs is', dfs('A', 'B'))