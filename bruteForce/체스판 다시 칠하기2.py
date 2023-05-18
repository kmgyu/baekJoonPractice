from sys import stdin
input = stdin.readline
N, M, K = map(int, input().split())

board = [[0]*(M+1) for _ in range(N+1)]
oppo_B = 1 #라인마다 두개는 서로 바뀐다. opposite
oppo_W = 0
for i in range(1, N+1):
    temp = input()
    for j in range(1,M+1):
        if (j % 2 == oppo_B and temp[j-1] == 'B') or (j % 2 == oppo_W and temp[j-1] == 'W'):
            board[i][j] += board[i][j-1]+board[i-1][j]-board[i-1][j-1]
        else:
            board[i][j] += board[i][j-1]+board[i-1][j]-board[i-1][j-1]+1
    oppo_W, oppo_B = oppo_B, oppo_W
ans = 10e9
for i in range(K, N+1):
    for j in range(K, M+1):
        temp = abs(board[i][j]-board[i-K][j]-board[i][j-K]+board[i-K][j-K])
        ans = min(temp, K**2-temp, ans)
print(ans)