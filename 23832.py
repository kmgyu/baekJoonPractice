n=int(input())
def euler_p(N):
    num = N
    ans = N
    for i in range(2, int(N**0.5)+1):
        if num % i == 0:
            while num % i == 0: num //= i
            ans = ans * (i-1) // i
    if num>1: ans = ans * (num-1) // num
    return ans
ans = 0
for i in range(2, n+1):
    ans += euler_p(i)
print(ans)