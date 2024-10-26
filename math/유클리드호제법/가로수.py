from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
tree = sorted([int(input()) for _ in range(n)])
dist = [tree[i]-tree[i-1] for i in range(1, n)]
print(sum(dist)//gcd(*dist)-n+1)