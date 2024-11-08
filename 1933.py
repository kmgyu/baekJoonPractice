import sys
from heapq import heappop, heappush

input = sys.stdin.readline 

n = int(input())
buildings = []
for _ in range(n):
    heappush(buildings, list(map(int, input().split())))

stack = []
end = 0
while buildings:
    l,h,r = heappop(buildings)
    if l >= end:
        if l > end:
            stack.append((end,0))
            stack.append((l,h))
        else:
            if h != stack[-1][1]:
                stack.append((l,h))
        end = r
        continue
    if h <= stack[-1][1]:
        if r > end:
            heappush(buildings,[end,h,r])
        continue
    if end > r:
        heappush(buildings,[r,stack[-1][1],end])
    if l == stack[-1][0]:
        stack.pop()
    stack.append((l,h))
    end = r
stack.append((end,0))
for i in range(1,len(stack)):
    print(*stack[i],end=" ")
