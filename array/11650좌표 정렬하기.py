import sys
n=sys.stdin.readline().strip() #점 개수
li=[] #리스트 선언
for _ in range(int(n)):
    x,y= map(int,sys.stdin.readline().strip().split())
    li.append([x,y])
li.sort(key = lambda x: (x[0],x[1])) #x좌표 정렬 후 y좌표 정렬한다.

for i in range(int(n)):
    print(li[i][0],li[i][1])
