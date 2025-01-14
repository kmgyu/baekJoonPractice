import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
l = sorted(map(int, input().split()))

l2 = sorted([l[i] - l[i-1] for i in range(1, len(l))])[n-k:]

point = l[0]
dist = 0
for i in range(1, n):
    if l[i] - l[i-1] in l2:
        l2.remove(l[i] - l[i-1])
        continue
    dist += l[i] - l[i-1]
print(dist)
