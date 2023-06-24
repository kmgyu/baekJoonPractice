from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
heap = []
for i in list(map(int, input().split())):
    heappush(heap, i)
for i in range(m):
    a = heappop(heap) + heappop(heap)
    heappush(heap, a)
    heappush(heap, a)
print(sum(heap))