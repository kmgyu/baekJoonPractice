n, k = map(int, input().split())
nums = list(range(n))
ans = 0
mok = n
modulo = 0
while True:
    modulo = mok%k
    mok = mok//k
    if mok+modulo < k:
        ans += mok
        break
    ans += mok
    mok -= modulo
print(ans)