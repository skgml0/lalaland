import sys
while 1:
    stack=[] #리스트 먼저 생성
    #cnt=0 #0으로 초기화
    arr=sys.stdin.readline().rstrip() #괄호 입력받기
    temp = 1
    if arr=='.':
        break
    for j in arr: # 입력받은 괄호 하나씩 따지기
        #print('stack:',stack,'arr:',j,"len(stack",len(stack))

        if j == ".":
            break
        elif j =="(" or j=="[": # 왼쪽 괄호일경우
            stack.append(j) #stack에 넣는다
        elif  j ==")" :
            if len(stack)==0:
                temp=0
                break
            elif len(stack)>0 and stack[-1]=="(" :
                stack.pop()
            else:
                temp = 0
                break
        elif j =="]" :
            if len(stack) == 0:
                temp = 0
                break
            elif len(stack)>0 and stack[-1] == "[":
                stack.pop()
            else:
                temp=0
                break

    if temp==1 and not stack:
        print('yes')
    else:
        print('no')
#print('끝')





