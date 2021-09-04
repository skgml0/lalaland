string = list(input())
alpha=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time=0
for i in string:
    for j in alpha:  #해당하는 알파벳이 (리스트인덱스 +2)
            if i in j:
                value=alpha.index(j)
                #print(value)
                #print('출력좀해봐',i)
                time+=3+value
print(time)