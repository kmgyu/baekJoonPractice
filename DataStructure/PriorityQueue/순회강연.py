import sys
from heapq import heappush, heappop
input = sys.stdin.readline
days = list(range(0, 10001))
def find_empty(i):
    if days[i] == i:
        return i
    days[i] = find_empty(days[i])
    return days[i]

n = int(input())
heap = []
day = 0
for i in range(n):
    p, d = map(int, input().split())
    heappush(heap, (-p, d))
    day = max(d, day)

pay = [0] * (day+1)
while heap:
    p, d = heappop(heap)
    i = find_empty(d)
    if i != 0 and pay[i] == 0:
        pay[i] = -p
        days[i] -= 1
print(sum(pay))