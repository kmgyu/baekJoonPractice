dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r1,c1,r2,c2 = map(int,input().split())
hurricane = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
total = (c2-c1+1) * (r2-r1+1)
direction = 1
x = 0
y = 0
cnt = 1
l = 1

while total > 0:
    for _ in range(2):
        for _ in range(l):
            if r1 <= x <= r2 and c1 <= y <= c2:
                hurricane[x - r1][y - c1] = cnt
                total -= 1
            x += dx[direction]
            y += dy[direction]
            cnt += 1
        direction = (direction-1) % 4
    l += 1
max_len = len(str(cnt))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(hurricane[i][j]).rjust(max_len), end=" ")
    print()
    
def spiral(x, y):
    n = max(abs(x), abs(y))
    d = abs(x - n) + abs(y - n)
    return ((2 * n - 1) ** 2 + d) if y > x else ((2 * n + 1) ** 2 - d)


# r1, c1, r2, c2 = map(int, input().split())
# l = len(str(max(spiral(r1, c1), spiral(r1, c2), spiral(r2, c1), spiral(r2, c2))))
# print(
#     "\n".join(
#         " ".join(f"%{l}d" % spiral(i, j) for j in range(c1, c2 + 1))
#         for i in range(r1, r2 + 1)
#     )
# )