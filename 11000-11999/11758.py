p = [list(map(int, input().split())) for _ in range(3)]
v1 = [p[1][i] - p[0][i] for i in range(2)]
v2 = [p[2][i] - p[0][i] for i in range(2)]
det = v1[0]*v2[1] - v2[0]*v1[1]
if det > 0:print(1)
elif det == 0:print(0)
else:print(-1)