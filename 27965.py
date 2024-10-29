n, k = map(int, input().split())
ans = 0
exp = 10
for i in range(1, n+1):
    if i == exp: exp*=10
    ans = (ans*exp + i) % k
print(ans)