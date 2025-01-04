
n = int(input())
ans = n
i = 2
j = 1
while i < n:
    j = (n-1) // ((n-1)//i)
    ans += (j-i+1)*(1+(n-1)//i)
    i = j+1
if n != 1:
    ans += 1
print(ans)

