from sys import stdin
from heapq import heappush, heappop
input = stdin.readline
n = int(input())
ans = 0
day = dict()
heap=[]
for i in range(n):
    a, b = map(int, input().split())
    heappush(heap, (-b, a))

while heap:
    b, a = heappop(heap)
    while a > 0:
        if a not in day:break
        a -= 1
    if a < 1: continue
    ans += -b
    day[a] = True
print(ans)