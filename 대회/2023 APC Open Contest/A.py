n = int(input())
k = 0
cnt = 0
while k < n:
    k += 1
    if k == n:break
    if '50' in str(k): cnt += 1
print(k+cnt)