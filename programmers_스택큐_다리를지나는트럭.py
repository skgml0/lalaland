def solution(bridge_length, weight, truck_weights):
    answer = 0
    dummy=[]
    n= len(truck_weights)
    #다른 차랑 무게 비교해서 무게가w 이하이고, 차수가 브리지 다리 이하인 경우 한 묶음.
    #만약 트럭 최대 1대만 올라갈 수 있으면?
    i=0
    if bridge_length==1:
        answer = n
    else:#트럭 최대 개수 2개 이상인 경우  #무게가 초과하는 경우와 아닌 경우!
        while i<n: #i가 트럭수보다 작을 경우 동작
            count=1
            w= truck_weights[i]
            for j in range(i+1,n): #다리 한꺼번에 올라갈 수 있는 트럭수와 무게 조건이 충족된다면
                if count <= bridge_length and w+truck_weights[j]<= weight:
                    w+=truck_weights[j]
                    count+=1
                    """여길 어떻게 하지.? """
                else:
                    dummy.append(w)
                    break
            i+=count
            if i== n:
                dummy.append(w)
    return len(dummy)*bridge_length+(n-len(dummy))+1