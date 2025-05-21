n, x = map(int, input().split())
p = sum(map(int, input().split()))
print(1 if p%x == 0 else 0)