input = open(0).readline
N, t = map(int, input().split())

trees = [list(map(int, input().split())) for _ in range(N)]
trees.sort()

ans = 0
shadow = trees[0][1]
for i in range(1, N):
    shadow -= (trees[i][0]-trees[i-1][0])*t
    ans += min(shadow, trees[i][1])
    shadow = max(shadow, trees[i][1])
print(ans)