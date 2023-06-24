import heapq
from sys import stdin
input = stdin.readline

heap = []
for i in range(int(input())):
    a = int(input())
    if a != 0:
        heapq.heappush(heap, a)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)