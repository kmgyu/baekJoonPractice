import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A = set(map(int, input().split()))

rooms = list(map(int, input().split()))

# 대충 이분 탐색으로 매칭되는 위치 찾고 그리디 알고리즘 쓰기...?
# 역순 / 순차 탐색 한 후 순서를 지정해줘야 하나
# 애드혹은 뭐야...