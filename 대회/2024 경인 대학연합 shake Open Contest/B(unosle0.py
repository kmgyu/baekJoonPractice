import sys
from collections import Counter, defaultdict

input = sys.stdin.readline
powers = {pow(i, 2):i for i in range(1, 1001)}

N = int(input())
# M = sorted(map(int, input().split()))

t = list(map(int, input().split()))
M = [t[i]*t[j] for i in range(N) for j in range(N)]
M.sort()
print(M)

# N*N 행렬 구성하고 정렬하면 i*i에 있는 원소가 제곱임.
cnts = Counter(M)

elements = [] # 기본 원소들, 이를 이용해 증명해야된다.
for i in range(1, N+1):
    print(M[(i**2)-1], i)
    if M[(i**2)-1] in powers:
        elements.append(powers[M[(i**2)-1]])
    else:
        print("NO")
        exit()

el_cnt = Counter(elements)

pd_cnt = defaultdict(int)

# 원소 곱으로 갯수세기로 검증
for i in el_cnt.keys():
    for j in el_cnt.keys():
        pd_cnt[i*j] += el_cnt[i]*el_cnt[j]

for i in cnts.keys():
    if cnts[i] != pd_cnt[i]:
        print('NO')
        break
else:
    print('YES')

print(cnts, el_cnt, pd_cnt)