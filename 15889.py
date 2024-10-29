import sys
input = sys.stdin.readline
n = int(input())
mans = sorted(map(int, input().split()))
if n > 1: range_ = list(map(int, input().split()))
r = 0
for i in range(n-1):
    r = max(mans[i] + range_[i], r)
    if mans[i+1] > r:
        print("엄마 나 전역 늦어질 것 같아")
        exit()
print("권병장님, 중대장님이 찾으십니다")