# topology sort O(v+e)
def topology_sort(graph):
    inDeg = {}
    for v in graph:
        inDeg[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1
    
    vlist = [] # indegree 0 vertex list
    for v in graph:
        if inDeg[v] == 0:
            vlist.append(v)
    
    while vlist:
        v = vlist.pop()
        print(v, end=' ')
        
        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u] == 0:
                vlist.append(u)

def dfs_sort(graph):
    inDeg = {}
    for v in graph:
        inDeg[v] = 0
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1
    stack = []
    result = []
    for v in graph:
        if inDeg[v] == 0:
            stack.append(v)
    while stack:
        v = stack.pop()
        if inDeg[v] == 0: result.append(v)
        print(v, end=' ')
        for u in graph[v]:
            inDeg[u] -= 1
        for u in graph[v]:
            if inDeg[u] == 0:
                stack.append(u)
    print(result)
            

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

dfs_sort(graph1)