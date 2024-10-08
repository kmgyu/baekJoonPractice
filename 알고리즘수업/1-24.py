from heapq import heappush, heappop

num = []
heap = []

for i in num:
    heappush(heap, i)
    
sorted = []
for i in range(len(heap)):
    sorted.append(heappop(heap))