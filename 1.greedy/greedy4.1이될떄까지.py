""" n이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 수행
n에서 1을 뺀다 / n이 k로 나누어떨어질 때만 n을 k로 나눌 수 있다.n을 1로 만드는 최소 횟수 셀것"""
n,k = map(int,input().split(" "))
count=0
while(n!=1):
    if n % k !=0 :
        n-=1
        count+1
    else:
        n=n//k
        count+=1
print(count)
