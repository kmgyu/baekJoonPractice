n = int(input())
tree = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans = max(tree[i] - (n-i), ans)
print(ans)