n = int(input())
f = int(input())
n = int(str(n)[:-2] + "00")
while True:
    if n % f == 0:
        break
    n += 1
print(str(n)[-2:])