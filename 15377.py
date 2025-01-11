def euler_p(N):
    num,ans = N,N
    for i in range(2,int(N**0.5)+1):
        if num%i==0:
            while num%i==0: num//=i
            ans = ans//i*(i-1)
    if num>1: ans=(ans//num)*(num-1)
    return ans
T=int(input())
for _ in range(T):
    n = int(input())
    if n==0: break
    else: print(euler_p(n+1))
# 시작점으로 복귀해야 하므로, n+1의 점이 나와야 한다.
# 왜 오일러 피 함수를 사용해야 하는가? 나도 알고리즘 분류보기전까진 몰랐다..
# 핵심은, 서로소를 step으로 밟아야 한다는 거다. (이래야 시작점으로 돌아올 수 있다.)
# 왜냐하면... 서로소가 아닌 수는 배수로 이동하게 되고 이에 따라 전부 순회를 돌지 못하게 된다.
# 그래서 서로소를 이용해야 하는 것이다.