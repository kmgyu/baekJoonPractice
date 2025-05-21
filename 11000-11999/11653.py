#소인수분해, 11653번
N = int(input())
i = int(N/2)
k = 2
breaker = False
while True:
    if N == 1:
        break
    if i <= 2:
        i = 3
    for k in range(2, i):
        if N % k == 0:
            print(k)
            N = N//k
            break
        elif N % k != 0 and k == i-1:
            breaker = True
    if breaker:
        print(N)
        break

# 시간 최소로 사용하면서 코드도 짧은 거. 난 여태까지 뭘 만든건가....
# N = int(input())
# if N != 1:
#     i = 2
#     while i <= N**0.5:
#         if N % i == 0:
#             print(i)
#             N = N // i
#             continue
#         i += 1
#     print(N)

