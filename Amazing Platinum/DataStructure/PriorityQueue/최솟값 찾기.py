import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, l = map(int, input().split())
nums = list(map(int, input().split()))
heap = []
for i in range(n):
    # 최솟값을 기준으로 힙푸시
    heappush(heap, (nums[i], i))
    # 인덱스 범위가 충족될 때 까지 팝
    while heap and heap[0][1] < i - l + 1:
        heappop(heap)
    # 최솟값 출력
    print(heap[0][0], end=' ')

