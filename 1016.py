m, M = map(int, input().split())
memo = [1] * (M-m+1)
cnt = M-m+1

# 에라토스테네스의 체 응용
# i의 제곱의 배수들을 지워나간다.
# 몫연산한뒤 곱해서 그 수부터 시작한다!(ex) 30을 4로 나누면 2 남아서 28로 바꿔줘야 함
# j-m으로 음수 체크해줌.
for i in range(2, int(M**0.5)+1):
    for j in range((m//(i**2))*(i**2), M+1, i**2):
        if j-m >= 0 and memo[j-m]:
            cnt-=1
            memo[j-m] = 0
print(cnt)