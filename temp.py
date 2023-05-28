n = int(input()) #n까지 반복
fib = [1, 1] #기본 피보나치
fib2 = [0] * n
for i in range(2, n):
    fib.append(fib[i-1]+fib[i-2])
    fib2[i] = fib[i-1]+fib[i-2]