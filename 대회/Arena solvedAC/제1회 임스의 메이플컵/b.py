import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
cnt = 1
j = a[0]
for i in range(n):
    if a[i] - j < 100: continue
    cnt += 1
    j = a[i]
    
print(cnt)

cnt = 1
j = b[0]
for i in range(m):
    if b[i] - j < 360: continue
    cnt += 1
    j = b[i]
print(cnt)