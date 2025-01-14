import sys
input = sys.stdin.readline

n, l = map(int, input().split())
pool = []

for i in range(n):
    start, end = map(int, input().split())
    pool.append((start, end))
pool.sort()

point = pool[0][0]
total_cnt = 0

for start, end in pool:
    if end < point: continue
    if start > point:
        point = start
    dist = end-point
    cnt = dist//l
    if dist%l != 0: cnt += 1
    point += cnt*l
    total_cnt += cnt
print(total_cnt)