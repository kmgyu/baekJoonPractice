from itertools import permutations
#15649
# 1 <= m <= n <= 8
n, m = map(int, input().split())
num = list(range(1, n+1))
for i in permutations(num, m):
    print(*i)