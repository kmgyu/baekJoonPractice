from sys import stdin
input = stdin.readline
n = int(input())
board = [list(input()) for _ in range(n)]
ans = 0

def count_candy():
    row_cnt, col_cnt = 0, 0
    for k in range(n):
        cnt = 1
        for l in range(n-1):
            if board[k][l] == board[k][l+1]:
                cnt += 1
            else:
                cnt = 1
            row_cnt = max(cnt, row_cnt)
    
    for l in range(n):
        cnt = 1
        for k in range(n-1):
            if board[k][l] == board[k+1][l]:
                cnt += 1
            else:
                cnt = 1
            col_cnt = max(cnt, col_cnt)
    return max(row_cnt, col_cnt)


step = [[-1, 0], [1,0],[0,-1],[0,1]]
for i in range(n):
    for j in range(n):
        for v in range(4):
            nx = i+step[v][0]
            ny = j+step[v][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[i][j] != board[nx][ny]:
                board[nx][ny], board[i][j] = board[i][j], board[nx][ny]
                ans = max(ans, count_candy())
                board[nx][ny], board[i][j] = board[i][j], board[nx][ny]

print(ans)
