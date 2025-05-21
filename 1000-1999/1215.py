# https://dhdroid.github.io/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/2020/01/03/boj-1215.html
# 이게 뭔데 쒸잇팔ㅋㅋㅋㅋㅋ

n, k = map(int, input().split())

ans = 0
if n>k:
    ans += k*(n-k)

m = int(k**0.5)+1
for i in range(1, m):
    l = min(k//i, n)
    r = k//(i+1) + 1
    if l<r : continue
    ans += k*(l-r+1) - (l+r)*(l-r+1)*i//2

for i in range(1, min(k//m, n)+1):
    ans += k%i

print(ans)