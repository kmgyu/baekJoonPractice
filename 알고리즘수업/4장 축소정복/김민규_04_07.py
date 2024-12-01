def dfs_sort(graph):
    print('dfs sort!!!')
    inDeg = {}
    for v in graph:
        inDeg[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1
    stack = []
    # result = []
    for v in graph:
        if inDeg[v] == 0:
            stack.append(v)
    
    # 알파벳 오름차순이 우선순위기에 재귀형식으로 구현
    # 스택으로 구현 시, 스택에 넣은 순서대로 출력된다.
    def dfs(graph, v, visited):
        print(v, end=' ')
        for u in graph[v]:
            inDeg[u] -= 1
            if u not in visited and inDeg[u] == 0:
                visited.add(u)
                dfs(graph, u, visited)
    
    visited = set()
    while stack:
        v = stack.pop()
        dfs(graph, v, visited)
    # while stack:
    #     v = stack.pop()
    #     if inDeg[v] == 0: result.append(v)
    #     print(v, end=' ')
    #     for u in graph[v]:
    #         inDeg[u] -= 1
    #     for u in graph[v]:
    #         if inDeg[u] == 0:
    #             stack.append(u) # 넣는 과정에서 문제가 생긴다...
    # print(result)
            
# test driver
graph1 = {
    "A" : ["B", "D", "E"],
    "B" : ["C", "E", "F"],
    "C" : ["G"],
    "D" : ["E"],
    "E" : [],
    "F" : ["G"],
    "G" : []
}

graph2 = {
    "A" : {"B", "C"},
    "B" : {"D"},
    "C" : {"D", "E"},
    "D" : {"F"},
    "E" : {"G", "H"},
    "F" : {},
    "G" : {"H"},
    "H" : {"C"}
}

for graph in (graph1, graph2):
    dfs_sort(graph)