# https://yabmoons.tistory.com/592
# https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80
# A to B 가 팰린드롬일 때에 대한 증명... 이것 또한 dp이다.
# 축소문제와의 연관성을 메모이제이션

input = open(0).readline

S = input()
l = len(S)
dp = [float('inf') for _ in range(l)]
dp[-1] = 0
is_p = [[0] * l for _ in range(l)] # is_palindrome

# 길이가 1일때
for i in range(l):
    is_p[i][i] = 1

# 길이가 2일때
for i in range(1, l):
    if S[i-1] == S[i]: is_p[i-1][i] = 1

# 3일때 팰린드롬
for length in range(3, l+1):
    for start in range(l - length + 1):
        end = start + length - 1
        if S[start] == S[end] and is_p[start+1][end-1]:
            is_p[start][end] = 1

# 팰린드롬 개수 풀이.
for end in range(l):
    for start in range(end+1):
        if is_p[start][end]:
            dp[end] = min(dp[end], dp[start-1] + 1) # -1이므로... dp[-1]을 0으로 초기화...?
        else:
            dp[end] = min(dp[end], dp[end-1] + 1)

print(dp[-2])