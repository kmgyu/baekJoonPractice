#1546번
a = int(input())
b = list(map(int, input().split()))
print(sum(b)/a/max(b)*100)