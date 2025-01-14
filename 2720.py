p = [25, 10, 5]
for i in range(int(input())):
    c = int(input())
    for i in p:
        print(c//i, end=" ")
        c %= i
    print(c)