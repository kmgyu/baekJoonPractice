while True:
    s = input().strip().lower()
    if s == "#":break
    
    c = s[0]
    s1 = s[2:]
    print(c, s1.count(c))