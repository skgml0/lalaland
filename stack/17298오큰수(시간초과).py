import sys
result=[]
n= int(sys.stdin.readline().strip())
stack = list(map(int,sys.stdin.readline().strip().split()))
for i in range(len(stack)):#0~3반복
    for j in range(i+1,len(stack)):#
        #print(i)
        #print(stack[j])
        if stack[i] == max(stack):
            result.append(-1)
            break
        elif stack[i]<stack[j]:
            result.append(stack[j])
            break
result.append(-1)
for k in range(len(result)):
    sys.stdout.write(str(result[k])+" ")


