import sys
n= int(sys.stdin.readline().strip())
stack=[]
answer=[]
cur =1
flag=0

for i in range(n):
    m = int(sys.stdin.readline().strip())
    while cur <=m: #입력한 수를 만날때까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur+=1
        #입력한 수를 만나면 while문 탈출. 즉 cur =m 일때까지 while문 돌아 스택을 쌓는다.

    if stack[-1]==m: #스택의 top이 입력한 숫자와 같다면 꺼내서 answer에 수열을 만든다.
        stack.pop()
        answer.append("-")
    else:  #stack의 top이 입력한 수가 아니면 주어진 스택만들 수 없다
        print("NO")#즉 오름차순 스택으로 저장되지 않은 경우
        flag=1
        break

if flag ==0: # no경우를 제외하고 맞은 경우만 정답 출력할 수 있또록 한다. 
    for i in answer:
        print(i)