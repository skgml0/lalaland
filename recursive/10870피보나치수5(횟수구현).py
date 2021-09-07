counter =0
def fibonacci(n):
    #어떤 피보나치 수를 구하는지 출력
    print("fibonacci({})를 구합니다".format(n))
    global counter
    counter +=1
    #피보나치 수를구합니다.
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=fibonacci(int(input()))
print(n)
print("fibonacci({})계산에 활용된 덧셈 횟수는 {}번입니다.".format(n,counter) )