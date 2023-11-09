import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
ceil = max(a)
ans = 0
for i in range(1, n):
    tmp = a[i]
    if tmp > a[i-1]:
        ans += tmp-a[i-1]
ans+=ceil-a[n-1]
print(ans)