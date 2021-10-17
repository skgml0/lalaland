def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): 비어있거나 마지막 일수가 앞 일수보다 크면
            Q.append([-((p-100)//s),1]) #필요한 일수 저장하기
        else: #마지막 일수가 앞 일수보다 작으면 카운트 늘리기
            Q[-1][1]+=1
    print("progresses :{} speeds:{}".format(p,s),Q)
    return [q[1] for q in Q] # 일수만 출력하기
