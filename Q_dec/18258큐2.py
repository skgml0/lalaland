import sys
from collections import deque

def push(que,x) :
    que.append(x)
def pop(que):
    return que.popleft() if len(que) > 0 else -1
def size(que):
    return len(que)
def empty(que):
    return 0 if len(que)>0 else 1
def front(que):
    return que[0] if len(que)>0 else -1
def back(que):
    return que[-1] if len(que)>0 else -1
n=int(input())
que=deque()
for _ in range(n):
    order= sys.stdin.readline().strip().split()
    a= order[0]
    if a == 'push':
        push(que,order[1])
    elif a=='front':
        print(front(que))
    elif a == 'size':
        print(size(que))
    elif a=='empty':
        print(empty(que))
    elif a=='pop':
        print(pop(que))
    elif a =='back':
        print(back(que))
    #print('function : ',a, ' /que : ',que)