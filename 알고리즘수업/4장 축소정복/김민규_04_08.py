# topology sort O(v+e)
def topology_sort(graph):
    print('topology sort!!!')
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
    topology_sort(graph)