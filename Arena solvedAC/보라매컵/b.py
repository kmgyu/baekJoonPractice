import sys
input = sys.stdin.readline
n,m,p = map(int, input().split())
s = [sorted(map(int, input().split())) for _ in range(n)]

item = 0
for head in s:
    for floor in head:
        if floor == -1:
            item += 1
        elif floor <= p: p += floor
        else:
            if item:
                while item and floor > p:
                    p*=2
                    item -= 1
            if floor <= p: p+= floor
            else:
                print(0)
                exit()
    if item:
        p*=2*item
        item=0
print(1)