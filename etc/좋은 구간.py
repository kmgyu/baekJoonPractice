import sys
size=int(input())
input_set=list(map(int,sys.stdin.readline().strip().split()))
n=int(input())

def sol(size,input_set,n):
    input_set.sort()
    start_num,end_num=0,0
    for i in range(size+1):
        if input_set[i]>n:
            start_num=input_set[i-1]+1
            end_num=input_set[i]-1
            break
        if input_set[i]==n:
            return 0

    return (n-start_num)*(end_num-n+1)+(end_num-n)

#남의꺼 뽀려온거임 버그 개쩜 쓰는거 ㄴㄴ
print(sol(size,input_set,n))