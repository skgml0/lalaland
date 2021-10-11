"""
정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 문제
첫째줄 정수 n 입력
3이 하나라도 포함되는 모든 경우
"""
n= int(input())
count=0
h=0
m=0
s=0
for time in range(n*60*60):
    h= str(time //3600)
    m= str(time //60 %60)
    s= str(time % 3600 %60)
    print("{}시 {}분 {}초".format(h, m, s))
    print(h+m+s)
    if "3" in h+m+s:
        count+=1
        print("{}시 {}분 {}초 3체크{}".format(h,m,s,count))
#print("시간 {}, 분 {}, 초{}".format(h,m,s))
print(count)