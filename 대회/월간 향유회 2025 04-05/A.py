from math import sqrt

def euclidean(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

input = open(0).readline
N = int(input())
# 선으로 이어지는 형태의 그래프, 유클리드 거리는 최적화된 거리
# 도로를 하나씩 철거해가며 최소거리 갱신
# 음.... 음?
# 1번부터 N번까지의 가는 총 길이의 최솟값은 보장되지 않나?

coor = [[*map(int, input().split())] for _ in range(N)]

# summation = 0
# for i in range(N-1):
#     summation += euclidean(coor[i], coor[i+1])

print(euclidean(coor[0], coor[-1]))