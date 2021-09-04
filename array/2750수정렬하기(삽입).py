from sys import stdin, stdout
n= stdin.readline().rstrip()
array=[]
for _ in range(int(n)):
    array.append(int(stdin.readline().rstrip()))
for i in range(1,len(array)):
    for j in range(i,0,-1): #인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        elif array[j]==array[j-1]: # 같은 경우 삭제한다.
            del array[j-1]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
for i in array:
    print(i)
# n개의 줄에는 수가 주어진다: 숫자로 입력받아라.