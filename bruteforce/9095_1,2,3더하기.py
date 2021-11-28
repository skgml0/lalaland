# testcase 정수: t
t= int(input())
# 함수 sol 정의
def sol(n):
    # n이 1이면 1리턴
    if n ==1:
        return 1
    # n이 2이면 2
    elif n==2:
        return 2
    # n이 3이면 4
    elif n==3:
        return 4
    # 그 외 sol의 n값 재귀함수
    else:
        return sol(n-1) +sol(n-2)+sol(n-3)
    #함수 호출 
for _ in range(t):
    n= int(input())
    print(sol(n))
