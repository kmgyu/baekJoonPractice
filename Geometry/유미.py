from itertools import permutations
import math

def dist(yum, i):
    dx = mans[i][0]
    dy = mans[i][1]
    return (yum[0]-dx)**2 + (yum[1]-dy)**2

yumi = list(map(int, input().split()))
mans = [list(map(int,input().split())) for _ in range(3)]
distance = 1000000
for nums in permutations(range(3), r = 3):
    yumi1 = yumi[:]
    dis = 0
    for num in nums:
        dis += math.sqrt(dist(yumi1, num))
        yumi1[0] = mans[num][0]
        yumi1[1] = mans[num][1]
    distance = min(dis, distance)

print(int(distance))
