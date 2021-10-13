n,m= map(int,input().split(" "))
a=set()
b=set()
for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())
c=list(a&b)
c.sort()
print(len(c))
for j in c :
    print(j)
    """
집합 자료형 : set([])키워드
s1= set([1,2,3])
s1 {1,2,3}
위와 같이 set()의 괄호 안에 리스트를 입력하여 만들거나 다음과 같이 문자열을 입력
하여 만들 수 도 있다.
s2= set("Hello")
s2 {'e','H','l','o'}>> 특징 1. 중복을 허용하지 않는다. 2.순서가 없다
리스트나 튜플은 순서가 있기(ordered) 때문에 인덱싱을 통해 자료형 값을 얻기 가능
set 자료형은 순서가 없기(unordered)때문에 인덱싱으로 값을 얻을 수 없다. 
* 비어있는 집합 자료형은 s = set()로 만들 수 있다. 

1. 교집합 s1&s2  또는 s1.intersection(s2)
2. 합집합 s1|s2  또는 s1.union(s2)
3. 차집합 s1-s2  또는 s1.difference(s2)

집합 자료형 관련 함수들 s1.add() s1.update([]) s1.remove()
- 값 1개 추가(add)
- 값 여러개 추가(update)
- 특정 값 제거(remove)
    """

