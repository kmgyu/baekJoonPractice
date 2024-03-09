import sys
input = sys.stdin.readline

n = int(input())
tmp = list(map(int, input().split()))
minfloor = tmp
maxfloor = tmp
inf = float('inf')

for i in range(1, n):
    cur = list(map(int, input().split()))
    tmp = [inf, inf, inf]
    for j in range(3):
        if j-1 >=0: tmp[j] = min(tmp[j], minfloor[j-1]+cur[j])
        tmp[j] = min(tmp[j], cur[j]+minfloor[j])
        if j+1 <=2: tmp[j] = min(tmp[j], minfloor[j+1]+cur[j])
    minfloor = tmp[:]
    
    tmp = [0, 0, 0]
    for j in range(3):
        if j-1 >=0: tmp[j] = max(tmp[j], maxfloor[j-1]+cur[j])
        tmp[j] = max(tmp[j], cur[j]+maxfloor[j])
        if j+1 <=2: tmp[j] = max(tmp[j], maxfloor[j+1]+cur[j])
    maxfloor = tmp[:]
print(max(maxfloor), min(minfloor))