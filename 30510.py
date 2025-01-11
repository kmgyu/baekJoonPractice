# 상당히 기묘한 문제
P, Q = map(int, input().split())
# 1/q가 p/q보다 커지는 시점에서, q~1까지의 서로소 합을 구하는 문제
# 아. 추가로 x=0일때 f(x)=1이라 0일때도 구해주어야 한다. 따라서 +1을 추가해야함
# 기묘...

q=0 # 커지는 시점의 q 찾기
for i in range(Q, 0, -1):
    if i*P > Q: continue
    else: q=i; break
# 오일러 피 함수로 서로소 개수 합 구하기
def euler_p(N):
    num = N
    ans = N
    for i in range(2, int(N**0.5)+1):
        if num % i == 0:
            while num % i == 0: num //= i
            ans = ans * (i-1) // i
    if num>1: ans = ans * (num-1) // num
    return ans
ans = 1
for i in range(1, q+1):
    ans += euler_p(i)
print(ans)