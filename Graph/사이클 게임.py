import sys

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

input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(range(n))

for i in range(m):
    x, y = map(int, input().rstrip().split())
    if find(x) == find(y):
        print(i+1)
        break
    union(x, y)
else: #for-else
    print(0)
    
# https://computer-science-student.tistory.com/675