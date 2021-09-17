from collections import deque
n= int(input())
que=deque()
for i in range(1,n+1):
    que.append(i)
while(len(que)>1):
    que.popleft()
    x= que[0]
    que.append(x)
    que.popleft()
    #print(que)
print(que[0])
# deque 객체 : 스택과 큐를 합친 자료구조이다. 가장자리에 원소를 넣거나 뺄 수 있다.
"""deque(iterable,[,maxlen]) 초기화 함수, iterable(리스트 등)을 인자로 건내면 이를 deque화 시켜준다.
append(x): x를 덱의 오른쪽에 삽입한다.
popleft(): 덱의 가장 왼쪽에 있는 원소를 덱에서 제거하고, 그 값을 리턴한다.
clear(): 모든 원소를 지운다.
스택과 달리 큐를 list로 이용하지 않는 이유: 스택에서 list.append와 list.pop()을 이용했던 것처럼
 list.append와 list.pop(0)을 이용하면 리스트를 큐처럼 사용할 수 있다. 하지만 pop()의 시간복잡도는 O(1)인 
 반면 pop(0)의 시간복잡도는 O(N)이기 때문에 시간이 오래 걸린다. 따라서 시간 복잡도를 고려해 리스트는 큐로
 사용하지 않는다."""