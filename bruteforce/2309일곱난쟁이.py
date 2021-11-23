# input 9번 받고 int형 변환 후 list에 넣기
a=list(int(input()) for _ in range(9))
# 9난쟁이 중 진짜 난쟁이의 키 합은 100이므로 가짜의 합 num선언
num=sum(a)-100
# 0~8 총 9번 돔
for i in range(0,9):
    # 1~8 총 8번 , 하나의 0~8 중 숫자와 i+1~8 로 비교하여 num만족 찾기
    for j in range(i+1,9):
        if a[i]+a[j] ==num:
            # 찾은 수를 n1,n2에 선언
            n1,n2=a[i],a[j]
# 해당 값을 리스트에서 삭제
a.remove(n1)
a.remove(n2)
# 리스트 정렬
a.sort()
# 정렬된 리스트 하나씩 출력
for z in range(len(a)):
    print(a[z])
