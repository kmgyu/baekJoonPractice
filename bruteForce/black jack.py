#2798
import sys
import random


class Pivot:
    arr = []

    def __init__(self, index, array):
        self.index = index
        self.data = array[index]
        if coor[index] == 0:
            self.index += 1
            self.data += 1
            coor[index+1] == 0
        coor[index] = 0

    def move(self, opposite=1, distance=1):
        if coor[self.index + (distance * opposite)] == 0 :
            distance = distance + 1
        self.index = self.index + (distance * opposite)
        self.data = Pivot.arr[self.index]


# pivot을 설정
# 2차 pivot을 설정
# 3번째 수에 따라 위, 아래로 나뉨.
# 3번째 수는 어떻게 해야할까? Pivot클래스?
# 3번째 수를 기준으로 limit_up, limit_down을 정한다.
# limit_down = 0, limit_up = arr[n]+arr[n-1]+arr[n-2]
# len(arr) = 3일경우 바로 그값을 출력할 수 있어야 한다.
# 카드 수 N, 합 M
# 피벗 좌표 기억시키기

input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
coor = list(range(1, 101))  # coordinate
Pivot.arr = num

pivot1 = Pivot(int(len(num)/2-0.1), num)
pivot2 = Pivot(random.randrange(int(len(num)))-1, num)

#move() 작동
print(pivot1.index, pivot1.data)
pivot1.move()
print(pivot1.index, pivot1.data)

#while True : 로 만들기.


