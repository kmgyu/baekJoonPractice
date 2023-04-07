#1259
while True:
    a = input()
    if a == "0":
        break
    if a == "".join(reversed(a)):
        print("yes")
    else:
        print("no")