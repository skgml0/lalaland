t= int(input())
for _ in range(t):
    b,a = map(int, input().split())
    b1,a1=b,a
    while(b!=0):
        n=a%b
        a,b=b,a
        b=n
    gcd=a
    print(a1*b1//gcd)
