from collections import deque
import sys
n= int(input())
que=deque()
func = list()
for _ in range(n):
    func= sys.stdin.readline().strip().split()
    if func[0] == 'push_front':
        que.appendleft(func[1])
    elif func[0] == 'push_back':
        que.append(func[1])
    elif func[0] == 'pop_front':
        if len(que) > 0:
            print(que.popleft())
        else:
            print(-1)
    elif func[0] == 'pop_back':
        if len(que) > 0:
            print(que.pop())
        else:
            print(-1)
    elif func[0] == 'size':
        print(len(que))
    elif func[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif func[0] == 'front':
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    elif func[0] == 'back':
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)

"""import collections
왼쪽에 요소값 추가하기- 
(1)appendleft
(2)extendleft
dictionary를 이용하여 switch-case문을 구현할 수 있다.
이를 이용해서 key값을 가지고 딕셔너리에 접근하여 대응되는 value값을 통해 함수를 호출
"""
