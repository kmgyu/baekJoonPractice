s = input()
l = len(s)
ans = ''.join(sorted(s, reverse=True))
# print(ans)
for i in range(l-1):
    if i > 0 and ord(s[i]) > ord(s[0]): continue
    for j in range(i+1, l-1):
        if ord(s[j]) > ord(s[i+1]): continue
        new_s = s[i::-1] + s[j:i:-1] + s[:j:-1]
        # print(s[i::-1], s[j:i:-1], s[:j:-1])
        ans = sorted([new_s, ans])[0]
        # print(i, j)
        # print(ans)
print(ans)