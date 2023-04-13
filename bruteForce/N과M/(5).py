from itertools import permutations
#15654
n, m = map(int, input().split())
num = list(map(int,input().split()))
num.sort()
for i in permutations(num, m):
    print(*i)