from sys import stdin, stdout
input = stdin.readline
print = stdout.write

k = list(map(str, input().rstrip()))
k2 = list()
for i in range(int(input())):
    q = list(input().split())
    cur = len(k)-1
    if q[0] == "L":
        if k:
            k2.append(k.pop())
    elif q[0] == "D":
        if k2:
            k.append(k2.pop())
    elif q[0] == "B":
        if k:
            k.pop()
    else:
        k.append(q[1])
k.extend(reversed(k2))
print("".join(k))

