#import sys
T= int(input())
ans=[]
for i in range(T):
    N,M = map(int,input().split())
    #몇 번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇 번째에 놓여 있는지를 나타내는 정수M
    importance= list(map(int,input().split()))
    max_im=importance.index(max(importance))
    #리스트에서 최대값 찾기 max()
    #print("M값",M)
    #print("최고 중요도 인덱스",max_im)
    if max_im == M:
        answer=1
    elif M < max_im:
        answer = N-max_im +1
    elif M > max_im:
        answer = N-max_im
    print(answer)
