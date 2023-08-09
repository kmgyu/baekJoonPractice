def find(li):
    ans = inf
    for i in range(1, len(li)):
        ans = min(ans, li[i] - li[i-1])
    return ans

n = int(input()) #length
num = list(map(int, input().split()))
num.sort()

inf = int(2e9)+1

single = []
double = []
for i in range(n):
    if num[i] % 2 == 0: double.append(num[i])
    else: single.append(num[i])

d = min(find(single), find(double))
ans = inf
for i in range(1, n):
    if (num[i] - num[i-1]) % 2:
        ans = min(ans, num[i] - num[i-1])
s = ans

if d < inf: print(d, end = " ")
else: print(-1, end = " ")
if s < inf: print(s)
else: print(-1)