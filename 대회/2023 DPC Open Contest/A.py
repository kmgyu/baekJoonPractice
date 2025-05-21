p = int(input())
s = [0, 0, 0, 0]
for i in range(p):
    g, c, n = map(int, input().split())
    if g == 1:
        s[3] += 1
        continue
    if c == 1 or c == 2:
        s[0] += 1
    elif c == 3:
        s[1] += 1
    else:
        s[2] += 1
print(*s, sep="\n")