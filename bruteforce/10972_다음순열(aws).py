# 10972 
n= int(input())
input_array = list(map(int, input().split()))
# 마지막값 빈공백, 그래서 제외
for i in range(n-1,0,-1): # 마지막 항부터 돈다
    if input_array[i-1] < input_array[i] : #만약 앞 열의 값이 그 뒷열의 값보다 작다면
        for j in range(n-1,0,-1): #다시 그 앞 열의 값을 맨 뒷열부터 비교
            if input_array[i-1] < input_array[j]: #그 앞열의 값이 뒤에 있는 어느 열보다 작다면
                input_array[i-1], input_array[j] = input_array[j], input_array[i-1] #그 두 값을 스왑
                input_array = input_array[:i] + sorted(input_array[i:]) #i-1번째까지의 리스트와 그 뒤에 리스트를 정렬한 채 붙인다.
                print(*input_array) # *를 이용해 리스트 내부의 원소들을 공백을 사용하여 출력
                exit() #코드 변환
print(-1) #만약 위에서 코드 종료가 일어나지 않았다면( 마지막 항이라면) -1 출력


