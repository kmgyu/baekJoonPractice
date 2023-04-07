# 2609번 최대공약수와 최소공배수

a, b = map(int, input().split())
num = a*b
if a < b :
    a, b = b, a
while b > 0:
    temp = a
    a = b
    b = temp%b
print(a)
print(num//a)