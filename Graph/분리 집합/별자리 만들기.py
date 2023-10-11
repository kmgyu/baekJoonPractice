from math import sqrt
import sys
input = sys.stdin.readline

def find(n):
    if node[n] == n:
        return n
    node[n] = find(node[n])
    return node[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a>b: a, b = b, a
    if a != b: 
        node[b] = a
        return True
    return False

def euclidean(a, b):
    return sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2)

n = int(input())
node = list(range(n))

star = [list(map(float, input().split())) + [i] for i in range(n)]

edges = []
edges.extend([(euclidean(star[i], star[j]), star[i][2], star[j][2]) for i in range(n) for j in range(i+1, n)] )
edges.sort()
answer = 0
for edge in edges:
    if union(edge[1], edge[2]):
        answer += edge[0]
print(f'{answer:.2f}')