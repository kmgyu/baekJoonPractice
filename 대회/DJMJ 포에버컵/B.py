def get_point(p1, p2, y_p):
    # y_position에서의 직선의 방정식 점 위치
    if p2[0] == p1[0]:
        # disivison zero
        return p2[0]
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    y1 = p1[1] - (m * p1[0])
    return (y_p - y1) / m



input = open(0).readline
W, H = map(int, input().split())
x, y = map(int, input().split())
PQ = [*map(int, input().split())] # x1 y1 x2 y2

if PQ[1] > y: print(0.0); exit(0)

# 삼각형 비율 구하여 시작점, 끝점 계산하기

AB = [0, 0, W, 0]

# print(get_point(AB[:2], (x, y), PQ[1]), \
#     get_point(AB[2:], (x, y), PQ[3]))

dist = get_point(AB[:2], (x, y), PQ[1]), get_point(AB[2:], (x, y), PQ[3])

PQ_dist = max(PQ[0], dist[0]), min(dist[1], PQ[2])
# print(dist, PQ_dist) # 10 20 0 20 2 18 3 19
dist = dist[1]-dist[0]
PQ_dist = PQ_dist[1] - PQ_dist[0]
print('%1.12f' % (max(PQ_dist/dist, 0)))