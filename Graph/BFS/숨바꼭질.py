from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        c = q.popleft() #current
        if c == k:
            return visited[c] - 1
        for i in (c-1, c+1, 2*c): #잘보면 range 아님 ㅋㅋㅋㅋㅋㅋㅋㅋ
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[c] + 1
                q.append(i)

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
print(bfs(n))