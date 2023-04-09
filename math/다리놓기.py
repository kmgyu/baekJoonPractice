#1010번 다리놓기
from math import factorial
for i in range(int(input())):
    a, b = map(int, input().split())
    temp = 1
    for i in range(b, b-a, -1):
        temp *= i
    temp /= factorial(a)
    print(int(temp), sep=" ")
print()