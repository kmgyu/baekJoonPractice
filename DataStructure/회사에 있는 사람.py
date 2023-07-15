import sys
input = sys.stdin.readline

n = int(input())
log = set()
for i in range(n):
    a, b = input().split()
    if b == 'enter': log.add(a)
    else: log.remove(a)
print(*sorted(log)[::-1], sep="\n")