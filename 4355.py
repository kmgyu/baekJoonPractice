def euler_p(N):
    num,ans = N,N
    for i in range(2,int(N**0.5)+1):
        if num%i==0:
            while num%i==0: num//=i
            ans = ans//i*(i-1)
    if num>1: ans=(ans//num)*(num-1)
    return ans
while True:
    n = int(input())
    if n==0: break
    if n==1: print(0)
    else: print(euler_p(n))
