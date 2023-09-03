from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
man = [[] for _ in range(11)]

for i in range(n):
    p, w = map(int, input().split())
    heappush(man[p-1], -w)
    
for t in range(k):
    for i in range(11):
        if not man[i]: continue
        s = heappop(man[i])+1
        heappush(man[i], s)
ans = 0

for i in range(11):
    if not man[i]: continue
    s = man[i][0]
    if s >= 0: continue
    ans += -s
print(ans)

