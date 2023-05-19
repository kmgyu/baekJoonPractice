#2주차 공부내용
#DFS
#행렬로 표현하는걸 인접행렬 방식
#딕셔너리로 연결관계표현하는걸 linkedlist방식

Graph = {'A' : ['B','E','G'],
         'B' : ['A','C','D'],
         'C' : ['B'],
         'D' : ['B'],
         'E' : ['A', 'F'],
         'F' : ['E'],
         'G' : ['A','H','I','J'],
         'H' : ['G'],
         'I' : ['G','K'],
         'J' : ['G'],
         'K' : ['I']}
stack = []
visited = [False]*len(Graph)

def dfs(n): #n is start node
    print(f"{n} ->", end=" ")
    for i in Graph[n]:
        if visited[ord(i)-65]: continue
        visited[ord(i)-65] = True
        dfs(i)
    return

visited[0] = True
dfs('A')