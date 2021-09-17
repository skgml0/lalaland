from collections import deque
import sys
def push_front(x,deq):
    tmp = [x]
    tmp.extend(deq)
    deq = tmp
    return deq
def push_back(x,deq):
    deq.append(x)
def pop_front(deq):
    if deq:
        print(deq.popleft())
    else: #빈 덱일 경우
        print(-1)
def pop_back(deq):
    if deq:
        print(deq.pop())
    else:
        print(-1)
def size(deq):
    print(len(deq))
def empty(deq):
    if not deq:
        print(1)
    else:
        print(0)
def front(deq):
    if deq:
        print(deq[0])
    else:
        print(-1)
def back(deq):
    if deq:
        print(deq[-1])
    else:
        print(-1)
statements_dict ={
    'push_front' : push_front,
    'push_back' : push_back,
    'pop_front' : pop_front,
    'pop_back' :pop_back,
    'size' : size,
    'empty': empty,
    'front' : front,
    'back': back
}
n= int(sys.stdin.readline())
deq= deque()
for _ in range(n):
    statement = input().split(" ")
    if len(statement) ==1:
        cmd= statement[0]
        statements_dict[cmd](deq)
    else:
        cmd,x= statement
        deq = statements_dict[cmd](x,deq)

# 다시 찾아보자!