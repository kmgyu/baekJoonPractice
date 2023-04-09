#2839번
n = int(input())
a = n//5
b = (n % 5)//3

if (n % 5 == 1 or n % 5 == 4) and a > 0:
    a -= 1
    b = ((n % 5)+5)//3
elif n % 5 == 2 and a > 1:
    a -= 2
    b = ((n % 5)+10)//3

if 5*a + 3*b < n:
    print(-1)
else:
    print(a+b)

