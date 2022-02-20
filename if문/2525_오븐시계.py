h,m=map(int,input().split())
plus = int(input())
if (m+plus) >=60 or (m + plus)%60==0 :
    h+=((m+plus)//60)
    m=((m+plus)%60)
    if h >=24:
        h-=24
    print(h,m)
else:
    m+=plus
    print(h,m)