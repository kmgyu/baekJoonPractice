from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
pokedex = dict()
dexnum = dict()
for i in range(1, n+1):
    temp = input().rstrip()
    pokedex[i] = temp
    dexnum[temp] = i
for i in range(m):
    temp = input().rstrip()
    try:
        print(pokedex[int(temp)])
    except:
        print(dexnum[temp])