n=int(input())

def euler_p(N):
    num = N # target
    ans = N
    for i in range(2, int(n**0.5)+1):
        if num % i == 0:
            # 소인수분해
            while num % i == 0: num //= i
            # euler's phi function
            # n * (1-1/p) * (1-1/q) * ... * (1-1/pn)
            # floating point error sucks. use integer division
            ans = ans * (i-1) // i
    
    # self-prime number
    if num>1: ans = ans * (num-1) // num
    return ans

ans = euler_p(n)
print(ans)