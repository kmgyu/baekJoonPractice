from math import *
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    W=int(ceil(N/H))
    if N%H:H=N%H
    print(str(H)+str(W).zfill(2))

#맨처음 만든 정답버전
# import sys
# from math import *
# T = int(sys.stdin.readline()) # 테스트 시행 횟수
# for i in range(T):
#     H, W, N = map(int, sys.stdin.readline().split())# 층, 방, 손님
#     W = int(ceil(N/H))
#     if N%H:H=N%H
#     else: pass
#     print(str(H) + str(W).zfill(2))

#맞힌사람 돚거
# import sys
# input = sys.stdin.readline
# 
# for _ in range(int(input().rstrip())):
#     h,w,n = map(int,input().split())
#     print(str((n-1)%h+1) + str((n-1)//h+1).rjust(2,'0')) 