import itertools 
stature = []

for _ in range(9):
    stature.append(int(input()))

for i in itertools.combinations(stature,7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
