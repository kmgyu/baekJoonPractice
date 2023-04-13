from itertools import product
#pypy3로 해결함. 개선 필요.
def findAns(a):
    global t
    global ans
    for i in product(num, repeat=len(str(n))+a):
        temp = ''
        for j in list(i):
            temp += (str(j))
        if abs(int(temp) - n) < ans :
            t = int(temp)
            ans = min(ans, abs(int(temp) - n))

n = int(input())
num_length = int(input())
num = list(range(10))
if num_length:
    k = input().split()
    for i in list(map(int, k)):
        num.remove(i)
ans = 500000
t = 0
for i in range(-1, 2):
    if len(str(n))+i <= 0 or (i == 1 and int(str(n)[0]) <= 4) or (i == -1 and int(str(n)[0]) >= 6):
        continue
    findAns(i)
print(min(ans+len(str(t)),abs(100-n)))