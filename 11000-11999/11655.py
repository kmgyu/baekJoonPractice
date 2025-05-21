n = input()
a = 0
ans = []
for i in n:
    a = i
    if 65 <= ord(i) <= 90:
        a = ord(i) + 13
        a %= 90
        if a == 0:
            a += 90
        elif a < 65:
            a += 64
        a = chr(a)
    elif 97 <= ord(i) <= 122:
        a = ord(i) + 13
        a %= 122
        if a == 0:
            a += 122
        elif a < 97:
            a += 96
        a = chr(a)
    ans.append(a)
print(*ans, sep="")