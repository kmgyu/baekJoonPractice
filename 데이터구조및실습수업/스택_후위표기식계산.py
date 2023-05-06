oper = list(input().split())
stack = []
for i in oper:
    if i == "+":
        temp = stack.pop()
        stack[-1] += temp
    elif i == "-":
        temp = stack.pop()
        stack[-1] -= temp
    elif i == "*":
        temp = stack.pop()
        stack[-1] *= temp
    elif i == "/":
        temp = stack.pop()
        stack[-1] /= temp
    else:stack.append(int(i))
print(stack[0])

