import sys
from heapq import heappush, heappop
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    minQ, maxQ = [], []
    deleted = [True] * k
    for i in range(k):
        com, n = input().split()
        n = int(n)
        if com == 'I':
            heappush(minQ, (n, i))
            heappush(maxQ, (-n, i))
            deleted[i] = False
        else:
            if n == 1:
                while maxQ and deleted[maxQ[0][1]]:
                    heappop(maxQ)
                if maxQ:
                    deleted[maxQ[0][1]] = True
                    heappop(maxQ)
            else:
                while minQ and deleted[minQ[0][1]]:
                    heappop(minQ)
                if minQ:
                    deleted[minQ[0][1]] = True
                    heappop(minQ)
        while minQ and deleted[minQ[0][1]]:
            heappop(minQ)
        while maxQ and deleted[maxQ[0][1]]:
            heappop(maxQ)
    if minQ and maxQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')