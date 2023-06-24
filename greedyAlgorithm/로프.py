import sys
input = sys.stdin.readline
n = int(input())
r = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0
for i in range(n):
    if r[i]*(i+1) > ans:ans = r[i]*(i+1)
print(ans)