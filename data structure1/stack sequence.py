#1874
n = int(input()) #수열 길이
number = list(range(1, n+1))
print(number)
pt = 0
for i in range(n):
    num = int(input())
    if num > pt:
        for j in range(num-pt):
            if number[pt]:
                print("+")
                number[pt] = 0
            else:
                continue
            pt += 1

    elif num <= pt:
        for j in range(0, pt-num):
            print("-")
            pt -= 1


print(number, pt)
