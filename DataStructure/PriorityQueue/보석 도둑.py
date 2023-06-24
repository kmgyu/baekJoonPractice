from heapq import heappush, heappop
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
gems = []
values = []
for _ in range(n):
    m, v  = map(int, input().split())
    heappush(gems, (m, v))

bags = sorted([int(input()) for _ in range(k)])

result = 0
for bag in bags:
    while gems and bag >= gems[0][0]: heappush(values, -heappop(gems)[1])
    if values: result -= heappop(values)
    elif not gems: break
print(result)
#무게로 비교해서 들어갈수 있는 것중 가장 비싼거 빼서 가져감.