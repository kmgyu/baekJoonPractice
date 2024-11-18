memo = dict()
song = list(map(int, input().split()))
n = song[0]

def solve(n, song):
    if n==0:
        if song[0] == song[1] == song[2] == 0: return 1
        else: return 0
    
    if (song[0], song[1], song[2], n) in memo:
        return memo[(song[0], song[1], song[2], n)]

    res = 0
    for i in range(1, 8):
        a=song[0] - (i&1>0)
        b=song[1] - (i&2>0)
        c=song[2] - (i&4>0)
        if a<0 or b<0 or c<0: continue
        res+=solve(n-1, [a, b, c])
    memo[(song[0], song[1], song[2], n)] = res%1_000_000_007
    # print(res, n)
    return memo[(song[0], song[1], song[2], n)]

print(solve(n, song[1:]))

# import sys
# 조합을 이용한 풀이
# https://www.acmicpc.net/source/52542954

# def comb(N, M):
#     result = 1
#     for n in range(N, N - M, -1):
#         result *= n
#     for m in range(M, 0, -1):
#         result //= m
#     return result


# S, d, k, h = map(int, sys.stdin.readline().split())

# if d + k + h < S:
#     print(0)
#     exit()

# d, k, h = sorted([d, k, h])
# result = 0
# select_h = comb(S, h) % 1000000007
# residue = S - h
# for nk in range(k + 1):
#     for nd in range(d, -1, -1):
#         if residue == nk + nd:
#             result += select_h * comb(residue, nk) * comb(S - nk, k - nk) * comb(h, d - nd)
#             result %= 1000000007

# print(result)