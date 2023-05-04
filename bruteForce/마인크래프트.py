from collections import Counter
from sys import stdin
input = stdin.readline
n, m, b = map(int, input().split())
land = Counter()
for i in range(n):
    land.update(map(int, input().split()))
ans = [10e9, 0]
for h in range(min(land),max(land)+1):
    bag = b
    sec = 0
    for height, cnt in land.items():
        if height > h:
            sec += (height - h)*2 * cnt
            bag += (height - h) * cnt
        else:
            sec += (h - height) * cnt
            bag -= (h - height) * cnt
    if bag >= 0:
        if sec <= ans[0]:
            ans[0] = sec
            ans[1] = h
print(*ans)
