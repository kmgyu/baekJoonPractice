import sys
from collections import deque
input = sys.stdin.readline

# heapq를 썼더니 deque보다 더 빠르게 나왔다... 왜지???

L = int(input()) # 길이
ml, mk = map(int, input().split()) # 기관총 유효사거리, 데미지
C = int(input()) # 유탄
Z = [int(input()) for _ in range(L)] # 좀비 갯수

mcnt = 1 # 기관총 사용횟수.

def solve(L, ml, mk, C, Z):
    expire = deque()
    c_damage = 0
    for i in range(L):
        while expire and expire[0] <= i:
            expire.popleft()
            c_damage -= 1
        if Z[i] > mk*(c_damage + 1):
            if C: C -= 1
            else: return "NO"
        else:
            c_damage += 1
            expire.append(i+ml)
    return "YES"

print(solve(L, ml, mk, C, Z))