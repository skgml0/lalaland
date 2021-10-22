from itertools import combinations
t=int(input())
for _ in range(t):
    n,m = map(int,input().split())
    arr=list(i for i in range(1,m+1))
    res= list(combinations(arr,n))
    print(len(res))

