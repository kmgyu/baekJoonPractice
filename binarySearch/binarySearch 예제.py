def binary_search(array, target, start, end):
    if start> end:
        return None
    mid = (start+end) //2
    # 왜 start가 end보다 커질까...

    #값 찾았다.
    if array[mid] == target:
        return mid
    # 원하는 값이 중간점보다 작을 때
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    #원하는 값이 중간점보다 클 때
    else:
        return binary_search(array, target, mid+1, end)

#숫자 카드의 다른사람꺼 솔루션.
# from bisect import bisect_left, bisect_right
# from sys import stdin, stdout
# bisect는 파이썬의 이진탐색모듈이다. 이것말고도 여러개있음.
# https://hongcoding.tistory.com/12 이거 참고
# input = stdin.readline
# print = stdout.write
# n = int(input())
# n_li = list(input().split())
# m = int(input())
# m_li = list(input().split())
# n_li.sort()

# for i in m_li:
#     right = bisect_right(n_li, i)
#     left = bisect_left(n_li, i)
#     print(str(right - left) + " ")
# print("\n")