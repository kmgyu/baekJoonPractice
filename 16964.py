import sys
input = sys.stdin.readline

def info(): #그래프 입력 코드.
    n = int(input())
    graph = {i : [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    seq = list(map(int, input().split()))
    return n, graph, seq

def check_dfs(seq): #dfs 체크.
    visited = [False] * (n + 1)
    l = [{1}]
    visited[1] = True
    tmp = l.pop()
    for i in seq:
        if tmp == set():
            tmp = l.pop()
        if i not in tmp:
            return False
        tmp.remove(i)
        tset = set()
        for x in graph[i]: #tmp에 자식 노드 추가.
            if not visited[x]:
                visited[x] = True
                tset.add(x)
        if tmp != set():
            l.append(tmp)
        tmp = tset
    return True

n, graph, seq = info()
print(1 if check_dfs(seq) else 0)