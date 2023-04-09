from collections import Counter
#모음은 vowel
#자음은 consonant
n = int(input())
a1 = list(input())
b1 = list(input())
a2 = [] #자음
b2 = []
vowel = ['a','e','i','o','u']
for i in range(n):
    if a1[i] in vowel:
        pass
    else:
        a2.append(a1[i])
    if b1[i] in vowel:
        pass
    else:
        b2.append(b1[i])
a3 = Counter(a1)
b3 = Counter(b1)
isT = True
for i in a1:
    if a3[i] == b3[i]:
        continue
    else:
        isT = False
        break
#조건들
if (a1[0] != b1[0] or a1[-1] != b1[-1]) or a2 != b2 or len(a3) == 1:
    isT = False

if isT:
    print("YES")
else:
    print("NO")