n, b = input().split()
ans = 0
b = int(b)
for i in range(len(n)):
    if 65 <= ord(n[i]) <= 97: #문자일때
        temp = ord(n[i]) - 55
    else:
        temp = int(n[i])
    ans += temp * (b**(len(n)-i-1))
print(ans)