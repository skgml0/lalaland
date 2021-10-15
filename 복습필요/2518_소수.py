m = int(input())
n= int(input())
arr = []
for num in range(m, n + 1): # m이상 n 이하 충족시키기 위해.
    count=0
    if num >1: #1은 소수가 아니다
        for j in range(1,num+1): # 소수의 정의, 1과 자기자신
            if num % j ==0: #나누어 떨어질 때 세줌
                count+=1
        if count ==2: # 반복문 1부터 ~n까지 돌았을 때, 소수는 count =2인 경우
            arr.append(num)

if len(arr)>0:
    print("{}".format(sum(arr)))
    print("{}".format(min(arr)))
else:
    print(-1)
