#11656 접미사 배열
s = input()
ans = []
for i in range(len(s)):
    ans.append([s[i:]])
ans.sort(key=len, reverse=True)
ans.sort()
for i in ans:
    print(*i)