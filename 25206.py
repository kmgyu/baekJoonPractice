ans = 0
temp = 0
for i in range(20):
    a, b, c = input().split()
    if c == 'P':
        continue
    d = 0
    if c[0] == 'A':
        d += 4
    elif c[0] == 'B':
        d += 3
    elif c[0] == 'C':
        d += 2
    elif c[0] == 'D':
        d += 1
    if c != 'F' and c[1] == "+":
        d += 0.5
    ans += float(b) * d
    temp += float(b)
print(ans/temp)