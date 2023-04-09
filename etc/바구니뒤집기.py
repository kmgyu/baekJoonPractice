n, m = map(int, input().split())
num = list(range(1, n+1))
for i in range(m):
    a, b = map(int,input().split())
    num = num[:a-1] + list(reversed(num[a-1:b])) + num[b:]
print(*num)