""" 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의에 대하여 회의실 사용표만들기.
각 회의에 대해 시작시간~끝나는시간, 겹치지 않게 회의실을 사용할 수 있는 회의의 최대 개수 찾기
단, 회의는 한번 시작하면 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. (시작하자마자 끝난다)
"""

# 회의 수
n = int(input())
s=[]
for i in range(n):
    a,b=map(int,input().split(" "))
    s.append([a,b])
s=sorted(s,key=lambda a:a[0])
s=sorted(s,key=lambda a:a[1])
last=0
cnt=0
#print(s)
for i,j in s:
    if i> last:
        cnt+=1
        last =j
print(cnt)