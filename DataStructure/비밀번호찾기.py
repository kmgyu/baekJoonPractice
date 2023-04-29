from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
pswd = dict()
for i in range(n):
    a, b = input().split()
    pswd[a] = b
for i in range(m):
    print(pswd[input().rstrip()])