t = int(input())
result=[]
for _ in range(t):
    s,e = map(int,input().split(" "))
    result.append([s,e])
s= sorted(result, key=lambda s:s[0])
print('시작시간 오름차순',s)
s= sorted(result, key=lambda s:s[1])
print('시작+끝 시간 오름차순',s)
last =0
cnt=0
# last의 값과 i값을 비교해서 i값이 크다면 개수 추가해준다.
# last= j값으로 갱신해준다.
for i,j in s:
    if i>=last:
        cnt+=1
        last=j
print(cnt)