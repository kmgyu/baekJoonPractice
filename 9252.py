import sys
sys.setrecursionlimit(10**5)

#최장 공통부분수열 찾기
def lcs(i, j):
    if i < 0 or j < 0: return
    if lcs_list[i][j] == 0: return
    if lcs_list[i][j-1] == lcs_list[i][j]:
        lcs(i,j-1)
    elif lcs_list[i-1][j] == lcs_list[i][j]:
        lcs(i-1,j)
    else:
        answer.append(m[i-1])
        lcs(i-1, j-1)


n = list(input())
m = list(input())

lcs_list =[[0 for _ in range(len(n) + 1)] for _ in range(len(m) + 1)]
cnt = 0
answer = []

for i in range(len(n)):
    for j in range(len(m)):
        if n[i]==m[j]:
            lcs_list[j+1][i+1] = lcs_list[j][i] + 1
        else:
            lcs_list[j+1][i+1] = max(lcs_list[j][i+1],lcs_list[j+1][i])

print(lcs_list[-1][-1])
if lcs_list[-1][-1]:
    lcs(len(m), len(n))
    print(*answer[::-1], sep="")