n = int(input())
s = list(map(int, input().split()))
ans = 0
tmp = 0
for i in s:
    if i != 0:
        tmp += 1
    else:
        ans = max(tmp, ans)
        tmp = 0
ans = max(tmp, ans)

print(ans)