from heapq import heappush, heappushpop
import sys
input = sys.stdin.readline

n = int(input())
task = [list(map(int, input().split())) for _ in range(n)]
task.sort(key= lambda x: x[1])
heap = []
heappush(heap, task[0][2])

for i in range(1, n):
    if task[i][1] < heap[0]:
        heappush(heap, task[i][2])
    else:
        heappushpop(heap, task[i][2])
print(len(heap))
