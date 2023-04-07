# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
import heapq
import sys

loop = int(input())
num = list()
for i in range(loop):
    heapq.heappush(num, int(sys.stdin.readline()))
for i in range(loop):
    print(heapq.heappop(num))

# 힙은 C나 C++로 직접 구현해보자.
# 씨봉방거
