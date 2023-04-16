from collections import Counter
s = list(input().split())
cnt = 0
big = [] #대괄호 저장
for i in range(len(s)):
    if s[i] == '[' or s[i] == ']':
        cnt += 4
    else:
        try:
            int(s[i])
            cnt+=8
        except:
            cnt+=len(s[i])+12

print(cnt)