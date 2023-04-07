def factorial(ans) :
    num = 1
    for i in range(2,ans+1):
        num *= i
    return num

n, k = map(int, input().split())
print(int(factorial(n) / (factorial(n-k) * factorial(k))))
