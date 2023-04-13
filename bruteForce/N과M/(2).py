#15650
from itertools import combinations
n, m = map(int, input().split())
for i in combinations(list(range(1, n+1)), m):
    print(*i)