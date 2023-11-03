
n = int(input())
c = [0] * (n+1)

li = list(map(int, input().split()))

for i in li:
    c[i] += 1

f = max(c)
idx = 0
for i in range(1, n+1):
    if c[i]==f and idx:
        idx = 0
        break
    if c[i] == f:
        idx = i
    
if idx: print(idx)
else: print('skipped')