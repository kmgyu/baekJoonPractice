n, b = map(int, input().split())
stack = []

while n >= b:
    temp = n%b
    if temp > 9:
        stack.append(chr(temp+55))
    else:
        stack.append(temp)
    n //= b
if n > 9:
    stack.append(chr(n+55))
else:
    stack.append(n)
stack.reverse()
print(*stack, sep="")
