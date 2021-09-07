import sys

n= int(sys.stdin.readline().strip())
stack = list(map(int,sys.stdin.readline().strip().split()))
result=[-1]*n
for i in range(n):#0~n-1까지 n번 반복
    j = i+1
    while(j<n): #i번째와 i+a나머지에서 큰수를 못찾으면 반복
        if max(stack) ==stack[i] :
            break
        elif stack[i] < stack[j]:
            result[i]=stack[j]
            break
        else: j+=1
print(*result)
