n= int(input())
count=0
# 00시 00분 00초 ~ n시 59분 59초까지의 모든 시각 중 3이 하나라도 포함될경우
for i in range(n+1):
    for m in range(0,60):
        for s in range(0,60):
            if '3' in str(i)+str(m)+str(s):
                count+=1
print(count)