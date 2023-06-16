import sys
input = sys.stdin.readline
n,m=map(int, input().split())
a=set([input() for _ in range(n)])
print(sum([1 for _ in range(m) if input() in a]))