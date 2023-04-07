#1158 요세푸스 문제

n, k = map(int, input().split())
num = list(range(1, n+1))
index = 0
print("<", end="")
for i in range(n):
    index = (index + k - 1) % len(num) #index + k한 후 배열위치니까 -1, 한바퀴 돌려서 원하는 index 나오려면 mod연산해야함.
    print(num.pop(index), end="")
    if i < n-1:
        print(", ", end="")
print(">")