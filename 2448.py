n = int(input())

ex = ["  *  ", " * * ","*****"]
def star(n):
    if n == 1:
        return ex
    else:
        temp = star(n//2)
        l = len(temp)
        li = [" "*(n//2*3) + temp[i] + " "*(n//2*3) for i in range(l)] + [temp[i] + " " + temp[i] for i in range(l)]
        return li
print(*star(n//3), sep="\n")