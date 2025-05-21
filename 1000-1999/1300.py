n = int(input())
k = int(input())

l, r = 0, k
ans = 0
while l <= r:
    mid = (l+r)//2
    idx = 0
    for i in range(1, n+1):
        idx += min(mid//i, n)
    
    if idx >= k:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)