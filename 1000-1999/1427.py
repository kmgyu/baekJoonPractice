#1427
n = input()
a = sorted(list(map(int, n)), reverse = True)
print(*a, sep="")
