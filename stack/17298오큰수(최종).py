import sys
n= int(sys.stdin.readline().strip())
A= list(map(int,sys.stdin.readline().strip().split()))
result=[-1]*n # 기본값으로 이루어진 -1 배열
stack=[]
stack.append(0) #비어있는 스택에 0 삽입
for i in range(1,n):
    while stack and A[stack[-1]] <A[i]: #stack에 값이 있고 A[0]보다 A[i]값이클때
        result[stack.pop()]=A[i] #stack의 마지막 값을 pop 0이므로 결과 마지막값은 우측큰값
    stack.append(i) #크든작든 인덱스 넣어준다.
print(*result)
