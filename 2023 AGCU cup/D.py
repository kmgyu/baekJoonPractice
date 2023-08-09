n = int(input())
s = list(input())
isT = False
for i in range(1, n+1):
    a = s[:i]
    b = s[-i:]
    cnt = 0
    for j in range(i):
        if a[j] != b[j]:
            cnt += 1
    if cnt == 1:
        isT = True
        break
if isT:
    print("YES")
else:
    print("NO")