import sys
input = sys.stdin.readline
while True:
    try:
        x = int(input()) * (10**7)
        n = int(input())
        pieces = [int(input()) for _ in range(n)]
        temp=0
        if x%2==0 and pieces.count(x//2)>=2:
            temp = x//2
        finder = set(pieces)
        for piece in pieces:
            if x-piece in finder and piece*2 != x:
                print('yes', piece, x-piece)
                break
        else: 
            if temp: print('yes', temp, temp)
            else: print('danger')
    except:
        break