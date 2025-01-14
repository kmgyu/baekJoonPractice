s = list(map(int, input().split()))
s.sort()
if s[-1] >= s[0]+s[1]:
    s[-1] = s[0]+s[1]-1
print(sum(s))