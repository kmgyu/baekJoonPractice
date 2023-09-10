from math import ceil
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

dps = [int(input()) for _ in range(n)]
dps.sort(reverse=True)

boss = [tuple(map(int, input().split())) for _ in range(k)]

ans = 0

for c in range(m):
    time = [0]*901
    for i in boss:
        dd = ceil(i[0]/dps[c])
        for j in range(900, dd-1, -1):
            time[j] = max(time[j], time[j-dd]+i[1])
    ans += time[-1]
print(ans)
