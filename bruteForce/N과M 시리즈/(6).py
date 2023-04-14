from itertools import combinations
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
for i in combinations(num, m):
    print(*i)