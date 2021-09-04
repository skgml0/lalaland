t=int(input())
for i in range(t):#테스트케이스 실행횟수
    s=[] # s는 리스트
    p=[]
    r,s=input().split() #r은 반복횟수 s는 문자열
    for j in s:# s에서 한글자씩 갖고오기
        p.append(j*int(r))
    p="".join(p)
    print(p)