n, l = map(int, input().split())
hole = sorted(list(map(int, input().split())))
ans = 0
start = hole[0]
for i in range(1, n):
    if l <= hole[i] - start:
        ans += 1
        start = hole[i]
print(ans+1)