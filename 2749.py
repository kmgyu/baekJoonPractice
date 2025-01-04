n = int(input())
d = [0, 1, 1]
m = 10**6
p = n%(15*(m//10))
for i in range(2, p):
    d[0],d[1],d[2] = d[1],d[2],((d[1]+d[2])%m)
print(d[2]%m)
# print(d)

#피사노 주기에 대한 것. 모르면 배워랏!!!