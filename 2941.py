from collections import Counter
s = input()
c = Counter(s)
ans = c['='] + c['-']
for i in range(len(s)):
    if s[i] == 'j' :
        if i-1 >=0 and s[i-1] == 'l' or s[i-1] == 'n':
            ans += 1
    elif s[i] == 'z':
        if i-1 >=0 and i+1 < len(s) and s[i-1] == 'd' and s[i+1] == '=':
            ans += 1
print(len(s) - ans)