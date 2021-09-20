a,b = map(int,input().split())
num=[]
for i in range(2,max(a,b)//2):
    #print("i : {} a: {}, b:{}".format(i,a,b))
    if max(a,b)% min(a,b)==0:
        print(min(a,b))
        print(max(a,b))
        break

    elif a % i ==0 and b % i ==0:
        a=a//i
        b=b//i
        num.append(i)
    gcd = 1
    lcm = a * b
    for j in num:
        gcd *= j
        lcm *= j
    print(gcd)
    print(lcm)


