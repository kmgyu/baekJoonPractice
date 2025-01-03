import sys
input = sys.stdin.readline
# 1,2,3번 연산을 메인으로 검사하면 된다.
# 1번과 2번은 동치이고 3번도 동치...? 라고 볼 수 있다. 2번과 4번만 이용한다고 보면 된다.
S = list(input().strip())

n = len(S)
res = [[-1 for _ in range(n)] for _ in range(n)]

def check(i, j):
    if res[i][j] != -1: return res[i][j]
    if i >= j: return 0
    res[i][j] = min(check(i+1, j)+1, check(i, j-1)+1, check(i+1, j-1)+(S[i]!=S[j])) # 왼쪽 삭제, 오른쪽 삭제, 팰린드롬 체크(진짜 팰린드롬일 수 있음)
    return res[i][j]

def solve(S):
    global res
    ans = check(0, n-1)
    for i in range(n):
        for j in range(i+1, n):
            res = [[-1 for _ in range(n)] for _ in range(n)] # 초기화하고 교체했을 때에 대한 체크. (4번은 교환)
            S[i], S[j] = S[j], S[i]
            ans = min(ans, check(0, n-1)+1)
            S[i], S[j] = S[j], S[i]
    print(ans)

solve(S)