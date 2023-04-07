#10871번 문제
nx = list(map(int, input().split()))
numlist = list(map(int, input().split()))
result = [numlist[i] for i in range(nx[0]) if nx[1] > numlist[i]]
print(*result)
