li = []
while True:
    name, age, weight = input().split()
    age, weight = int(age), int(weight)
    if name == '#' and (age, weight) == (0,0):
        break
    if age > 17 or weight >= 80:
        li.append([name, "Senior"])
    else:
        li.append([name, "Junior"])
for i in li:
    print(*i)