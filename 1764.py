from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
hear = set()
see = set()
for i in range(n):
    hear.add(input().rstrip())
for j in range(m):
    see.add(input().rstrip())
lo = list(hear & see)
lo.sort()
print(len(lo))
for i in lo:
    print(i)