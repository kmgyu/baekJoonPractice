from collections import Counter
n = int(input()) #토핑
toping = Counter(input().split())
cnt = 0
for i in toping:
    if len(i) >= 6 and i[-6:] == "Cheese":
        cnt += 1
if cnt >= 4:
    print("yummy")
else:
    print("sad")