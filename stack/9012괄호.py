import sys
n=int(sys.stdin.readline().rstrip())
for i in range(n):
    stack=[] #리스트 먼저 생성
    cnt=0 #0으로 초기화
    arr=sys.stdin.readline().rstrip() #괄호 입력받기
    for j in range(len(arr)): # 입력받은 괄호 하나씩 따지기
        if arr[j] =="(": # 왼쪽 괄호일경우
            stack.append(arr[j]) #stack에 넣는다
        else: # 오른쪽 괄호인 경우
            if len(stack)==0: #stack 개수가 0이면 즉, 처음 상태에서 오른쪽괄호입력이면
                print("NO") #no 출력
                cnt-=1  # 예외상황 조건
                break #반복문 종료
            else: #stack개수가 0이 아니면
                stack.pop() #stack에서 가장 마지막 괄호 나올것
    # 출력물에서 첫시작( 일때 결과 출력하는 것.
    if len(stack)==0 and cnt ==0: #스택의 괄호 쌍이 맞아 남은게 없는 경우
        print("YES")
    elif len(stack)!=0 and cnt==0: #스택의 괄호 쌍이 맞지 않아 남은 경우
        print("NO")


