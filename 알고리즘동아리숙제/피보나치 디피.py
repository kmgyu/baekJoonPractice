# 1을 0번째 항으로 두었음.
# 바텀-업 방식
n = int(input("몇 번째?: "))
dp = [1, 1] + [0]*(n-2) #초깃값 지정
for i in range(n):
    dp[i] = dp[i-1]+dp[i-2] #점화식
print(f"옛다 {n} 번째! : {dp[n-1]}")

# 탑-다운 방식
top = dict() #딕셔너리로 구현.
top[1] = 1 #초깃값 지정.
top[2] = 1
def topDown(n):
    if n in top: # n번째 값이 저장되어 있을 때
        return top[n] # n번째 값 호출
    else: # 없으면 재귀 호출.
        top[n] = topDown(n-1) + topDown(n-2) #n-1과 n-2의 값을 불러와 n번째 값을 구함.
        return top[n]
n = int(input("몇 번째?: "))
print(f"옛다 {n} 번째! : {topDown(n)}")
