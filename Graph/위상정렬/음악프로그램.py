import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())

node = [0] * (n+1) # level
parent = [[] for _ in range(n+1)]
node[0] = -1

orders = []
for i in range(m):
    order = list(map(int, input().split()))
    orders.append(order)

for order in orders:
    for i in range(2, order[0]+1):
        node[order[i]] += 1
        parent[order[i-1]].append(order[i])

q = deque()
for i in range(1, n+1):
    if node[i] == 0:
        q.append(i)

answer = []
while q:
    vertex = q.popleft()
    answer.append(vertex)
    for i in parent[vertex]:
        node[i] -= 1
        if node[i] == 0:
            q.append(i)
# print(parent)
# print(node)
if len(answer) != n:
    print(0)
else:
    print(*answer, sep="\n")