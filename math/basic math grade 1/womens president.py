#2775번
T = int(input()) #test case
for _ in range(T):
    k = int(input())
    n = int(input())
    floor = list(range(1, 15))
    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]
    print(floor[n-1])


# 최초답안
# z_floor = list(range(1,15)) #1~14
# T = int(input()) #test case
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     floor = list(range(1,15))
#     temp_floor = z_floor
#     for i in range(k):
#         for j in range(n):
#             floor[j] = sum(temp_floor[:j+1])
#         temp_floor = list(floor)
#     print(floor[n-1])

# 숏코딩 돚거
# import math
# i=input
# for n in[int]*int(i()):k=n(i());print(math.comb(k+n(i()),k+1))