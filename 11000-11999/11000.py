import heapq
import sys
input = sys.stdin.readline

n = int(input())
task = sorted([list(map(int,input().split())) for _ in range(n)])
heap = []
heapq.heappush(heap, task[0][1])

for i in range(1,n):
    if task[i][0] < heap[0]:
        heapq.heappush(heap, task[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, task[i][1])
print(len(heap))
