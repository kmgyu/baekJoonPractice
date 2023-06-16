from ordered_set import OrderedSet

def dfs(graph, start, visited=OrderedSet()):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)

graph = dict()
graph['A'] = OrderedSet(['B', 'C', 'D'])
graph['B'] = OrderedSet(['A', 'D'])
graph['C'] = OrderedSet(['A','D','E'])
graph['D'] = OrderedSet(['A','B','C','E'])
graph['E'] = OrderedSet(['C','D','G','H'])
graph['F'] = OrderedSet(['D','G'])
graph['G'] = OrderedSet(['E','F','H'])
graph['H'] = OrderedSet(['E', 'G'])
dfs(graph, 'A')