from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
n = int(input())
heap = []
ans = 0
for i in range(n):
    heappush(heap, int(input()))
for i in range(n-1):
    a = heappop(heap)
    b = heappop(heap)
    ans += a+b
    heappush(heap, a + b)
print(ans)