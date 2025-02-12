import sys
sys.setrecursionlimit(10**6)

def dfs(cur, value, bits):
    # cur : 현재 탐색할 노드
    # value : 현재 가격
    # bits : 현재 탐색 완료 비트
    bits = bits | (1 << cur) # 비트연산해서 맞춰주기

    if dp[bits][cur]: return dp[bits][cur] # 있으면 탐색 종료
    
    # 갱신
    for i in range(N):
        # 비트 조회가 되었거나(bits) 가격(price)이 크거나 같을 시 넘김
        if bits & (1 << i) or mat[cur][i] < value: continue
        dp[bits][cur] = max(dp[bits][cur], dfs(i, mat[cur][i], bits) + 1)
    
    return dp[bits][cur]


input = open(0).readline

N = int(input())
mat = [list(map(int, input().strip())) for _ in range(N)]
dp = [[0] * (N) for _ in range(2**N)] # 비트 수만큼의 행 * N(대상) 크기의 행렬

print(dfs(0, 0, 0)+1)