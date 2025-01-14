n = int(input())
t = 0
while t*(t+1)/2 < n and n - t*(t+1)/2 > t:
    t += 1
print(t)
