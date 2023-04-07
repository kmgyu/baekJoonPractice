import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
coor = list()
for i in range(N):
    coor.append(list(map(int, input().split())))

coor.sort()
for i in range(N):
    print(*coor[i])

# 람다? 이해가 안가용
# import sys
# num = int(sys.stdin.readline())
# xys = []
# for _ in range(num):
#     xy = list(map(int, sys.stdin.readline().split()))
#     xys.append(xy)
# for x, y in sorted(xys, key=lambda x: (x[0], x[1])):
#     print(x, y)