a, b = map(int, input().split())
num = []
while a!=0 and b!=0:
    num.append(a%10+b%10)
    a//=10
    b//=10
if a:print(a, end="")
elif b:print(b, end="")
while num:print(num.pop(), end="")
