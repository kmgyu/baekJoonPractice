from math import gcd

def slope(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    c = gcd(x, y)
    return (x//c, y//c)

n = int(input())
coor = []
for i in range(n):
    s = input()
    for j in range(n):
        if s[j] != '.':
            coor.append((i,j))
cnt = 0
for i in range(len(coor)):
    for j in range(i+1, len(coor)):
        for k in range(j+1, len(coor)):
            s1 = slope(coor[i], coor[j])
            s2 = slope(coor[j], coor[k])
            if s1 == s2: cnt+=1
print(cnt)

