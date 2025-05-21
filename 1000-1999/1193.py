#1193번
X = int(input())
n=1 #X의 현재 줄 위치
fin = 0
a, b = 0, 0
while X > fin:
    fin = int((n ** 2 + n) / 2)
    if X > fin: n += 1

if n % 2 == 0:
    right = 1
    a = 1
    b = n
else:
    right = -1
    a = n
    b = 1

n -= 1
fin = int((n ** 2 + n) / 2)
if n >= 1 :
    for i in range(X - fin - 1):
        a += right
        b -= right
print(f"{a}/{b}")

#코드를 줄일 방법은 있는거 같은데... 방법을 모르겠다.

"""
X = int(input())
a = 0
b = 0
while X > b:
    a+=1
    b+=a

b -= a

if (a%2 == 1):
    i = a - (X - b) + 1
    j = X - b

else:
    i = X - b
    j = a - i + 1

print(f"{i}/{j}")
위와 같이 만들 수 있다.
"""