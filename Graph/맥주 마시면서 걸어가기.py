import sys
input = sys.stdin.readline

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

t= int(input())
for i in range(t):
    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n+2)]

    parent = list(range(n+2))

    for i in range(n+2):
        for j in range(i, n+2):
            x = p[i][0] - p[j][0]
            y = p[i][1] - p[j][1]
            if abs(x)+abs(y) <= 1000:
                union(i, j)
    if parent[0] == parent[-1]: print("happy")
    else: print("sad")