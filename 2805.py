from sys import stdin
from collections import Counter
input = stdin.readline

n, m = map(int, input().split())
tree = Counter(map(int, input().split()))
start = 0
end = max(tree)
while start <= end:
    mid = (start + end) // 2
    cut = 0
    cut = sum((h-mid)*i for h,i in tree.items() if h>mid)
    if cut >= m:
        start = mid+1
    elif cut < m:
        end = mid-1
print(end)