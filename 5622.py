s = input()
ans = 0
for i in range(len(s)):
    if (ord(s[i])-65)//3 > 4:
        if 79 < ord(s[i]) < 84:
            ans += 8
        elif 86 < ord(s[i]):
            ans += 10
        else:
            ans += 9
    else:
        ans += (ord(s[i])-65)//3+3
print(ans)
