import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
v = sorted(map(int, input().split()))
m = []
for i in range(n-1):
    m.append(v[i+1]-v[i])

ans = int(2e9)+1
q = []
if n-k-2 > 0: q.append(min(m[:n-k-2]))
for i in range(k+1):
    if i>0 and q[0] == m[i-1]:heappop(q)
    while q and m[i+(n-k-2)] < q[0]:
        heappop(q)
    heappush(q, m[i+(n-k-2)])
    ans = min(q[0] + v[i+(n-k-1)] - v[i], ans)
print(ans)


