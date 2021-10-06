"""
어떤 나라에 n개 도시 .
제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여
이동하려고한다.
인접한 두 도시 사이의 도로들은 서로 길이가 다를 수 있다.

처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발
기름통 크기는 무제한. 도로를 이용하여 이동할 때 1km마다 1리터 기름사용
각 도시에는 단 하나의 주유소가 있으며, 도시마다 주유소의 리터당 가격 다를 수 있다.

각 도시에 있는 주유소의 기름 가격과 각 도시를 연결하는 도로의 길이를 입력으로 받아
제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소비용 계산.

첫번째 줄에는 도시 개수 n
다음 줄에는 인접한 두 도시 연결하는 도로 길이
"""
t= int(input())
distance=list(map(int,input().split(" ")))
price= list(map(int,input().split(" ")))
result=0
#price
#x=price.index(min(price))
for i in range(t-1):
    result += price[i]*distance[i]
    if price[i] < price[i + 1]:
        price[i+1]=price[i]
print(result)