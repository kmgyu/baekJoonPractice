c=[500,100,50,10,5,1]
m=1000-int(input());a=0
for i in c:a+=m//i;m%=i
print(a)