from collections import deque
import sys
def input() : return sys.stdin.readline().rstrip()

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    parent = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        parent[y] += 1
    obj = int(input())
    
    
    q = deque()
    for i in range(1, n+1):
        if parent[i] == 0:
            q.append(i)
            parent[i] -= 1

    time = [0] * (n+1)
    for value in q:
        time[value] = d[value]
    while q:
        index = q.popleft()
        if index == obj: break
        
        for i in graph[index]:
            time[i] = max(time[i], time[index]+d[i])
            parent[i] -= 1
            
        for i in range(1, n+1):
            if parent[i] == 0:
                q.append(i)
                parent[i] -= 1
    print(time[obj])