import sys
input = sys.stdin.readline

def find(n):
    if n == node[n]:
        return n
    node[n] = find(node[n])
    return node[n]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    node = list(range(n+1))
    book = [False] * (n+1)
    info = []
    cnt = 0
    for i in range(m):
        a, b = map(int, input().split())
        info.append((a,b))
    info.sort(key = lambda x: (-x[0], -x[1]))
    
    for i in range(m):
        a, b = info[i]
        tmp = find(b)
        if tmp >= a:
            cnt += 1
            book[tmp] = True
            node[tmp] -= 1

    print(cnt)