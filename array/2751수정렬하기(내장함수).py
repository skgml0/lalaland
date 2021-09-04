from sys import stdin, stdout
n= stdin.readline().rstrip()
array=set()
for _ in range(int(n)):
    array.add(int(stdin.readline().rstrip()))
array=sorted(array)
for i in array:
    print(i)

"""정렬 알고리즘 문제는 어느 정도 정해진 답이 있는, 즉 외워서 잘 풀어낼 수 있는 문제라고 할 수 있다.
파이썬은 기본 정렬 라이브러리인 sorted()함수를 제공한다. sorted()는 퀵정렬과 동작방식이 비슷한 
병합 정렬 기반으로 만들어졌는데, 병합정렬은 일반적으로 퀵정렬보다 느리지만 최악의 경우에도 시간 복잡도
O(NlogN)을 보장한다는 특징이 있다. 
이러한 sorted() 함수는 리스트, 딕셔너리 자료형 등을 입력받아서 정렬된 결과를 출력한다. 
집합 자료형이나 딕셔너리 자료형을 입력받아도 반환되는 결과는 리스트 자료형이다.\

리스트 변수가 하나 있을 때 내부 원소를 바로 정렬할 수도 있다. 리스트 객체의 내장 함수인 sort()를 \
이용하는 것인데, 이를 이용하면 별도의 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬된다.

또한 sorted()나 sort()를 이용할 때에는 key매개변수를 입력으로 받을 수 있다.
key값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다. 
예를 들어 리스트의 데이터가 튜플로 구성되어 있을 때, 각 데이터의 두 번째 원소를 기준으로 설정하는 경우
다음과 같은 형태의 소스코드를 작성할 수 있다. 혹은 람다함수를 사용할 수 있다
array =[('바나나',2),('사과',5),('당근',3)]
def setting(data):
    return data[1]
result(sorted(array,key=setting)
print(result)  => 결과 [('바나나',2),('당근',3),('사과',5)]"""
