def func(n):
    if n == 1:
        return ["-"]
    a = n//3
    return func(a) + [" "]*a + func(a)

while True:
    try:
        n = int(input())
        print(*func(3**n), sep="")
    except:
        break