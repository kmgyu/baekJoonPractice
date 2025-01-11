n=int(input())
cases = [int(input()) for _ in range(n)]
M=max(cases)
mem=[0 for _ in range(M+1)]
mem[0], mem[1], mem[2] = 0, 2, 3
def euler_p(N):
    num,ans = N,N
    for i in range(2, int(N**0.5)+1):
        if num % i == 0:
            while num % i == 0: num //= i
            ans = ans * (i-1) // i
    if num>1: ans = ans * (num-1) // num
    return ans
for i in range(3, M+1):
    mem[i] = euler_p(i)+mem[i-1]
print(*[mem[i] for i in cases], sep='\n')