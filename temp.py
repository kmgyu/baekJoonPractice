n, s, p = map(int, input().split());ans=n+1
if n:
    S=list(map(int,input().split()))
    if p<=n and S[p-1] >= s: print(-1); exit()
    for i in range(n):
        if S[i]<=s: ans=i+1; break
print(ans)

# n, Eugene, p = map(int, input().split())

# if n == 0:
#     print(1)
# else:
#     ranking = list(map(int, input().split()))
#     if n == p and ranking[-1] >= Eugene:
#         print(-1)
#     else:
#         rank = n + 1
#         for i in range(n):
#             if ranking[i] <= Eugene:
#                 rank = i + 1
#                 break
#         print(rank)