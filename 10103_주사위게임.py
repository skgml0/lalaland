"""
문제
창영이와 상덕이는 게임을 하고 있다.
게임을 시작하는 시점에서, 두 사람의 점수는 모두 100점이다.
게임은 여섯 면 주사위를 사용하며, 라운드로 진행된다.
매 라운드마다, 각 사람은 주사위를 던진다. 낮은 숫자가 나온 사람은 상대편 주사위에 나온 숫자만큼 점수를 잃게 된다. 두 사람의 주사위가 같은 숫자가 나온 경우에는 아무도 점수를 잃지 않는다.
게임이 끝난 이후에 두 사람의 점수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 라운드의 수 n (1 ≤ n ≤ 15)가 주어진다. 다음 n개 줄에는 두 정수가 주어진다. 첫 번째 정수는 그 라운드에서 창영이의 주사위에 나타난 숫자, 두 번째 정수는 상덕이의 주사위에 나타난 숫자이다. 두 정수는 항상 1보다 크거나 같고, 6보다 작거나 같다.

출력
첫째 줄에 게임이 끝난 이후에 창영이의 점수, 둘째 줄에는 상덕이의 점수를 출력한다.
"""
n = int(input())
s1=100
s2=100
for _ in range(n):
    a,b = map(int,input().split(" "))
    if a>b:
        s2-=a
    elif a<b:
        s1-=b
print(s1)
print(s2)