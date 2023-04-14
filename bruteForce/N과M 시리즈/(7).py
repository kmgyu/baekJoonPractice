from itertools import product
n, m = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
for i in product(num, repeat = m):
    print(*i)