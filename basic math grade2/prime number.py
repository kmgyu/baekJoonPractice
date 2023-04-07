from math import *

M = int(input())
N = int(input())
prime = list(range(M, N+1))
print("start")
for num in range(M, N+1):
    if num == 1:
        prime.remove(num)
        continue
    i = int(sqrt(num)) + 1
    for k in range(2, i):
        if num % k == 0:
            try:
                prime.remove(num)
            except:
                continue
if len(prime) >= 1:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)




# 일단 더 빨랐던 코드.
# M = int(input())
# N = int(input())
# lst = []
#
# for x in range(M, N+1):
#     if x == 2:
#         lst.append(x)
#     for y in range(2, x):
#         if x % y == 0:
#             break;
#         if y == x-1:
#             lst.append(x)
#             break;
#
# if len(lst) == 0:
#     print(-1)
# else:
#     print(sum(lst))
#     print(min(lst))