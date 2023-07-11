n = int(input())

def dfs(num):
    if len(str(num)) == n:
        print(num)
        return
    for i in range(10):
        temp = num*10 + i
        if isPrime(temp):
            dfs(temp)
    

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i ==  0:
            return False
    else:
        return True

for i in (2,3,5,7):
    dfs(i)