from collections import deque
import sys
#testcase 개수
t=int(input())
for _ in range(t):
    p=input() #수행할 함수
    n= int(input()) #배열에 들어있는 수의 개수 n
    # [X1..Xn]과 같은 형태로 주어짐-1부터 -1전까지 []제외하고 ,로 나눠준다.
    x= sys.stdin.readline().strip()[1:-1].split(",")
    queue=deque(x) # x를 deque형태로 바꿔준다.
    #print(x)
    flag=0 #마지막에 error와 출력값 동시 나오지 않도록 하기 위한 구분
    turn=0 #뒤집는 횟수 축적, 짝수일 경우 그대로이므로 홀수인 경우만 출력 바꿔준다.
    if n ==0: #입력 개수가 없는 경우
        queue=[] #빈 큐로 초기화시켜준다. (공백제거)

    for f in p: #입력받은 한줄 함수를 한개씩 출력
        #print(f)
        if f =='R': #만약 뒤집기라면 횟수 증가
            turn+=1
        elif f=='D': # 버리기라면
            if len(queue)<1: #큐가 비어있는 경우는 error출력, flag=1로 바꿔주고 끝낸다.
                flag=1
                print('error')
                break

            else: # 큐가 비어있지 않다면
                if turn %2 ==0: #짝수번인 경우, 그대로이므로 맨 왼쪽 제거
                    queue.popleft()
                else: # 큐가 홀수번인경우 오른쪽에서 삭제한 후 뒤집어준다.
                    queue.pop()
    if flag ==0: #flag=1인경우 제외하고 큐 출력해준다.
        if turn %2 ==0:
            print("["+",".join(queue)+"]")
        else:
            print("["+",".join(reversed(queue))+"]")
""".join(리스트)
매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수
1) "".join(리스트) : 매개변수로 들어온 ['a','b','c']이런 식의 리스트를 'abc'의 문자열로
합쳐서 반환해주는 함수
2) "구분자".join(리스트) : 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의
문자열로 합쳐줌. '_'.join(['a','b','c'])라 하면 "a_b_c"와 같은 형태로 문자열을 만들어서 반환

"""

