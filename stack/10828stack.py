import sys
n=int(sys.stdin.readline().rstrip())
a=[]
for _ in range(n):
    k=sys.stdin.readline().rstrip().split()
    if k[0] == "push" :
        a.append(k[1])
    elif k[0] =="pop":
        if len(a)>0:
            print(a[-1])
            a.pop()
        else:
            print(-1)
    elif k[0]=="size":
        print(len(a))
    elif k[0] =="empty":
        if len(a)==0:
            print(1)
        else: print(0)
    elif k[0]=="top":
        if len(a)>0:
            print(a[-1])
        else: print(-1)