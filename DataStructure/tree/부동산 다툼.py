import sys
input = sys.stdin.readline

def find(n):
    c = n
    ans = n
    while c > 1:
        c //= 2
        if node[c]: ans = c
    if node[1]: ans = 1
    elif ans == n and not node[n]:
        node[i] = True
        ans = 0
    return ans

n, q = map(int, input().split())

node = [False] * (n+1)
duck = [int(input()) for _ in range(q)]

for i in duck: print(find(i))