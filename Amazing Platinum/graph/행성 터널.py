import sys
input = sys.stdin.readline

def find(n):
    if n != node[n]:
        node[n] = find(node[n])
        return node[n]
    return n

def union(a, b):
    parent = find(a)
    child = find(b)
    if parent>child: parent, child = child, parent
    if parent != child:
        node[child] = parent
        return True
    return False

n = int(input())
planets = [list(map(int, input().split())) + [i] for i in range(n)]

node = list(range(n))

edges = []
for i in range(3):
    sor = sorted(planets, key = lambda x: x[i])
    edges += [(abs(sor[j][i] - sor[j+1][i]), sor[j][3], sor[j+1][3]) for j in range(n-1)]

edges.sort()

answer = 0
for i in edges:
    if union(i[1], i[2]):
        answer += i[0]
print(answer)