from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n = int(input())
for i in range(n):
    r, e, c = map(int, input().split())
    if r < e-c:
        print("advertise\n")
    elif r == e-c:
        print("does not matter\n")
    else:
        print("do not advertise\n")