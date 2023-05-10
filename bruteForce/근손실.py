from itertools import*
k=int(input()[2:]);c=0
for i in permutations(map(int,input().split())):
 n=len(i)
 if len([j for j in range(1,n+1)if sum(i[:j])-k*j>=0])==n:c+=1
print(c)