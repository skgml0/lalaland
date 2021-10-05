""" 숫자가 쓰인 카드 n:행개수 m:열개수, 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다. 선택된 행 중 가장 숫자가 낮은 카드 뽑기
처음 카드를 골라낼 행을 선택할 떄, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것응ㄹ 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록
전략을 세워야 한다. """
n,m = map(int,input().split(" "))
arr1=[]
for n in range(n):
    arr=list(input().split(" "))
    #print(min(arr))
    arr1.append(min(arr))
print(max(arr1))
