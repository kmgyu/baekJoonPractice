from collections import Counter
a = Counter(input().upper())
k = max(a.values())
li=[]
for i in a.keys():
    if a[i] == k:
        li.append(i)
if len(li) > 1:
    print("?")
else:
    print(li[0])