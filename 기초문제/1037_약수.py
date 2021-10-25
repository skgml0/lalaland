t= int(input())
arr=[]
flag=0

if t==1:
    print(int(input())**2)
    flag=1
else:
    arr=list(map(int,input().split(" ")))
    arr.sort()
if flag==0 :
    print(arr[0]*arr[-1])

