def recursion(a) :
    if (a>0) :
        return (a-1)
    else :
        return 1

n = int(input())
a = 1
while (n >= 1):

    a *= n
    n = recursion(n)
print(a)