import sys
input = sys.stdin.readline

inf = int(1e9)
t = int(input())
for k in range(t):
    n, m, w = map(int, input().split())

    dist = [inf] * (n+1)
    dist[1] = 0
    edges = []
    for i in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for i in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    a = False
    for i in range(1, n+1):
        for j in edges:
            if dist[j[1]] > dist[j[0]] + j[2]:
                dist[j[1]] = dist[j[0]] + j[2]
                if i == n-1:
                    a = True
    print("YES") if a else print("NO")
