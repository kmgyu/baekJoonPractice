from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
paper = [list(input()) for _ in range(n)]

ans = 0

#모든 경우 구하기
#0인 곳은 가로, 1인 곳은 세로
for h in range(1<<(n*m)): #비트연산 왜 n*m인건데...
    #그건 바로 n*m 을 10000000~ 대충 이렇게 만들고
    #0001 0010100 등등으로 인덱스 뒤집기를 표현하기 때문.(브루트포스)
    temp = 0 #sum
    
    #가로계산
    for i in range(n):
        current = 0
        for j in range(m):
            #한줄로 붙였을 때의 인덱스 k
            k = i*m + j
            
            #k번째 자리값이 0이다(가로 컷)
            if h & (1 << k) == 0:
                current = current*10 + int(paper[i][j])
            else: #세로인 경우 앞에까지 만들어진 조각 sum
                temp += current
                current = 0
        #한 행 끝나면 sum에 더해주기
        temp += current

    #세로 계산
    for j in range(m):
        current = 0
        for i in range(n):
            k = i*m + j
            
            #k번째 자리값이 0이다(세로 컷)
            if h & (1 << k) != 0:
                current = current*10 + int(paper[i][j])
            else:
                temp += current
                current = 0
        temp += current
    
    #최댓갑 계속해서 비교
    ans = max(ans, temp)

print(ans)

#돚거돚거 309ms걸려서 나보다 3배 빠름.
# import sys #백트래킹으로 풀기

# n, m = map(int, sys.stdin.readline().split())
# arr = []
# answer = []
# for _ in range(n):
#     arr.append(list(map(int, sys.stdin.readline().rstrip())))
# check = [[False for _ in range(m)] for _ in range(n)]


# def dfs(i, j):
#     if i==n:
#         answer.append(calc())
#         return

#     if j==m:
#         dfs(i+1,0)
#         return

#     check[i][j]=True
#     dfs(i,j+1)
#     check[i][j]=False
#     dfs(i,j+1)


# def calc() -> int:
#     total = 0
#     for row in range(n):
#         row_sum = 0
#         for col in range(m):  # 가로 연산 체크되어있으면 쭉
#             if check[row][col]:
#                 row_sum = row_sum * 10 + arr[row][col]
#             else:
#                 total += row_sum
#                 row_sum = 0
#         total += row_sum

#     for col in range(m):
#         col_sum = 0
#         for row in range(n):
#             if not check[row][col]:
#                 col_sum = col_sum * 10 + arr[row][col]
#             else:
#                 total += col_sum
#                 col_sum = 0
#         total += col_sum
#     return total

# dfs(0,0)
# print(max(answer))