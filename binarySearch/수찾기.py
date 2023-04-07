#1920 수찾기

def binary_search(array, target, start, end):
    if start> end:
        return 0
    mid = (start+end) //2
    # 왜 start가 end보다 커질까...

    #값 찾았다. index 리턴
    if array[mid] == target:
        return 1
    # 원하는 값이 중간점보다 작을 때
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    #원하는 값이 중간점보다 클 때
    else:
        return binary_search(array, target, mid+1, end)

n = int(input())
nLi = list(map(int, input().split()))
m = int(input())
mLi = list(map(int, input().split()))

# 일단 n이랑 mLi로 이진탐색 구현해보기
nLi.sort()

for i in mLi:
    print(binary_search(nLi, i, 0, len(nLi)-1))
