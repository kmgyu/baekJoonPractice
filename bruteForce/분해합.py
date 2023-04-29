n = int(input())
for i in range(max(0, n-100), n):
    if sum(map(int, str(i))) + i == n:
        print(i)
        exit(0)
print(0)