#세자리수 두개 . 거꾸로 읽고 크기 비교하여 큰 것 출력한다.
a,b=input().split(" ")
a=int(a)
b=int(b)
a_3=a//100 # 100으로 나눴을 때 정수 7
a_2=(a%100)//10 # 100으로 나눈 나머지.
a_1=(a%100)%10 # 100으로 나누고 10으로 나눈 나머지
a_total= str(a_1)+str(a_2)+str(a_3)
#print(a_total)
b_3=b//100 # 100으로 나눴을 때 정수 7
b_2=(b%100)//10 # 100으로 나눈 나머지.
b_1=(b%100)%10 # 100으로 나누고 10으로 나눈 나머지
b_total= str(b_1)+str(b_2)+str(b_3)
#print(b_total)
if a_total > b_total:
    print(a_total)
else:
    print(b_total)