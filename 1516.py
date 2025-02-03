from collections import deque

input = open(0).readline
N = int(input())

time = []
level = [0] * N
parent = [[] for _ in range(N)]
for i in range(N):
    data = list(map(int, input().split()))
    time.append(data[0])
    for d in data[1:-1]:
        parent[d-1].append(i)
        level[i] += 1

answer = [0] * N
q = deque()
for i in range(N):
    if level[i] == 0:
        q.append(i)
        level[i] -= 1
        answer[i] = time[i]

while q:
    vertex = q.popleft()
    
    for i in parent[vertex]:
        answer[i] = max(answer[i], answer[vertex] + time[i])
        level[i] -= 1
        
    for p in range(N):
        if level[p] == 0:
            q.append(p)
            level[p] -= 1
    
print(*answer, sep="\n")