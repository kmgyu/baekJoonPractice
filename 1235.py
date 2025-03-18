N=int(input())
S = [input() for _ in range(N)]
s_l = len(S[0])
for j in range(s_l, -1, -1):
    s=set()
    for i in range(N):
        if S[i][j:] in s: break
        s.add(S[i][j:])
    # print(j, len(s))
    if len(s) == N:
        print(s_l-j); exit()
# NodeJS로 리팩토링 해보기..