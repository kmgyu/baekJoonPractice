s = input()
lst = s.split('-')
ans = 0
for i in lst[0].split('+'):
    ans += int(i)
for i in range(1, len(lst)):
    tmp = 0
    for j in lst[i].split('+'):
        tmp += int(j)
    ans -= tmp
print(ans)