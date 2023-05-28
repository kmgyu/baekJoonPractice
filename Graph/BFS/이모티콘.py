from collections import deque

def bfs():
    q = deque()
    q.append([1, 0])
    
    while q:
        c, clip = q.popleft() #current
        if c == s:
            print(visited[(c, clip)])
            return
        for i in ((c, c), (c+clip, clip), (c-1, clip)):
            if i not in visited:
                visited[i] = visited[(c, clip)] + 1
                q.append(i)

visited = dict()
visited[(1, 0)] = 0
s = int(input())
bfs()