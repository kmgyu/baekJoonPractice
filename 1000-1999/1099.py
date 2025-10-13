# https://code-angie.tistory.com/25
# 여기서는 암호화된 알파벳을 해석하는 비용으로 정의하였다.
# DP 너무 어려우엉
# 코드 자체는 쉽게 잘만들어져있다.

import sys
input = sys.stdin.readline

# 단어 해석 비용 함수
# 해석 비용 함수 자체는 간단함.
# 여기서 알파벳 검증을 하지 않는다. 참고.
def check(w1,w2,l):
    cnt = 0
    for i in range(l):
        if w1[i] != w2[i]:
            cnt+=1
    return cnt

# 0,0은 0으로 설정하기 위해 공백 추가해줌.
s = " "+input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

inf = float('inf')

dp = [[inf]*(len(s)) for _ in range(len(s))]
dp[0][0] = 0

for i in range(1,len(s)+1):
    if dp[i-1][0] == inf: # 앞서 연결될 수 있는 단어가 없음(현재 위치 이전의 부분 문자열은 조합 불가능함.)
        continue
    for word in words:
        l = len(word)
        # 문자열 s에서 슬라이스하여 정렬, 해석 가능한지(알파벳이 일치하는지) 확인한다.
        if sorted(s[i:i+l]) == sorted(word):
            dp[i][i+l-1] = min(dp[i][i+l-1],dp[i-1][0]+check(s[i:i+l],word,l))
            # i+l-1 위치에 대한 최솟값을 정의해준다. 해당 위치에서 시작할 단어들을 위해 i+l-1,0에 정의됨.
            dp[i+l-1][0] = min(dp[i+l-1][0],dp[i][i+l-1])

# 만약 문장의 모든 단어를 해석할 수 있는 경우(하나도 남김없이 가능)
if dp[-1][0] != inf: 
    print(dp[-1][0])
else: # 해석 불가능함
    print(-1)