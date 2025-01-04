info = []
for i in range(3):
    info.append(list(input().split()))

ans = ""
info.sort(key=lambda x: int(x[1]))
for i in info:
    ans += i[1][-2:]
print(ans)
ans=""

info.sort(key=lambda x: -int(x[0]))
for i in info:
    ans += i[2][0]
print(ans)