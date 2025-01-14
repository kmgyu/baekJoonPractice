from sys import stdin
input = stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    app = []
    ans = 0
    for i in range(n):
        app.append(list(map(int, input().split())))
    app.sort()
    mx = app[0][1]
    for i,j in app:
        if j <= mx: #i순으로 정렬되므로 i보다 작은게 전제가 됨.
            ans += 1 # 따라서 mx값을 갱신해줘야 된다.
            mx = j
    print(ans)