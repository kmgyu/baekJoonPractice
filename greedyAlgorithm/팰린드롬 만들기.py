from collections import Counter
n = sorted(input())
s = Counter(n)
pell = ""
cnt = -1
for k,v in s.items():
    pell += k * (v//2)
    s[k] -= (v//2)*2
    if s[k]%2 == 1 and cnt == -1:
        cnt = k
    elif s[k]%2 == 1 and cnt != -1:
        print("I'm Sorry Hansoo")
        exit()
if cnt != -1:
    pell += cnt + pell[::-1]
else:
    pell += pell[::-1]
print(pell)
