input = open(0).readline
N, t = map(int, input().split())

trees = [list(map(int, input().split())) for _ in range(N)]
trees.sort()

l_end = -float('inf')
ans = 0
for x, h in trees:
    end = x + h//t
    
    if end > l_end:
        ans += end-max(l_end, x)
        l_end = max(l_end, end)

print(ans)