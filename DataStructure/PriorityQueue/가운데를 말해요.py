import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())

minq, maxq = [],[]
minl, maxl = 0,0

for i in range(n):
    num = int(input())
    heappush(minq, -num)
    minl += 1
    
    if minl - maxl > 1:
        heappush(maxq, -heappop(minq))
        minl -= 1
        maxl += 1
    elif minq and maxq and -minq[0] > maxq[0]:
        m1 = -heappop(minq)
        m2 = heappop(maxq)
        heappush(minq, -m2)
        heappush(maxq, m1)
    print(-minq[0])