#2920
a = list(map(int, input().split()))
k = list(range(1,9))
if a == k:
    print("ascending")
elif a == list(reversed(k)):
    print("descending")
else:
    print("mixed")