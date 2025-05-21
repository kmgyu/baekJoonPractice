from bisect import bisect_left, bisect_right
from sys import stdin, stdout
#bisect는 파이썬의 이진탐색모듈이다. 이것말고도 여러개있음.
#https://hongcoding.tistory.com/12 이거 참고
input = stdin.readline
print = stdout.write
n = int(input())
n_li = list(input().split())
m = int(input())
m_li = list(input().split())
n_li.sort()

for i in m_li:
    right = bisect_right(n_li, i)
    left = bisect_left(n_li, i)
    print(str(right - left) + " ")
print("\n")