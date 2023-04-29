for i in range(int(input())):
    x, y = map(int, input().split())
    print(int(((y-x)*4-3)**.5))
    #distance = y-x
    #제곱근은 알겠는데 왜 4를 곱하고 3을뺄까...
    