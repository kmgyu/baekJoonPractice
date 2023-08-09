from collections import deque
import sys
def input() : return sys.stdin.readline.rstrip()

t = int(input())
n, k = map(int, input().spilt())
d = [0] + list(map(int, input().split()))
parent = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    parent[y] += 1



