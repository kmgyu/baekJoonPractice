n = int(input())
s = input()
li = []
cnt = 0
while s:
    if s[:4] == "long":
        cnt += 1
        s = s[4:]
        continue
    elif s[:4] != "long":
        if cnt > 0:
            li.append(cnt)
            cnt = 0
    s = s[1:]
if cnt > 0: li.append(cnt)
dp = [1, 1]
t = 3
if li: t = max(li)
for i in range(2, t+1): dp.append(dp[-1]+dp[-2])
ans = 1
for i in li: ans *= dp[i]
print(ans)