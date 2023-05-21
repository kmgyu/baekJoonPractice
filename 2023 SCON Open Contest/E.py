from math import factorial
n = int(input())
s = input()
li = list()
cnt = 0
while s:
    if s[:4] == "long":
        cnt += 1
        s = s[4:]
        continue
    elif s[:4] != "long":
        li.append(cnt)
        cnt = 0
    s = s[1:]
if cnt > 0:
    li.append(cnt)
ans = 1
print(li)
for i in li:
    if i < 2: continue
    ans *= int(factorial(i)/(factorial(2)*factorial(i-2)))
print(ans)
