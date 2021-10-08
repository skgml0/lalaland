"""
이항계수 n과 k가 주어지면 nCk = n! /( k! * (n-k) !)
*수학적 개념
이항계수는 이항정리에서 전개된 항의 계수를 의미한다. 이항계수는 음이 아닌 두 개의 지표(index) n,k를 사용하여
기호 nCk로 나타낸다. 이항계수는 거듭제곱 (1+x) ^n 을 전개하였을 때, x^k의 계수이다.
"""
n,k = map(int,input().split())
N,K,M=1,1,1
for n in range(1,n+1):
    N*=n
for k in range(1,k+1):
    K*=k
for m in range(1,n-k+1):
    M*=m
print(N//(K*M)%10007)